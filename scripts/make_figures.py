#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera figuras placeholder para os slides: heatmap, split e flowchart.
Saída: docs/presentation/figures/*.svg
"""
from pathlib import Path
from datetime import date
import math

FIG_DIR = Path("docs/presentation/figures")

def _write(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
    print(f"[OK] gravado: {p}")

def _wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<style>
text{{font-family:-apple-system,Segoe UI,Roboto,Inter,Arial;fill:#0f172a}}
.sub{{fill:#4b5563;font-size:12px}}
.small{{fill:#6b7280;font-size:11px}}
</style>
{body}
</svg>'''

def heatmap_svg(title="Heatmap de Retornos (placeholder)", n=10, w=1280, h=720):
    m = 60
    cw = (w - 2*m)/n
    ch = (h - 2*m)/n
    rects=[]
    for i in range(n):
        for j in range(n):
            v = (math.sin(i*1.7)+math.cos(j*1.3)+2)/4  # 0..1
            r = int(240*v + 15); b = int(240*(1-v) + 15); g = 40
            x = m + j*cw; y = m + i*ch
            rects.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{ch:.1f}" fill="rgb({r},{g},{b})"/>')
    hdr = f'<text x="{m}" y="30" font-size="22" font-weight="700">{title}</text>'
    sub = f'<text class="small" x="{m}" y="{h-12}">Gerado em {date.today().isoformat()} — troque por figura real quando disponível</text>'
    return _wrap(w, h, hdr + "".join(rects) + sub)

def split_svg(title="Split por buckets (placeholder)", w=1280, h=720):
    m = 60; bars = 10
    bw = (w - 2*m)/bars
    body = f'<text x="{m}" y="30" font-size="22" font-weight="700">{title}</text>'
    for i in range(bars):
        v = math.sin(i*0.6)+0.2*math.cos(i*1.3)
        hgt = (h-2*m)*abs(v)/2
        x = m + i*bw
        if v >= 0:
            y = h/2 - hgt
            body += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw*0.7:.1f}" height="{hgt:.1f}" fill="#16a34a"/>'
        else:
            y = h/2
            body += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw*0.7:.1f}" height="{hgt:.1f}" transform="scale(1,-1) translate(0,-{2*y})" fill="#dc2626"/>'
    body += f'<line x1="{m-10}" y1="{h/2}" x2="{w-m+10}" y2="{h/2}" stroke="#9ca3af" stroke-width="1"/>'
    body += f'<text class="sub" x="{w-m-260}" y="{h-12}">Verde=Long  •  Vermelho=Short (exemplo)</text>'
    return _wrap(w, h, body)

def flowchart_svg(title="Pipeline (07→11) — placeholder", w=1280, h=720):
    m=40; bw=220; bh=66; gap=40
    x=m; y=h/2-bh/2
    labels=[("07  Métricas & Risco","vol • VaR • CVaR"),
            ("08  Estratégias","IDX_TARGET • LS_DN • LS_RN"),
            ("09  Taxas","adm • perf • IOF/IR"),
            ("10  Gráficos","heatmap • split"),
            ("11  Produção","cron • GH Actions")]
    body=f'<text x="{m}" y="30" font-size="22" font-weight="700">{title}</text>'
    for i,(t,sub) in enumerate(labels):
        body+=f'<rect x="{x}" y="{y}" rx="12" ry="12" width="{bw}" height="{bh}" fill="#0ea5e9" opacity="0.12" stroke="#0ea5e9"/>'
        body+=f'<text x="{x+12}" y="{y+28}" font-size="16" font-weight="700">{t}</text>'
        body+=f'<text class="sub" x="{x+12}" y="{y+48}">{sub}</text>'
        if i < len(labels)-1:
            x2 = x + bw + gap; mid = y+bh/2
            body+=f'<line x1="{x+bw}" y1="{mid}" x2="{x2-16}" y2="{mid}" stroke="#0ea5e9" stroke-width="2"/>'
            body+=f'<polygon points="{x2-16},{mid-6} {x2-16},{mid+6} {x2-4},{mid}" fill="#0ea5e9"/>'
        x += bw + gap
    body+=f'<text class="small" x="{m}" y="{h-12}">Trocar por diagrama real quando oportuno</text>'
    return _wrap(w, h, body)

def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    _write(FIG_DIR/"fig-heatmap.svg", heatmap_svg())
    _write(FIG_DIR/"fig-estrategias-split.svg", split_svg())
    _write(FIG_DIR/"fig-flowchart.svg", flowchart_svg())

if __name__ == "__main__":
    main()
