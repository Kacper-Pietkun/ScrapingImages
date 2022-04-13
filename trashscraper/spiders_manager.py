import json
import traceback
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from trashscraper.spiders.unsplash_trash import UnsplashTrashSpider
from trashscraper.spiders.bing_trash import BingTrashSpider
from scrapy.utils.project import get_project_settings


def get_spider_classes(param):
    if param == 'unsplash_trash':
        return [UnsplashTrashSpider]
    elif param == 'bing_trash':
        return [BingTrashSpider]
    elif param == 'all_spiders':
        return [UnsplashTrashSpider, BingTrashSpider]
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
                    runner.crawl(spider,
                                category=run["category"],
                                keyword=run["keyword"],
                                size=run["size"])
            d = runner.join()
            d.addBoth(lambda _: reactor.stop())
            reactor.run()
        except KeyError as e:
            print("iteration: ", iter)
            traceback.print_exc()
