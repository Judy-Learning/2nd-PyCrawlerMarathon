import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime

def main():
    #target_board = ['Gossiping', 'KoreaDrama', 'STOCK']
    target_board = ['KoreaDrama']
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('PTTCrawler', board=board)
    process.start()

if __name__ == '__main__':
    main()
