from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def save_html_report(data: dict, output_path: str = "report.html") -> str:
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html", "xml"])
    )
    template = env.get_template("report.html.j2")
    rendered = template.render(report=data)

    path = Path(output_path)
    path.write_text(rendered, encoding="utf-8")
    return str(path.resolve())