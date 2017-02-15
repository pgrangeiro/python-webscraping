from exceptions import BadRequestException, UnexpectedContentToParseException
from .crawl_products_use_case import CrawlProductsUseCase
from .save_product_info_use_case import SaveProductInfoUseCase
from services import Logger


class GetProductsFromSiteUseCase:

    @classmethod
    def execute(self):
        products_ids = []

        try:
            for _id, name, title, url in CrawlProductsUseCase.execute():
                if _id not in products_ids:
                    SaveProductInfoUseCase.execute(name, title, url)
                    products_ids.append(_id)
        except UnexpectedContentToParseException as e:
            Logger.log(e.message)
        except BadRequestException as e:
            Logger.log(e.message)
