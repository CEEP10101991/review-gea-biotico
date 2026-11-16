"""Figura conceptual (esquema, datos ilustrativos).
A) Lógica de un análisis de asociación genotipo-ambiente (GEA): para cada locus,
   frecuencia = media + beta * predictor + estructura + error; se prueba beta = 0.
B) Asociación real con atribución equivocada (ejemplo de Rellstab et al. 2015, p. 4363).
Uso: python3 figura_gea_v3.py [directorio_de_salida]
"""
import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyBboxPatch, FancyArrowPatch

OUT = sys.argv[1] if len(sys.argv) > 1 else "."

TEAL, TEAL_D, TEAL_F = "#1D9E75", "#085041", "#E1F5EE"
GRIS_F, GRIS_B, GRIS_T, GRIS_M = "#F1EFE8", "#5F5E5A", "#2C2C2A", "#B4B2A9"
CORAL_F, CORAL_B, CORAL_T = "#FAECE7", "#993C1D", "#4A1B0C"
MOR_F, MOR_B, MOR_T = "#EEEDFE", "#534AB7", "#26215C"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5,
                     "svg.fonttype": "none", "pdf.fonttype": 42})
fig = plt.figure(figsize=(7.2, 8.6))


def flecha(x0, y0, x1, y1):
    fig.patches.append(FancyArrowPatch((x0, y0), (x1, y1), transform=fig.transFigure,
                                       arrowstyle="-|>", mutation_scale=10, lw=0.9,
                                       color=GRIS_B))


# ---------- Panel A ----------
fig.text(0.04, 0.965, "A", fontsize=13, fontweight="bold", va="center")
fig.text(0.075, 0.965, "Cómo funciona un GEA", fontsize=10.5, va="center", color=GRIS_T)

axl = fig.add_axes([0.08, 0.775, 0.84, 0.165])
axl.set_xlim(0, 6)
axl.set_ylim(0, 1.18)
axl.set_aspect("equal", adjustable="box")
axl.axis("off")
for i, f in enumerate([0.10, 0.25, 0.40, 0.60, 0.75, 0.90]):
    cx, cy, r = 0.5 + i, 0.62, 0.27
    axl.add_patch(Circle((cx, cy), r, fc="#E4E2DA", ec=GRIS_B, lw=0.7))
    axl.add_patch(Wedge((cx, cy), r, 90 - 360 * f, 90, fc=TEAL, ec="none"))
    axl.add_patch(Circle((cx, cy), r, fc="none", ec=GRIS_B, lw=0.7))
axl.annotate("", xy=(5.85, 0.2), xytext=(0.15, 0.2),
             arrowprops=dict(arrowstyle="-|>", lw=0.9, color=GRIS_B))
axl.text(0.15, 0.05, "Bajo", ha="left", va="center", color=GRIS_B)
axl.text(5.85, 0.05, "Alto", ha="right", va="center", color=GRIS_B)
axl.text(3.0, 0.05, "3. Valor del predictor en cada sitio", ha="center", va="center",
         fontweight="bold", color=GRIS_T)
axl.text(0.15, 1.08, "1. Muestreo de poblaciones", ha="left", va="center",
         fontweight="bold", color=GRIS_T)
axl.add_patch(plt.Rectangle((3.02, 1.03), 0.12, 0.1, fc=TEAL, ec="none"))
axl.text(3.2, 1.08, "2. Frecuencia de un alelo en cada sitio", ha="left", va="center",
         fontweight="bold", color=GRIS_T)

axt = fig.add_axes([0.24, 0.655, 0.52, 0.075])
axt.axis("off")
axt.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0,rounding_size=0.018",
                             fc=MOR_F, ec=MOR_B, lw=0.8, transform=axt.transAxes,
                             clip_on=False))
axt.text(0.5, 0.66, "4. Prueba de asociación, locus por locus", ha="center", va="center",
         fontweight="bold", color=MOR_T, transform=axt.transAxes)
axt.text(0.5, 0.28, "Descuenta la estructura poblacional", ha="center", va="center",
         color=MOR_B, transform=axt.transAxes)

flecha(0.5, 0.775, 0.5, 0.735)
flecha(0.36, 0.652, 0.23, 0.614)
flecha(0.50, 0.652, 0.53, 0.614)
flecha(0.64, 0.652, 0.84, 0.614)

xs = [0.08, 0.24, 0.40, 0.57, 0.74, 0.92]


def ejes(ax, xlabel, ylabel, titulo):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color(GRIS_B)
        ax.spines[s].set_linewidth(0.8)
    ax.set_xlabel(xlabel, color=GRIS_B, labelpad=3)
    ax.set_ylabel(ylabel, color=GRIS_B, labelpad=3, fontsize=7.5, linespacing=1.15)
    ax.set_title(titulo, fontsize=8.5, fontweight="bold", color=GRIS_T, pad=5)


def mini(pos, ys, titulo, color, borde, nota):
    ax = fig.add_axes(pos)
    ax.scatter(xs, ys, s=20, color=color, edgecolor=borde, linewidth=0.6, zorder=3)
    b, a = np.polyfit(xs, ys, 1)
    ax.plot([0.04, 0.96], [a + b * 0.04, a + b * 0.96], color=borde, lw=1.2, zorder=2)
    ejes(ax, "Predictor", "Frecuencia del alelo\n(ajustada por estructura)", titulo)
    ax.text(0.05, 0.93, nota, ha="left", va="center", fontsize=7.5, color=borde,
            transform=ax.transAxes)


mini([0.125, 0.425, 0.20, 0.165], [0.10, 0.24, 0.33, 0.52, 0.62, 0.76],
     "Un locus asociado", TEAL, TEAL_D, "pendiente ≠ 0")
mini([0.435, 0.425, 0.20, 0.165], [0.42, 0.34, 0.47, 0.36, 0.45, 0.39],
     "Un locus sin asociación", GRIS_M, GRIS_B, "pendiente ≈ 0")

axm = fig.add_axes([0.745, 0.425, 0.20, 0.165])
rng = np.random.RandomState(7)
xg = np.linspace(0.04, 0.96, 70)
yg = np.clip(rng.gamma(2.0, 0.085, 70), 0.02, 0.5)
cand = [14, 15, 47]
yg[cand] = [0.80, 0.90, 0.74]
col = [TEAL if i in cand else GRIS_M for i in range(70)]
axm.scatter(xg, yg, s=7, color=col, edgecolor="none", zorder=3)
axm.axhline(0.62, color=GRIS_B, lw=0.8, linestyle=(0, (3, 2)))
axm.text(0.97, 0.655, "umbral", ha="right", va="center", fontsize=7.5, color=GRIS_B)
ejes(axm, "Loci a lo largo del genoma", "Evidencia de asociación", "5. Todos los loci")
axm.text(0.47, 0.90, "candidatos", ha="left", va="center", fontsize=7.5, color=TEAL_D)

# ---------- Panel B ----------
fig.text(0.04, 0.345, "B", fontsize=13, fontweight="bold", va="center")
fig.text(0.075, 0.345, "Una asociación real, atribuida al factor equivocado",
         fontsize=10.5, va="center", color=GRIS_T)

axb = fig.add_axes([0.06, 0.025, 0.88, 0.2895])
axb.set_xlim(0, 100)
axb.set_ylim(0, 39.3)
axb.set_aspect("equal", adjustable="box")
axb.axis("off")


def rbox(x, y, w, h, fc, ec):
    axb.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                                 fc=fc, ec=ec, lw=0.8))


def arr(x0, y0, x1, y1, color=GRIS_B, **kw):
    axb.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=10,
                                  lw=1.1, color=color, **kw))


yc = 19.5
rbox(4, yc - 4, 20, 8, GRIS_F, GRIS_B)
axb.text(14, yc, "Temperatura", ha="center", va="center", fontweight="bold", color=GRIS_T)
axb.text(14, yc - 6.2, "Ambiente abiótico", ha="center", va="center", color=GRIS_B)
rbox(40, yc - 4, 20, 8, CORAL_F, CORAL_B)
axb.text(50, yc, "Patógeno", ha="center", va="center", fontweight="bold", color=CORAL_T)
axb.text(50, yc - 6.2, "Otra especie", ha="center", va="center", color=CORAL_B)
rbox(76, yc - 4, 20, 8, TEAL_F, TEAL_D)
axb.text(86, yc, "Alelo de defensa", ha="center", va="center", fontweight="bold", color=TEAL_D)
axb.text(86, yc - 6.2, "Especie focal", ha="center", va="center", color=TEAL_D)

arr(24.6, yc, 39.4, yc)
axb.text(32, yc + 1.9, "condiciona", ha="center", va="center", fontsize=7.5, color=GRIS_B)
arr(60.6, yc, 75.4, yc, CORAL_B)
axb.text(68, yc + 1.9, "selecciona", ha="center", va="center", fontsize=7.5, color=CORAL_B)

arr(14, yc + 4.4, 86, yc + 4.4, MOR_B, connectionstyle="arc3,rad=-0.3",
    linestyle=(0, (4, 3)))
axb.text(50, 36.6, "Asociación que detecta un GEA con clima", ha="center", va="center",
         fontweight="bold", color=MOR_T)

axb.text(50, 7.2, "El locus sí participa en la adaptación; lo falso es atribuirla al clima.",
         ha="center", va="center", fontweight="bold", color=GRIS_T)
axb.text(50, 3.8, "Solo si se mide el predictor biótico puede ponerse a prueba la otra explicación.",
         ha="center", va="center", color=GRIS_B)

os.makedirs(OUT, exist_ok=True)
for ext in ("png", "svg", "pdf"):
    fig.savefig(os.path.join(OUT, f"Figura_conceptual_GEA_v3.{ext}"), dpi=300,
                facecolor="white")
print("ok")
