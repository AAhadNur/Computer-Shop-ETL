import scrapy
from ExtractingLaptopData.items import RyansLaptopItem


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
        laptop = RyansLaptopItem()

        laptop_title = response.css('div.product_content h1::text').get()
        number_of_reviews = response.css(
            'div.rating span.review-text a::text').get()
        regular_price = response.css(
            'div.details-all-block span.rp-block ::text').get()
        special_price = response.css(
            'div.details-all-block span.sp-block ::text').get()
        
        specification_content = response.css('div.justify-content-center div.table-hr-remove')

        block_title_list = []
        block_content_list = []
        #response.css('div.justify-content-center span.att-value::text')

        for i in specification_content:
            if i.css('span::attr(class)').get() == 'att-title context':
                block_title_list.append(i.css('span.att-title::text').get())
                block_content_list.append(i.css('span.att-value::text').get())

        brand = ''
        model = ''
        processor_brand = ''
        processor_model = ''
        processor_base_frequency = ''
        processor_core = ''
        ram = ''
        ram_type = ''
        storage = ''
        display_size = ''
        display_type = ''
        graphics_chipset = ''
        battery = ''
        battery_capacity = ''
        battery_type = ''
        
        for i in range(len(block_title_list)):
            if 'Brand' in block_title_list[i] and len(block_title_list[i]) < 7:
                brand = block_content_list[i]
            elif 'Model' in block_title_list[i] and len(block_title_list[i]) < 7:
                model = block_content_list[i]
            elif 'Processor' in block_title_list[i] and 'Brand' in block_title_list[i]:
                processor_brand = block_content_list[i]
            elif 'Processor' in block_title_list[i] and 'Model' in block_title_list[i]:
                processor_model = block_content_list[i]
            elif 'Processor' in block_title_list[i] and 'Frequency' in block_title_list[i]:
                processor_base_frequency = block_content_list[i]
            elif 'Processor' in block_title_list[i] and 'Core' in block_title_list[i]:
                processor_core = block_content_list[i]
            elif 'RAM' in block_title_list[i] and len(block_title_list[i]) < 5:
                ram = block_content_list[i]
            elif 'RAM' in block_title_list[i] and 'Type' in block_title_list[i]:
                ram_type = block_content_list[i]
            elif 'Storage' in block_title_list[i] and len(block_title_list[i]) < 9:
                storage = block_content_list[i]
            elif 'Display' in block_title_list[i] and 'Size' in block_title_list[i]:
                display_size = block_content_list[i]
            elif 'Display' in block_title_list[i] and 'Type' in block_title_list[i]:
                display_type = block_content_list[i]
            elif 'Graphics' in block_title_list[i] and 'Chipset' in block_title_list[i]:
                graphics_chipset = block_content_list[i]
            elif 'Battery' in block_title_list[i] and len(block_title_list[i]) < 9:
                battery = block_content_list[i]
            elif 'Battery' in block_title_list[i] and 'Type' in block_title_list[i]:
                battery_type = block_content_list[i]
            elif 'Battery' in block_title_list[i] and 'Capacity' in block_title_list[i]:
                battery_capacity = block_content_list[i]

        laptop['title'] = laptop_title
        laptop['brand'] = brand
        laptop['model'] = model
        laptop['regular_price'] = regular_price
        laptop['special_price'] = special_price
        laptop['processor_brand'] = processor_brand
        laptop['processor_model'] = processor_model
        laptop['processor_base_frequency'] = processor_base_frequency
        laptop['processor_core'] = processor_core
        laptop['ram'] = ram
        laptop['ram_type'] = ram_type
        laptop['storage'] = storage
        laptop['display_size'] = display_size
        laptop['display_type'] = display_type
        laptop['graphics_chipset'] = graphics_chipset
        laptop['battery'] = battery
        laptop['battery_capacity'] = battery_capacity
        laptop['battery_type'] = battery_type
        laptop['reviews'] = number_of_reviews

        yield laptop
