# ScrapingImages

## Supported websites
Currently downloading images is possible only from:
- unsplash.com
- bing.com

## Spiders
There are three types of spides that are used to crawl:
- bing_image_trash (crawls bing.com, needs "urls" as parameter)
- bing_keyword_trash (crawls bing.com, needs "keywords" as parameter)
- unsplash_keyword_trash (crawls unsplash.com, needs "keywords" as parameter)

## Usage of web scraper
Scraper was written to collect images for trash dataset. They are going to be used in trash segregation classification problem. However, scraper can be used to download all kinds of images (not only trash) from pages listed above.

#### Command line (allows running only one spider at a time)
- get to the trashscraper folder
- run following command `scrapy crawl <spider_name> -a category=<category> -a keywords="<keywords>" -a urls="<urls>" -a size=<size> [--nolog]`
- where
    - \<spider_name> must be equal to the name of one of the spiders
    - \<category> can be one of the following (determines where images are going to be saved):
        - mixed
        - plastic_metal
        - paper
        - glass
        - bio
    - \<keywords> list of keywords separated by semicolon. Specifies what images are going to be loaded - search images based on a keyword (if keywords are passed then urls cannot be passed, remember to check what parameters given spider needs)
    - \<urls> list of urls separated by semicolon. Spider will crawl on those pages. Urls must lead to pages that search images based on images (if urls are passed then keywords cannot be passed, remember to check what parameters given spider needs)
    - \<size> declares how many images will be downloaded from the page (there might be some limitations when size is too big) (size=0 means that all images from the page are going to be saved)
    - use [--nolog] if you don't want to see the logs

#### Script (allows running many spiders at a time)
- get to the trashscraper folder
- specify parameters in params.json (each run will be given to the separate spider specified by `spider_name`)
- Examplary content of params.json:

        {
            "runs": [
                { 
                    "spider_name": "bing_keyword_trash",
                    "category": "plastic_metal",
                    "keywords": "can;bubble wrapper;plastic bag",
                    "size": "2"
                },
                { 
                    "spider_name": "unsplash_keyword_trash",
                    "category": "paper",
                    "keywords": "notebook;newspaper;",
                    "size": "4"
                },
                { 
                    "spider_name": "bing_image_trash",
                    "category": "glass",
                    "urls": "url1;url2;url3",
                    "size": "3"
                }
		
	        ]
        }
        
        
    - With this content in params.js, three spiders will be started in total.
    - First spider "bing_keyword_trash" will download two images of a "can", "bubble wrapper" and a "plastic bag" (six images in total). Images will be saved in "plastic_metal" folder.
    - Second spider "unsplash_keyword_trash" will download four images of a "notebook" and a "newspaper" (eight images in total). Images will be saved in "paper" folder.
    - Third spider "bing_image_trash" will download three images from all of the urls: "url1", "url2", "url3" (nine images in total). Images will be saved in "glass" folder.
    
- run following command `python spiders_manager.py`

## Notes
- you might need to run "playwrith install" after configuring your virtual environment
- Crawler works only on linux (don't know what is wrong with Windows, but after adding scrapy-playwright it stopped working)
