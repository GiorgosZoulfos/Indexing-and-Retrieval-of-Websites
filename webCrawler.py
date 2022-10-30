import os.path
import scrapy
from scrapy.crawler import CrawlerProcess

savePath = r'C:\Users\gz\PycharmProjects\Glossiki Texnologia\htmlPages'


class NewsCrawlerSpider(scrapy.Spider):
    name = 'web'

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 1000
    }

    allowed_domains = [
        'bbc.com',
        'edition.cnn.com',
        'theguardian.com/world',
        'nytimes.com',
        'reuters.com'
    ]

    start_urls = [
        # 'https://www.hltv.org/news/30896/top-10-teams-of-2020',
        'https://www.bbc.com/news/uk-55528241',
        'https://edition.cnn.com/2021/01/04/health/europe-school-closures-covid-19-gbr-intl/index.html',
        'https://www.theguardian.com/us-news/2021/jan/03/trump-georgia-raffensperger-call-biden-washington-post',
        'https://www.nytimes.com/2021/01/04/opinion/manufacturing-united-states-masks.html?action=click&module'
        '=Opinion&pgtype=Homepage',
        'https://www.reuters.com/article/us-iran-nuclear-enrichment/iran-says-it-resumes-20-enrichment-at-fordow-in'
        '-latest-nuclear-deal-breach-idUSKBN299101 '
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        complete_name = os.path.join(savePath, filename)

        with open(complete_name, 'wb') as f:
            f.write(response.body)

        a_selectors = response.css("a").xpath("@href").extract()

        for selector in a_selectors:

            request = response.follow(selector, callback=self.parse)
            yield request


process = CrawlerProcess()
process.crawl(NewsCrawlerSpider)
process.start()
