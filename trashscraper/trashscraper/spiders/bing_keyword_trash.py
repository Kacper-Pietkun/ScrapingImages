import scrapy
from trashscraper.items import TrashscraperItem
from trashscraper.spiders.trash_keyword_spider import TrashKeywordSpider


class BingKeywordTrashSpider(TrashKeywordSpider):
    name = 'bing_keyword_trash'
    allowed_domains = ['bing.com']

    def start_requests(self):
        super().start_requests()

        keywords_list = self.keywords.split(';')
        urls = [f'https://www.bing.com/images/search?q={keyword}&form=QBLH&sp=-1&pq=ca&sc=9-2&qs=n&cvid=2E700DF5E2BF4644929C9EEA1D7C3604&first=1&tsc=ImageBasicHover' for keyword in keywords_list]
        for keyword, url in zip(keywords_list, urls):
            yield scrapy.Request(url, meta={'keyword': keyword})

    def parse(self, response):
        item = TrashscraperItem()
        
        images = response.css('img.mimg')
        for iter, image in enumerate(images):
            if iter >= self.size and self.size != 0:
                break
            item['image_urls'] = [image.attrib["src"]]
            item['category'] = self.category
            yield item

        if self.size > len(images) and self.size != 0:
            print(f'SPIDER CATEGORY={self.category}, KEYWORD={response.meta["keyword"]} UNABLE TO DOWNLOAD MORE IMAGES: got {len(images)} out of {self.size}')