def base_url():
    url = "http://165.22.81.75:8090"
    return str(url)


def calculate_method():
    url = "/test/calculate"
    return str(url)


def api_url():
    url = base_url() + calculate_method()
    return str(url)
