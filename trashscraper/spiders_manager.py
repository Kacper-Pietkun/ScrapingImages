from twisted.internet.asyncioreactor import install
install()
import json
import traceback
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from trashscraper.spiders.bing_image_trash import BingImageTrashSpider
from trashscraper.spiders.unsplash_keyword_trash import UnsplashKeywordTrashSpider
from trashscraper.spiders.bing_keyword_trash import BingKeywordTrashSpider
from scrapy.utils.project import get_project_settings
from trashscraper.spiders.trash_keyword_spider import TrashKeywordSpider
from trashscraper.spiders.trash_image_spider import TrashImageSpider


def get_spider_classes(param):
    if param == 'unsplash_keyword_trash':
        return [UnsplashKeywordTrashSpider]
    elif param == 'bing_keyword_trash':
        return [BingKeywordTrashSpider]
    elif param == 'bing_image_trash':
        return [BingImageTrashSpider]
    raise KeyError(f'Spider with given name \'{param}\' does not exist')


if __name__ == "__main__":
    runner = CrawlerRunner(get_project_settings())

    with open("params.json") as params_file:
        data = json.load(params_file)
        runs_len = len(data["runs"])

        try:
            for iter, run in enumerate(data["runs"]):
                spiders = get_spider_classes(run["spider_name"])
                
                for spider in spiders:
                    if isinstance(spider(), TrashKeywordSpider):
                        runner.crawl(spider,
                                    category=run["category"],
                                    keywords=run["keywords"],
                                    size=run["size"])
                    else:
                        runner.crawl(spider,
                                    category=run["category"],
                                    urls=run["urls"],
                                    size=run["size"])
            d = runner.join()
            d.addBoth(lambda _: reactor.stop())
            reactor.run()
        except KeyError as e:
            print("iteration: ", iter)
            traceback.print_exc()
