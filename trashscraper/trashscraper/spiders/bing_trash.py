from fsspec import Callback
import scrapy
from trashscraper.items import TrashscraperItem
from trashscraper.spiders.trash_spider import TrashSpider


class BingTrashSpider(TrashSpider):
    name = 'bing_trash'
    allowed_domains = ['bing.com']

    def start_requests(self):
        super().start_requests()

        urls = [f'https://www.bing.com/images/search?q={self.keyword}&form=QBLH&sp=-1&pq=ca&sc=9-2&qs=n&cvid=2E700DF5E2BF4644929C9EEA1D7C3604&first=1&tsc=ImageBasicHover']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        item = TrashscraperItem()
        
        images = response.css('img.mimg')
        for iter, image in enumerate(images):
            if iter >= self.size:
                break
            item['image_urls'] = [image.attrib["src"]]
            item['category'] = self.category
            yield item

        if self.size > len(images):
            print(f'SPIDER CATEGORY={self.category}, KEYWORD={self.keyword} UNABLE TO DOWNLOAD MORE IMAGES: got {len(images)} out of {self.size}')