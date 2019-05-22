from crawler import Crawler
from domain import *
from general import *

PROJECT_NAME = 'silverbolt'
HOMEPAGE = 'https://www.silverbolt.ai/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        for link in queued_links:
            Crawler.crawl_page('Main thread', link)


crawl()
