#!/usr/bin/env python3
"""Exporta uma aba de docs/estudo-jtbd-widget.html como HTML autocontido.

O documento publicado é um fragmento: a plataforma de artefatos injeta o
esqueleto (doctype, head, reset) na publicação. Um arquivo exportado precisa
carregar esse esqueleto por conta própria para abrir com duplo clique, ser
anexado num e-mail ou impresso.

Uso:
    python3 scripts/export-aba.py estudo
    python3 scripts/export-aba.py gates docs/export/gates.html
"""

import io
import os
import re
import sys

FONTE = "docs/estudo-jtbd-widget.html"

# Rótulo e subtítulo de cada aba exportável.
ABAS = {
    "main":    ("Síntese",           "análise cruzada das quatro linhas de investigação"),
    "estudo":  ("Estudo",            "job map, outcomes, funil e hipóteses"),
    "mapa":    ("Mapa do widget",    "telas, conectores, eventos e perdas estruturais"),
    "modelo":  ("Banco de outcomes", "formulações para testar em entrevista"),
    "gates":   ("Gates × jobs",      "o modelo de gates cruzado com o job map"),
}

# Regras de CSS que só existem para a navegação em abas.
SELETORES_DE_ABA = (".tabs", ".tab", ".panel", ".tab-main", ".tab-sep")


def extrair(html, marcador, fim):
    i = html.index(marcador)
    return html[i:html.index(fim, i) + len(fim)]


def extrair_painel(html, aba):
    """Devolve o conteúdo interno de <section id="panel-{aba}">."""
    abre = html.index('id="panel-%s"' % aba)
    corpo = html.index(">", abre) + 1
    return html[corpo:html.index("</section>", corpo)].strip()


def limpar_css(css):
    """Remove as regras de navegação: num export não há abas para navegar.

    Percorre o CSS na ordem original e trata os blocos @media como unidades.
    A ordem importa: os tokens do tema escuro são redefinições dos claros e
    precisam continuar depois deles — e dentro do próprio @media, senão
    passam a valer sempre.
    """
    def e_regra_de_aba(regra):
        seletor = regra.split("{", 1)[0]
        return any(
            re.search(r"(^|[\s,>])%s([\s,:\[{.]|$)" % re.escape(s), seletor)
            for s in SELETORES_DE_ABA
        )

    saida, pos = [], 0
    for bloco in re.finditer(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\}\s*)*\}", css):
        for regra in re.findall(r"[^{}]+\{[^{}]*\}", css[pos:bloco.start()]):
            if not e_regra_de_aba(regra):
                saida.append(regra.strip())
        saida.append(bloco.group(0).strip())  # intacto, na posição original
        pos = bloco.end()
    for regra in re.findall(r"[^{}]+\{[^{}]*\}", css[pos:]):
        if not e_regra_de_aba(regra):
            saida.append(regra.strip())
    return "\n".join(saida)


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ABAS:
        sys.exit("Abas disponíveis: %s" % ", ".join(ABAS))

    aba = sys.argv[1]
    destino = sys.argv[2] if len(sys.argv) > 2 else "docs/export/%s.html" % aba
    rotulo, subtitulo = ABAS[aba]

    html = io.open(FONTE, encoding="utf-8").read()
    titulo = re.search(r"<title>(.*?)</title>", html).group(1)
    fontes = "\n".join(re.findall(r"<link[^>]*>", html))
    css = limpar_css(extrair(html, "<style>", "</style>"))
    painel = extrair_painel(html, aba)

    saida = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s — %(rotulo)s</title>
%(fontes)s
%(css)s
  *{box-sizing:border-box}
  img{max-width:100%%}
  [hidden]{display:none!important}
</style>
</head>
<body>
<main>

<header>
  <h1>%(titulo)s</h1>
  <p class="meta">%(rotulo)s · %(subtitulo)s</p>
  <p class="caption">Aba <b>%(rotulo)s</b> exportada do documento completo, que reúne cinco
  linhas de investigação. Este arquivo contém apenas esta aba.</p>
</header>

%(painel)s

</main>
</body>
</html>
""" % dict(titulo=titulo, rotulo=rotulo, subtitulo=subtitulo,
           fontes=fontes, css=css, painel=painel)

    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    io.open(destino, "w", encoding="utf-8").write(saida)
    print("%s -> %s (%d KB)" % (aba, destino, len(saida) // 1024))


if __name__ == "__main__":
    main()
