from urllib.parse import urlparse

def normalize_url(url: str) -> str:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return url

def get_hostname(url: str) -> str:
    return urlparse(url).netloc