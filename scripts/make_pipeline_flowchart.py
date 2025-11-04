# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 21:52:30 2025

@author: celso
"""

# scripts/make_pipeline_flowchart.py  (matplotlib puro, 1 figura)
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle

matplotlib.use("Agg")

STAGES = [
    ("01", "Ingestion\n& Catalog"),
    ("02", "Corporate &\nEconomic Data"),
    ("03", "Cleaning &\nGap Handling"),
    ("04", "Outliers &\nQuality Mask"),
    ("05", "Base Features\n& T+1 Lag"),
    ("06", "Train/Valid/Test\nSplit"),
]

def box(ax, x, y, w, h, text):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.045",
        mutation_aspect=1.0, linewidth=1.0, alpha=0.25))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center")

def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=ArrowStyle("Simple", head_length=6, head_width=6),
                                lw=1.0, alpha=0.8))

def main():
    fig = plt.figure(figsize=(12, 2.7))
    ax = fig.add_subplot(111)
    ax.set_axis_off()

    W, H = 0.13, 0.75
    X0, Y0 = 0.06, 0.12
    gap = 0.035

    xs = []
    for i, (_, label) in enumerate(STAGES):
        x = X0 + i * (W + gap)
        xs.append(x)
        box(ax, x, Y0, W, H, label)

    for i in range(len(xs) - 1):
        arrow(ax, xs[i] + W, Y0 + H/2, xs[i+1], Y0 + H/2)

    out = Path("reports/figures/pipeline_01_06.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)
    print(f"[OK] saved: {out}")

if __name__ == "__main__":
    main()
