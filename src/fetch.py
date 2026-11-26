import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
}

def fetch_url(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        return {
            "url": url,
            "final_url": response.url,
            "status": response.status_code,
            "headers": dict(response.headers),
            "html": response.text,
            "error": None,
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "final_url": None,
            "status": None,
            "headers": None,
            "html": None,
            "error": str(e),
        }

def fetch_domain(domain):
    prefixes = ["https://", "https://www.", "http://"]
    result = None

    for prefix in prefixes:
        url = prefix + domain
        print(url)
        result = fetch_url(url)
        if result["error"] is None:
            return result
    return result


if __name__ == "__main__":
    for domain in ["somalidisablesupport.com", "disneystore.com",
                   "joseph-herber.business.site", "nuexista-blabla123.com", "jcmobilecigars.com"]:
        result = fetch_domain(domain)
        print(
            domain, 
            "->", 
            result["status"], 
            result["final_url"], 
            len(result["html"]) if result["html"] is not None else 0,
            result["error"])
        print()