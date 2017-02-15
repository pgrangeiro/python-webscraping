from .crawl_products_use_case import CrawlProductsUseCase
from .save_product_info_use_case import SaveProductInfoUseCase


class GetProductsFromSiteUseCase:

    @classmethod
    def execute(self):
        products_ids = []
        for _id, name, title, url in CrawlProductsUseCase.execute():
            if _id not in products_ids:
                SaveProductInfoUseCase.execute(name, title, url)
                products_ids.append(_id)
