import scrapy


# Base class for other trash spiders
# DON'T RUN IT TO CRAWL ANYTHING
class TrashSpider(scrapy.Spider):

    def start_requests(self):
        try:
            print(
            '''
            *******************************************
            TRASH SPIDER SEARCHING FOR:
            category: {0}
            keyword: {1}
            number of photos: {2}
            *******************************************
            '''.format(self.category, self.keyword, self.size))
        except Exception as e:
            print("MISSING ARGUMENTS: ", e)
            return

        self.size = int(self.size)
        if self.category_validation() is False:
            print("INVALID CATEGORY: ")
            return

        if self.number_of_photos_validation() is False:
            print("INVALID SIZE: ")
            return

    # Allowed categories are equal to the classes of trash
    def category_validation(self):
        return self.category == 'mixed' or \
            self.category == 'plastic_metal' or \
            self.category == 'paper' or \
            self.category == 'glass' or \
            self.category == 'bio'

    def number_of_photos_validation(self):
        return self.size > 0
