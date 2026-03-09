import requests
from app.utils import normalize_url
from app.headers_audit import audit_headers
from app.robots_audit import analyze_robots
from app.fingerprint import passive_fingerprint
from app.tls_checks import check_tls
from app.scoring import calculate_score
from app.report_json import save_json_report
from app.report_html import save_html_report

def run_scan(target: str) -> dict:
    url = normalize_url(target)

    response = requests.get(url, timeout=10, headers={
        "User-Agent": "WebSecurityAuditTool/1.0"
    })

    headers_result = audit_headers(dict(response.headers))
    robots_result = analyze_robots(url)
    fingerprint_result = passive_fingerprint(dict(response.headers), response.text)
    tls_result = check_tls(url)

    summary = calculate_score(
        headers_score=headers_result["score"],
        robots_result=robots_result,
        tls_result=tls_result,
        fingerprint_result=fingerprint_result,
    )

    report = {
        "target": url,
        "summary": summary,
        "headers": headers_result,
        "robots": robots_result,
        "fingerprint": fingerprint_result,
        "tls": tls_result,
    }

    json_path = save_json_report(report, "report.json")
    html_path = save_html_report(report, "report.html")

    return {
        "report": report,
        "json_report_path": json_path,
        "html_report_path": html_path,
    }