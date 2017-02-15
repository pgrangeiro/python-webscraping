from use_cases import CrawlProductsUseCase, SaveProductInfoUseCase


def run():
    products_ids = []
    for id, name, title, url in CrawlProductsUseCase.execute():
        if id not in products_ids:
            SaveProductInfoUseCase.execute(name, title, url)


if __name__ == '__main__':
    run()
