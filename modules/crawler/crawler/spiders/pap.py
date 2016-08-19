# coding=utf-8
from scrapy.spiders import Spider
from scrapy.selector import Selector

# from modules.crawler.crawler.items import PAPAnnonce


class PAPSpider(Spider):
    name = "pap"
    allowed_domains = ["pap.fr"]
    start_urls = [
        "http://www.pap.fr/annonce/locations-appartement-40-annonces-par-page"
    ]

    def parse(self, response):
        # parse and extract data from response here
        annonces = response.xpath("//div[@class='box search-results-item annonce']")
        for annonce in annonces:
            # item = PAPAnnonce()
            title = annonce.xpath("div[1]/a/span[1]/text()").extract()[0]
            price = annonce.xpath("div[1]/a/span[2]/strong/text()").extract()[0]
            ref_date = annonce.xpath("div[1]/p/text()").extract_first()
            index = 0
            for i in range(len(ref_date)):
                if ref_date[i] == '/':
                    index = i
            date_published = ref_date[index+1:]
            reference = ref_date[:index]
            url = annonce.xpath("div[1]/a/@href").extract()[0]
            id = annonce.xpath("div[1]/a/@name").extract()[0]
            nb_pieces = annonce.xpath("div[2]//ul[@class='item-summary float-left']//li[text()='Piece']").extract()[0]
            nb_chambres = annonce.xpath("div[2]//ul[@class='item-summary float-left']//li[text()='Chambre']").extract()[0]
            surface = annonce.xpath("div[2]//ul[@class='item-summary float-left']//li[text()='Surface']").extract()[0]
            print("%s *** %s *** %s *** %s *** %s *** %s *** %s *** %s *** %s" % (title, date_published, reference, price, url, id, nb_pieces, nb_chambres, surface))

