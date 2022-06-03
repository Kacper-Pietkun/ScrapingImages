import scrapy
from trashscraper.items import TrashscraperItem
from trashscraper.spiders.trash_keyword_spider import TrashKeywordSpider


class UnsplashKeywordTrashSpider(TrashKeywordSpider):
    name = 'unsplash_keyword_trash'
    allowed_domains = ['unsplash.com']

    def start_requests(self):
        super().start_requests()

        keywords_list = self.keywords.split(';')
        urls = [f'https://unsplash.com/napi/search/photos?query={keyword}&per_page={self.size if self.size != 0 else 10000}&page=1&xp=' for keyword in keywords_list]
        for keyword, url in zip(keywords_list, urls):
            yield scrapy.Request(url, meta={'keyword': keyword})

    def parse(self, response):
        item = TrashscraperItem()
        
        photos_json = response.json()['results']
        for iter, photo_json in enumerate(photos_json):
            if iter >= self.size and self.size != 0:
                break
            item['image_urls'] = [photo_json['urls']['small_s3']]
            item['category'] = self.category
            yield item
    
        if self.size > len(photos_json) and self.size != 0:
            print(f'SPIDER CATEGORY={self.category}, KEYWORD={response.meta["keyword"]} UNABLE TO DOWNLOAD MORE IMAGES: got {len(photos_json)} out of {self.size}')
