import scrapy
from ExtractingLaptopData.items import StartechLaptopItem


class StartechSpider(scrapy.Spider):
    """
    Scrapy Spider for Startech Computers Website

    This spider is designed to scrape laptop information from the Startech Computers website.
    It starts from the initial URL and follows links to individual laptop product pages,
    extracting various details such as title, prices, specifications, and reviews.

    Spider Attributes:
    - name (str): The name of the spider.
    - allowed_domains (list): A list of allowed domain names for crawling.
    - start_urls (list): A list of starting URLs for the spider.
    - page_count (int): A counter to limit the number of pages crawled.

    Methods:
    - parse(response): The main parsing method that extracts laptop product URLs and navigates to them.
    - parse_laptop_page(response): Parses the laptop product page and extracts laptop details.

    Author: [Abdul Ahad]
    """
    name = "startech"
    allowed_domains = ["www.startech.com.bd"]
    start_urls = ["https://www.startech.com.bd/laptop-notebook/laptop"]
    page_count = 0

    def parse(self, response):
        laptop_list = response.css('div.p-items-wrap div.p-item-inner')

        for laptop in laptop_list:
            laptop_url = laptop.css(
                'div.p-item-details h4.p-item-name a ::attr(href)').get()
            yield response.follow(laptop_url, callback=self.parse_laptop_page)

        ls = response.css('ul.pagination li')

        if ls[-1].css('a::text').get() == 'NEXT':
            next_page_url = ls[-1].css('a::attr(href)').get()

            if next_page_url is not None and self.page_count < 20:
                self.page_count += 1
                yield response.follow(next_page_url, callback=self.parse)

    def parse_laptop_page(self, response):

        laptop = StartechLaptopItem()

        laptop_title = response.css(
            'div.product-short-info h1.product-name ::text').get()
        reviews = response.css(
            'section.review div.title-n-action h2::text').get()
        regular_price = response.css(
            'div.product-short-info table.product-info-table td.product-regular-price::text').get()
        special_price = response.css(
            'div.product-short-info table.product-info-table td.product-price::text').get()
        brand = response.css(
            'div.product-short-info table.product-info-table td.product-brand::text').get()

        specification_content = response.css(
            'section#specification table.data-table tr')

        block_title_list = []
        block_content_list = []

        for i in specification_content:
            if i.css('td::attr(class)').get() == 'name':
                block_title_list.append(i.css('td.name::text').get())
                block_content_list.append(i.css('td.value::text').get())

        ll = response.css('div.short-description ul li::text')

        model = ''
        for i in range(len(ll)):
            if 'Model:' in ll[i].get():
                model = ll[i].get()
                break

        processor_brand = ''
        processor_model = ''
        generation = ''
        processor_frequency = ''
        display_size = ''
        display_type = ''
        ram = ''
        ram_type = ''
        storage_type = ''
        storage_capacity = ''
        graphics_model = ''
        battery_type = ''
        battery_capacity = ''

        for i in range(len(block_title_list)):

            if 'Processor' in block_title_list[i] and 'Brand' in block_title_list[i]:
                processor_brand = block_content_list[i]

            elif 'Processor' in block_title_list[i] and 'Model' in block_title_list[i]:
                processor_model = block_content_list[i]

            elif 'Generation' in block_title_list[i] and len(block_title_list[i]) < 12:
                generation = block_content_list[i]

            elif 'Processor' in block_title_list[i] and 'Frequency' in block_title_list[i]:
                processor_frequency = block_content_list[i]

            elif 'Display' in block_title_list[i] and 'Size' in block_title_list[i]:
                display_size = block_content_list[i]

            elif 'Display' in block_title_list[i] and 'Type' in block_title_list[i]:
                display_type = block_content_list[i]

            elif 'RAM' in block_title_list[i] and len(block_title_list[i]) < 5:
                ram = block_content_list[i]

            elif 'RAM' in block_title_list[i] and 'Type' in block_title_list[i]:
                ram_type = block_content_list[i]

            elif 'Storage' in block_title_list[i] and 'Type' in block_title_list[i]:
                storage_type = block_content_list[i]

            elif 'Storage' in block_title_list[i] and 'Capacity' in block_title_list[i]:
                storage_capacity = block_content_list[i]

            elif 'Graphics' in block_title_list[i] and 'Model' in block_title_list[i]:
                graphics_model = block_content_list[i]

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
        laptop['processor_generation'] = generation
        laptop['processor_frequency'] = processor_frequency
        laptop['ram'] = ram
        laptop['ram_type'] = ram_type
        laptop['storage_type'] = storage_type
        laptop['storage_capacity'] = storage_capacity
        laptop['graphics_model'] = graphics_model
        laptop['display_size'] = display_size
        laptop['display_type'] = display_type
        laptop['battery_type'] = battery_type
        laptop['battery_capacity'] = battery_capacity
        laptop['reviews'] = reviews

        yield laptop
