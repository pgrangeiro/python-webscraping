from domain import Product

class SaveProductInfoUseCase:

    @classmethod
    def execute(cls, name, title, url):
        instance = Product(name, title, url)
        instance.save()
