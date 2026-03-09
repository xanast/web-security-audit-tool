import json
from pathlib import Path

def save_json_report(data: dict, output_path: str = "report.json") -> str:
    path = Path(output_path)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return str(path.resolve())