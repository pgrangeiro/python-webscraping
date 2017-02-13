from factories import ProductFactory


class SaveProductInfoUseCase:

    @classmethod
    def execute(cls, content):
        instance = ProductFactory.create(content)
        instance.save()
