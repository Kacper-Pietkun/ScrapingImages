from trashscraper.spiders.trash_spider import TrashSpider


# Base class for other trash spiders
# DON'T RUN IT TO CRAWL ANYTHING
class TrashKeywordSpider(TrashSpider):

    def start_requests(self):
        super().start_requests()
        try:
            print(
            '''
            keywords: {0}
            *******************************************
            '''.format(self.keywords))
        except Exception as e:
            print(e)
            raise ValueError("MISSING ARGUMENTS!")
