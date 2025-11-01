from pathlib import Path
import shutil

ALLOW_EXT = {".csv", ".parquet", ".png", ".svg", ".json"}

SRC = Path("private/data_processed")
DST_FIG = Path("reports/figures")
DST_TAB = Path("reports/tables")

DST_FIG.mkdir(parents=True, exist_ok=True)
DST_TAB.mkdir(parents=True, exist_ok=True)

for p in SRC.rglob("*"):
    if p.suffix.lower() in ALLOW_EXT:
        target = DST_FIG if p.suffix.lower() in {".png", ".svg"} else DST_TAB
        shutil.copy2(p, target / p.name)
