import scrapy
from trashscraper.items import TrashscraperItem
from trashscraper.spiders.trash_spider import TrashSpider


class UnsplashTrashSpider(TrashSpider):
    name = 'unsplash_trash'
    allowed_domains = ['unsplash.com']

    def start_requests(self):
        super().start_requests()

        urls = [f'https://unsplash.com/napi/search/photos?query={self.keyword}&per_page={self.size}&page=1&xp=']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        item = TrashscraperItem()
        image_urls = []
        for photo_json in response.json()['results']:
            image_urls.append(photo_json['urls']['small_s3'])
            
        item['image_urls'] = image_urls
        item['category'] = self.category
        yield item
