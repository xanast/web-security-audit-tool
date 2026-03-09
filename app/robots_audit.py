import requests
from urllib.parse import urljoin

def analyze_robots(base_url: str, timeout: int = 8) -> dict:
    robots_url = urljoin(base_url, "/robots.txt")

    try:
        response = requests.get(robots_url, timeout=timeout)
        if response.status_code != 200:
            return {
                "url": robots_url,
                "exists": False,
                "status_code": response.status_code,
                "notes": ["robots.txt not found"],
            }

        content = response.text
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        disallow_entries = [line for line in lines if line.lower().startswith("disallow:")]
        sitemap_entries = [line for line in lines if line.lower().startswith("sitemap:")]

        return {
            "url": robots_url,
            "exists": True,
            "status_code": response.status_code,
            "disallow_count": len(disallow_entries),
            "sitemap_count": len(sitemap_entries),
            "sample_lines": lines[:15],
            "notes": [
                "robots.txt is advisory for crawlers and not an authorization mechanism"
            ],
        }
    except requests.RequestException as exc:
        return {
            "url": robots_url,
            "exists": False,
            "error": str(exc),
            "notes": ["Request failed"],
        }