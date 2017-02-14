from use_cases import CrawlProductsUseCase, SaveProductInfoUseCase


def run():
    for args in CrawlProductsUseCase.execute():
        SaveProductInfoUseCase.execute(*args)



if __name__ == '__main__':
    run()
