from crawlers import BrandInfoWebCrawler, BrandsWebCrawler, ProductInfoWebCrawler, ProductsWebCrawler

from exceptions import UnexpectedContentToParseException


class CrawlProductsUseCase:

    @classmethod
    def execute(cls):
        brands_crawler = BrandsWebCrawler()
        for brand in brands_crawler.execute():
            brand_info_crawler = BrandInfoWebCrawler(brand['url'])
            brand_info = brand_info_crawler.execute()
            products_crawler = ProductsWebCrawler(brand_info['id'])
            for product in products_crawler.execute():
                products_info_crawler = ProductInfoWebCrawler(product['url'])
                try:
                    product_info = products_info_crawler.execute()
                    yield (
                        product_info['name'],
                        product_info['title'],
                        product['url'],
                    )
                except UnexpectedContentToParseException:
                    print('Product Info Not Found - %s ' % product['url'])
