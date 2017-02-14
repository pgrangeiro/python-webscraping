from services import CSVService


class Product:

    def __init__(self, name, title, url):
        self.name = name
        self.title = title
        self.url = url

    def save(self):
        CSVService.write(self.name, self.title, self.url)
