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
            spider name: {0}
            category: {1}
            number of photos: {2}
            '''.format(self.name, self.category, self.size))
        except Exception as e:
            print(e)
            raise ValueError("MISSING ARGUMENTS!")

        
        if self.category_validation() is False:
            print("category doesn't match any folder")
            raise ValueError("INVALID CATEGORY!")

        if self.number_of_photos_validation() is False:
            print("Size must be greater or equal to 0")
            raise ValueError("INVALID SIZE!")

    # Allowed categories are equal to the classes of trash
    def category_validation(self):
        return self.category == 'mixed' or \
            self.category == 'plastic_metal' or \
            self.category == 'paper' or \
            self.category == 'glass' or \
            self.category == 'bio'

    # size 0 means it will load every image from the page
    def number_of_photos_validation(self):
        try:
            self.size = int(self.size)
        except ValueError as e:
            print(e)
            raise ValueError("Size cannot be converted to int")
        return self.size >= 0
