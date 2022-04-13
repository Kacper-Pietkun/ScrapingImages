# ScrapingImages

## Usage of web scraper (currently downloading images only from unsplash.com and bing.com):

Scraper was written to collect images for trash dataset. They are going to be used in trash segregation classification problem. However, scraper can be used to download all kinds of images (not only trash) from pages listed above.

#### Command line (allows running only one spider)
- get to the trashscraper folder
- run following command `scrapy crawl <spider_name> -a category=<category> -a keyword=<keyword> -a size=<size> [--nolog]`
- where
    - \<spider_name> can be equal to `unsplash_trash` for scrapping unsplash.com or `bing_trash` for scrapping bing.com
    - \<category> can be one of the following:
        - mixed
        - plastic_metal
        - paper
        - glass
        - bio
    - \<keyword> specifies what images are going to be loaded
    - \<size> declares how many images will be downloaded from the page (There might be some limitations when size is too big)
    - use [--nolog] if you don't want to see the logs

#### Script (allows running many spiders)
- get to the trashscraper folder
- specify parameters in params.json (each run will be given to the separate spider specified by `spider_name` ("all_spiders" means that every spider will be started for that run))
- Examplary content of params.json:

        {
            "runs": [
                { 
                    "spider_name": "all_spiders",
                    "category": "glass",
                    "keyword": "jar",
                    "size": "3"
                },
                { 
                    "spider_name": "unsplash_trash",
                    "category": "plastic_metal",
                    "keyword": "can",
                    "size": "4"
                },
                { 
                    "spider_name": "bing_trash",
                    "category": "paper",
                    "keyword": "newspaper",
                    "size": "10"
                }
            ]
        }
    With this content in params.js, four spiders will be started in total. Two spiders for the first run (because currently there are only two types of spiders), each of them will download 3 images of a 'jar' (6 in total) and will save them in the glass directory. Unsplash_trash spider will be runned for the second run and it will download 4 images of a 'can' and will save them in plastic_metal directory. Bing_trash spider will be runned for the third run and it will download 10 images of a 'newspaper' and will save them in paper directory.
    
- run following command `python spiders_manager.py`