@property
def base_url():
    url = "http://165.22.81.75:8090"
    return url


@property
def calculate_method():
    url = "/test/calculate"
    return url


@property
def api_url():
    url = base_url + calculate_method
    return url
