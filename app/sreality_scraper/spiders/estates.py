import scrapy
import json
from sreality_scraper.items import SrealityScraperItem


class EstatesSpider(scrapy.Spider):
    # define spider name and target URL
    name = 'estates'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500']

    def parse(self, response):
        data = json.loads(response.body)
        estateItem = SrealityScraperItem()
        # parse scraped data into items in order to be later processed by pipelines.py
        for estate in data['_embedded']['estates']:
            estateItem['title'] = estate['name']
            estateItem['url'] = estate['_links']['images'][0]['href']
            yield estateItem

