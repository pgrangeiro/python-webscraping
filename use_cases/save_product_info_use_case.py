class ProductFactory:

    @classmethod
    def create(self, content):
        pass


class SaveProductInfoUseCase:

    @classmethod
    def execute(cls, content):
        instance = ProductFactory.create(content)
        instance.save()
