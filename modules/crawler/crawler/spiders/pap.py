from scrapy.spiders import Spider
from scrapy.selector import Selector


class PAPSpider(Spider):
    name = "pap"
    allowed_domains = ["pap.fr"]
    start_urls = [
        "http://www.pap.fr/annonce/locations-maison",
        "http://www.pap.fr/annonce/locations-appartement"
    ]

    def parse(self, response):
        # parse and extract data from response here
        print("url" + response.url)

