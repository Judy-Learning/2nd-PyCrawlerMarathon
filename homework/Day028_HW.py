import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/KoreaDrama/M.1585846377.A.B81.html',
        'https://www.ptt.cc/bbs/KoreaDrama/M.1586178201.A.08E.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='output.json')
    process.start()

if __name__ == '__main__':
    main()
