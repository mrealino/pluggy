#!/usr/bin/env python3
"""Integra um documento HTML autônomo como painel de uma aba do estudo.

O documento recebido é uma página completa, com tokens `:root` de mesmo nome
dos nossos e classes genéricas (.box, .tag, .step, .hier...) que as outras
abas também usam. Colado cru, ele reestilizaria o documento inteiro.

O isolamento é feito em duas camadas, de propósito redundantes:

1. **Prefixo nas classes** — toda classe do documento recebe `om-`, de modo
   que nenhuma colide com as nossas nem em um sentido nem no outro.
2. **Escopo no seletor** — cada regra passa a valer só dentro do painel, e os
   tokens `:root` viram tokens do painel, herdados só ali dentro.

Uso:
    python3 scripts/integrar-aba.py <documento.html> <id-do-painel>
"""

import io
import re
import sys

ALVO = "docs/estudo-jtbd-widget.html"
PREFIXO = "om-"

# Regras que o host do artefato já fornece e que não devem ser reescopadas.
DESCARTAR = ("html", "body", "img", "[hidden]")


def classes_usadas(html, css):
    nomes = set()
    for attr in re.findall(r'class="([^"]*)"', html):
        nomes.update(attr.split())
    for sel in re.findall(r"\.([A-Za-z_][\w-]*)", css):
        nomes.add(sel)
    return {n for n in nomes if not n.startswith(PREFIXO)}


def prefixar(html, css, nomes):
    """Renomeia as classes nos dois lados, por token inteiro."""
    def nos_atributos(m):
        vals = " ".join(PREFIXO + c if c in nomes else c for c in m.group(1).split())
        return 'class="%s"' % vals

    html = re.sub(r'class="([^"]*)"', nos_atributos, html)
    for n in sorted(nomes, key=len, reverse=True):
        css = re.sub(r"\.%s\b" % re.escape(n), ".%s%s" % (PREFIXO, n), css)
    return html, css


def escopar_seletor(sel, painel):
    partes = []
    for p in (s.strip() for s in sel.split(",")):
        if not p:
            continue
        # Tokens do tema: viram tokens do painel, preservando o gate do tema.
        if p == ":root":
            partes.append("#" + painel)
        elif p.startswith(":root") and ("[data-theme" in p or ":not(" in p):
            partes.append("%s #%s" % (p, painel))
        elif p.split()[0].split(":")[0] in DESCARTAR or p in DESCARTAR:
            continue
        else:
            partes.append("#%s %s" % (painel, p))
    return ",".join(partes)


def escopar(css, painel):
    """Aplica o escopo regra a regra, preservando @media e sua ordem."""
    def bloco(trecho):
        saida = []
        for regra in re.findall(r"([^{}]+)\{([^{}]*)\}", trecho):
            sel, corpo = regra[0].strip(), regra[1].strip()
            if sel.startswith("/*"):  # comentário solto antes do seletor
                sel = re.sub(r"^/\*.*?\*/\s*", "", sel, flags=re.S).strip()
            if not sel or not corpo:
                continue
            novo = escopar_seletor(sel, painel)
            if novo:
                saida.append("%s{%s}" % (novo, corpo))
        return "\n".join(saida)

    saida, pos = [], 0
    for m in re.finditer(r"(@media[^{]*)\{((?:[^{}]*\{[^{}]*\}\s*)*)\}", css):
        saida.append(bloco(css[pos:m.start()]))
        saida.append("%s{\n%s\n}" % (m.group(1).strip(), bloco(m.group(2))))
        pos = m.end()
    saida.append(bloco(css[pos:]))
    return "\n".join(s for s in saida if s.strip())


def main():
    if len(sys.argv) != 3:
        sys.exit("uso: integrar-aba.py <documento.html> <id-do-painel>")
    origem, painel = sys.argv[1], sys.argv[2]

    doc = io.open(origem, encoding="utf-8").read()
    css = "\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", doc))
    corpo = doc[doc.index("<body") :]
    corpo = corpo[corpo.index(">") + 1 : corpo.index("</body>")]
    corpo = re.sub(r"<(style|script)[\s\S]*?</\1>", "", corpo)

    # <main> aninhado dentro do nosso <main> é inválido; vira div e o
    # seletor irmão da alternância de idioma acompanha a troca.
    corpo = corpo.replace("<main>", '<div class="omap">').replace("</main>", "</div>")
    css = css.replace("~main ", "~.omap ").replace("main{", ".omap{")

    nomes = classes_usadas(corpo, css)
    corpo, css = prefixar(corpo, css, nomes)
    css = escopar(css, painel)

    alvo = io.open(ALVO, encoding="utf-8").read()
    abre = alvo.index('id="%s"' % painel)
    ini = alvo.index(">", abre) + 1
    fim = alvo.index("</section>", ini)
    novo = alvo[:ini] + "\n<style>\n" + css + "\n</style>\n" + corpo.strip() + "\n" + alvo[fim:]

    io.open(ALVO, "w", encoding="utf-8").write(novo)
    print("%s -> #%s | %d classes prefixadas | css %d KB | painel %d KB"
          % (origem.split("/")[-1], painel, len(nomes), len(css) // 1024, len(corpo) // 1024))


if __name__ == "__main__":
    main()
