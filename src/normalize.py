from urllib.parse import urlparse

def normalize_domain(domain):
    domain = domain.strip().lower()

    if not domain:
        return None

    if "://" not in domain:
        domain = "http://" + domain
    
    parsed_domain = urlparse(domain)
    hostname = parsed_domain.hostname
    if hostname is None:
        return None
    hostname = hostname.removeprefix("www.")

    return hostname

if __name__ == "__main__":
    assert normalize_domain("") is None
    assert normalize_domain("HTTPS://WWW.Example.com/") == "example.com"
    assert normalize_domain("example.com") == "example.com"
    assert normalize_domain("  example.com  ") == "example.com"
    assert normalize_domain("http://example.com/path?x=1") == "example.com"
    assert normalize_domain("example.com:8080") == "example.com"
    assert normalize_domain("awwww.com") == "awwww.com"
    print("All tests passed")