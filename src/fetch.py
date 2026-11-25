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


if __name__ == "__main__":
    result = fetch_url("https://somalidisablesupport.com/")
    print(result["status"], result["final_url"], result["error"])

    result = fetch_url("https://nuexista-blabla123.com")
    print(result["status"], result["final_url"], result["error"])