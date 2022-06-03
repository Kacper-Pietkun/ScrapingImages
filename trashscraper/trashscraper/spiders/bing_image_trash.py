from fsspec import Callback
import scrapy
from trashscraper.items import TrashscraperItem
from trashscraper.spiders.trash_image_spider import TrashImageSpider
from scrapy_playwright.page import PageMethod
#from pathlib import Path


class BingImageTrashSpider(TrashImageSpider):
    name = 'bing_image_trash'
    allowed_domains = ['bing.com']

    def start_requests(self):
        super().start_requests()

        self.urls = self.urls.split(';')
        for url in self.urls:
            yield scrapy.Request(url, meta=dict(
                url=url,
    	 		playwright=True,
    	 		playwright_include_page=True,
                playwright_context_kwargs=dict(
                    viewport=dict(width=1920, height=10000)
                ),
    	 		playwright_page_methods=[
    	 			PageMethod('wait_for_selector', 'a.richImgLnk'),
                    PageMethod("hover", "div#i_results"),
                    # PageMethod(
                    #     "screenshot", path=Path(__file__).parent / "screen.png", full_page=True
                    # ),
    	 			]
    	 	))


    def parse(self, response):
        item = TrashscraperItem()

        elements = response.css('a.richImgLnk')
        for iter, element in enumerate(elements):
            if iter >= self.size and self.size != 0:
                break
            item['image_urls'] = [element.css('img').attrib["src"]]
            item['category'] = self.category
            yield item
        
        if self.size > len(elements):
            print(f'SPIDER CATEGORY={self.category}, URL={response.meta["url"]} UNABLE TO DOWNLOAD MORE IMAGES: got {len(elements)} out of {self.size}')
 