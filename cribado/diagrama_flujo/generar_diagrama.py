#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagrama de flujo PRISMA 2020 — review-gea-biotico.
Reproducible: los números provienen de busqueda/registro_ejecucion.md y cribado/.
Genera ES y EN en PDF (vector), SVG y PNG 300 dpi, en este mismo directorio.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK = "#1a1a1a"; EDGE = "#3a3a3a"; MUT = "#555555"
BAR_BG = "#e8e6e1"; BOX_BG = "#ffffff"

ES = dict(
    fases=["Identificación", "Cribado", "Incluidos"],
    A=("Registros identificados en bases de datos (n = 644)",
       ["•  Web of Science Core Collection (n = 194)", "•  Scopus (n = 197)", "•  OpenAlex (n = 253)"]),
    B=("Registros eliminados antes del cribado:", ["•  duplicados entre bases (n = 318)"]),
    C=("Registros cribados por título y resumen (n = 326)", []),
    D=("Registros excluidos (n = 299)",
       ["•  sin GEA espacial con predictor biótico,", "    u otro tema (n = 296)",
        "•  preprints elegibles, excluidos por la regla", "    de solo-arbitrados [Enmienda 5] (n = 3)"]),
    E=("Informes buscados para su recuperación (n = 27)", []),
    F=("Informes no recuperados (n = 0)", []),
    G=("Informes evaluados a texto completo (n = 27)", []),
    H=("Informes excluidos, con razón (n = 10)",
       ["•  sin GEA con predictor biótico medido", "    o modelado (n = 5)",
        "•  sin datos genómicos de descubrimiento", "    a escala genómica [Enmienda 3c] (n = 4)",
        "•  proxy de recurso sin identidad de", "    interactor [Enmienda 3d] (n = 1)"]),
    I=("Estudios incluidos en la síntesis (n = 17)",
       ["•  del barrido preliminar declarado en el protocolo (n = 6)", "•  nuevos de la búsqueda sistemática (n = 11)"]),
    pie="Protocolo preinscrito (release v0.1-protocolo, commit 6f5d943) y enmiendas 1–5 en github.com/CEEP10101991/review-gea-biotico",
    archivo="flujo_prisma_es",
)

EN = dict(
    fases=["Identification", "Screening", "Included"],
    A=("Records identified from databases (n = 644)",
       ["•  Web of Science Core Collection (n = 194)", "•  Scopus (n = 197)", "•  OpenAlex (n = 253)"]),
    B=("Records removed before screening:", ["•  duplicates across databases (n = 318)"]),
    C=("Records screened (title and abstract) (n = 326)", []),
    D=("Records excluded (n = 299)",
       ["•  no spatial GEA with a biotic predictor,", "    or off-topic (n = 296)",
        "•  eligible preprints, excluded under the", "    peer-reviewed-only rule [Amendment 5] (n = 3)"]),
    E=("Reports sought for retrieval (n = 27)", []),
    F=("Reports not retrieved (n = 0)", []),
    G=("Reports assessed for eligibility (full text) (n = 27)", []),
    H=("Reports excluded, with reasons (n = 10)",
       ["•  no GEA with a measured or modelled", "    biotic predictor (n = 5)",
        "•  no genome-scale discovery markers", "    [Amendment 3c] (n = 4)",
        "•  resource proxy without interactor", "    identity [Amendment 3d] (n = 1)"]),
    I=("Studies included in the synthesis (n = 17)",
       ["•  from the declared preliminary scoping (n = 6)", "•  new from the systematic search (n = 11)"]),
    pie="Pre-registered protocol (release v0.1-protocolo, commit 6f5d943) and amendments 1–5 at github.com/CEEP10101991/review-gea-biotico",
    archivo="flujo_prisma_en",
)

def caja(ax, x, y, w, h, titulo, lineas, fs=7.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.006,rounding_size=0.008",
                                fc=BOX_BG, ec=EDGE, lw=1.0, zorder=3))
    cx = x + w / 2
    if lineas:
        ax.text(cx, y + h - 0.014, titulo, ha="center", va="top", fontsize=fs,
                color=INK, fontweight="bold", zorder=4)
        ax.text(x + 0.02, y + h - 0.046, "\n".join(lineas), ha="left", va="top",
                fontsize=fs - 0.7, color=MUT, zorder=4, linespacing=1.45)
    else:
        ax.text(cx, y + h / 2, titulo, ha="center", va="center", fontsize=fs,
                color=INK, fontweight="bold", zorder=4)

def flecha(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=11, lw=1.0, color=EDGE,
                                 shrinkA=0, shrinkB=1, zorder=2))

def dibujar(T):
    fig, ax = plt.subplots(figsize=(9.8, 8.2))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    XL, WL = 0.085, 0.44          # columna principal
    XR, WR = 0.575, 0.385         # columna de exclusiones
    # alturas de cajas (y = base)
    yA, hA = 0.835, 0.125
    yC, hC = 0.660, 0.062
    yE, hE = 0.525, 0.062
    yG, hG = 0.390, 0.062
    yI, hI = 0.155, 0.095
    yB, hB = 0.862, 0.082
    yD, hD = 0.605, 0.148
    yF, hF = 0.525, 0.062
    yH, hH = 0.255, 0.200

    # barras de fase
    fases = [(0.79, 0.20, T["fases"][0]), (0.32, 0.42, T["fases"][1]), (0.13, 0.14, T["fases"][2])]
    for by, bh, lab in fases:
        ax.add_patch(FancyBboxPatch((0.012, by), 0.042, bh, boxstyle="round,pad=0.004,rounding_size=0.008",
                                    fc=BAR_BG, ec="none", zorder=1))
        ax.text(0.033, by + bh / 2, lab, rotation=90, ha="center", va="center",
                fontsize=9, color=INK, fontweight="bold")

    caja(ax, XL, yA, WL, hA, *T["A"]); caja(ax, XR, yB, WR, hB, *T["B"])
    caja(ax, XL, yC, WL, hC, *T["C"]); caja(ax, XR, yD, WR, hD, *T["D"])
    caja(ax, XL, yE, WL, hE, *T["E"]); caja(ax, XR, yF, WR, hF, *T["F"])
    caja(ax, XL, yG, WL, hG, *T["G"]); caja(ax, XR, yH, WR, hH, *T["H"])
    caja(ax, XL, yI, WL, hI, *T["I"])

    cx = XL + WL / 2
    flecha(ax, cx, yA, cx, yC + hC)          # A -> C
    flecha(ax, cx, yC, cx, yE + hE)          # C -> E
    flecha(ax, cx, yE, cx, yG + hG)          # E -> G
    flecha(ax, cx, yG, cx, yI + hI)          # G -> I
    flecha(ax, XL + WL, yA + hA / 2, XR, yB + hB / 2)   # A -> B
    flecha(ax, XL + WL, yC + hC / 2, XR, yD + hD - 0.025)  # C -> D
    flecha(ax, XL + WL, yE + hE / 2, XR, yF + hF / 2)   # E -> F
    flecha(ax, XL + WL, yG + hG / 2, XR, yH + hH - 0.025)  # G -> H

    ax.text(0.5, 0.035, T["pie"], ha="center", va="center", fontsize=7.2, color=MUT)

    for ext in ("pdf", "svg", "png"):
        fig.savefig(f"{T['archivo']}.{ext}", dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)
    print(f"{T['archivo']}: pdf, svg, png listos")

if __name__ == "__main__":
    dibujar(ES)
    dibujar(EN)
