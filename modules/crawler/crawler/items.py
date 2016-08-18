# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PAPAnnonce(Item):
    title = Field()
    url = Field()
    type = Field()
    date_published = Field()
    ref = Field()
    rent = Field()
    nb_pieces = Field()
    nb_chambres = Field()
    surface = Field()
    addr_postcode = Field()
    addr_name = Field()
    description = Field()
    email = Field()
    telephone = Field()
