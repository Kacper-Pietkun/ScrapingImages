from trashscraper.spiders.trash_spider import TrashSpider


# Base class for other trash spiders
# DON'T RUN IT TO CRAWL ANYTHING
class TrashImageSpider(TrashSpider):

    def start_requests(self):
        super().start_requests()
        try:
            print(
            '''
            urls: {0}
            *******************************************
            '''.format(self.urls))
        except Exception as e:
            print(e)
            raise ValueError("MISSING ARGUMENTS!")
