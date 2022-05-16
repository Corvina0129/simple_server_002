def index():
    with open("pages/index.html") as page:
        return page.read()


def news():
    with open("pages/news.html") as page:
        return page.read()
