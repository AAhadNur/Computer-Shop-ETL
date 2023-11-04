# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExtractinglaptopdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RyansLaptopItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    regular_price = scrapy.Field()
    special_price = scrapy.Field()
    processor_brand = scrapy.Field()
    processor_model = scrapy.Field()
    processor_base_frequency = scrapy.Field()
    processor_core = scrapy.Field()
    ram = scrapy.Field()
    ram_type = scrapy.Field()
    storage = scrapy.Field()
    display_size = scrapy.Field()
    display_type = scrapy.Field()
    graphics_chipset = scrapy.Field()
    battery = scrapy.Field()
    battery_capacity = scrapy.Field()
    battery_type = scrapy.Field()
    reviews = scrapy.Field()


class StartechLaptopItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    regular_price = scrapy.Field()
    special_price = scrapy.Field()
    processor_brand = scrapy.Field()
    processor_model = scrapy.Field()
    processor_generation = scrapy.Field()
    processor_frequency = scrapy.Field()
    ram = scrapy.Field()
    ram_type = scrapy.Field()
    storage_type = scrapy.Field()
    storage_capacity = scrapy.Field()
    graphics_model = scrapy.Field()
    display_size = scrapy.Field()
    display_type = scrapy.Field()
    battery_type = scrapy.Field()
    battery_capacity = scrapy.Field()
    reviews = scrapy.Field()