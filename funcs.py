import urls


def parse_response(request):
    """parses http request, returns http method and http code status"""
    parsed = request.split()
    return parsed[0], parsed[1]


def make_header(method, url):
    """makes a header for the response to the client"""
    result = "HTTP/1.1 200 OK\n\n", 200
    if method != "GET":
        result = "HTTP/1.1 405 Method not allowed\n\n", 405
    if url not in urls.urls:
        result = "HTTP/1.1 404 Not Found\n\n", 404

    return result


def make_content(code, url):
    """generates content for the response to the client"""
    if code == 404:
        return "<h1>404</h1><p>Not Found</p>"
    elif code == 405:
        return "<h1>405</h1><p>Method not allowed</p>"
    else:
        result = urls.urls[url]()

    return result


def make_response(request):
    """generates header and content for the response to the client
    and encodes that"""
    method, url = parse_response(request)
    header, code = make_header(method, url)
    body = make_content(code, url)
    return (header + body).encode()
