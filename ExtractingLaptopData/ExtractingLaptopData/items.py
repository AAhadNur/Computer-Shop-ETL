# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExtractinglaptopdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LaptopItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
    processor_model = scrapy.Field()
    processor_base_frequency = scrapy.Field()
    ram = scrapy.Field()
    ram_type = scrapy.Field()
    storage = scrapy.Field()
    graphics_chipset = scrapy.Field()
    battery = scrapy.Field()
    reviews = scrapy.Field()
