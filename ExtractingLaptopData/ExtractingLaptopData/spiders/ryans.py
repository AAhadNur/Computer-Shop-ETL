import scrapy
from ExtractingLaptopData.items import LaptopItem


class RyansSpider(scrapy.Spider):
    name = "ryans"
    allowed_domains = ["www.ryanscomputers.com"]
    start_urls = [
        "https://www.ryanscomputers.com/category/laptop-all-laptop?page=1"]

    def parse(self, response):
        laptop_list = response.css('div.category-single-product')

        for laptop in laptop_list:
            laptop_url = laptop.css('div.image-box a ::attr(href)').get()
            yield response.follow(laptop_url, callback=self.parse_laptop_page)

        next_page_url = response.css('[rel="next"] ::attr(href)').get()

        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_laptop_page(self, response):
        laptop = LaptopItem()

        laptop_title = response.css('div.product_content h1::text').get()
        number_of_reviews = response.css(
            'div.rating span.review-text a::text').get()
        price = response.css(
            'div.details-all-block span.sp-block ::text').get()

        block_title_list = response.css(
            'div.justify-content-center span.att-title::text')
        block_content_list = response.css(
            'div.justify-content-center span.att-value::text')

        brand = ''
        model = ''
        processor_model = ''
        processor_base_frequency = ''
        ram = ''
        ram_type = ''
        storage = ''
        graphics_chipset = ''
        battery = ''

        for i in range(len(block_title_list)):
            if block_title_list[i].get() == 'Brand':
                brand = block_content_list[i].get()
            elif block_title_list[i].get() == 'Model':
                model = block_content_list[i].get()
            elif block_title_list[i].get() == 'Processor Model':
                processor_model = block_content_list[i].get()
            elif block_title_list[i].get() == 'Processor Base Frequency':
                processor_base_frequency = block_content_list[i].get()
            elif block_title_list[i].get() == 'RAM':
                ram = block_content_list[i].get()
            elif block_title_list[i].get() == 'RAM Type':
                ram_type = block_content_list[i].get()
            elif block_title_list[i].get() == 'Storage':
                storage = block_content_list[i].get()
            elif block_title_list[i].get() == 'Graphics Chipset':
                graphics_chipset = block_content_list[i].get()
            elif block_title_list[i].get() == 'Battery':
                battery = block_content_list[i].get()

        laptop['title'] = laptop_title
        laptop['brand'] = brand
        laptop['model'] = model
        laptop['price'] = price
        laptop['processor_model'] = processor_model
        laptop['processor_base_frequency'] = processor_base_frequency
        laptop['ram'] = ram
        laptop['ram_type'] = ram_type
        laptop['storage'] = storage
        laptop['graphics_chipset'] = graphics_chipset
        laptop['battery'] = battery
        laptop['reviews'] = number_of_reviews

        yield laptop
