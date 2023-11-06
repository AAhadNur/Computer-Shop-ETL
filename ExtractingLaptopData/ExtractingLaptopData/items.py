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
    """
    Scrapy Item for Ryans Laptop Data

    This class defines the structure of Scrapy items used to extract data from Ryans laptops.
    Each field represents a piece of information scraped from the website.

    Fields:
    - title (str): The laptop's title.
    - brand (str): The laptop's brand.
    - model (str): The laptop's model.
    - regular_price (str): The regular price of the laptop.
    - special_price (str): The special (discounted) price of the laptop.
    - processor_brand (str): The brand of the laptop's processor.
    - processor_model (str): The model of the laptop's processor.
    - processor_base_frequency (str): The base frequency of the processor.
    - processor_core (str): The number of processor cores.
    - ram (str): The amount of RAM.
    - ram_type (str): The type of RAM.
    - storage (str): The type and capacity of storage.
    - display_size (str): The laptop's display size.
    - display_type (str): The type of display.
    - graphics_chipset (str): The chipset of the graphics.
    - battery (str): The laptop's battery information.
    - battery_capacity (str): The capacity of the laptop's battery.
    - battery_type (str): The type of the laptop's battery.
    - reviews (str): Reviews and ratings for the laptop.
    """

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
    """
    Scrapy Item for Startech Laptop Data

    This class defines the structure of Scrapy items used to extract data from Startech laptops.
    Each field represents a piece of information scraped from the website.

    Fields:
    - title (str): The laptop's title.
    - brand (str): The laptop's brand.
    - model (str): The laptop's model.
    - regular_price (str): The regular price of the laptop.
    - special_price (str): The special (discounted) price of the laptop.
    - processor_brand (str): The brand of the laptop's processor.
    - processor_model (str): The model of the laptop's processor.
    - processor_generation (str): The generation of the processor.
    - processor_frequency (str): The processor's frequency.
    - ram (str): The amount of RAM.
    - ram_type (str): The type of RAM.
    - storage_type (str): The type of storage (e.g., SSD, HDD).
    - storage_capacity (str): The capacity of the storage.
    - graphics_model (str): The model of the graphics.
    - display_size (str): The laptop's display size.
    - display_type (str): The type of display.
    - battery_type (str): The type of the laptop's battery.
    - battery_capacity (str): The capacity of the laptop's battery.
    - reviews (str): Reviews and ratings for the laptop.
    """
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
