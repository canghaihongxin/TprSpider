import scrapy


class CnblognewsSpider(scrapy.Spider):
    name = 'cnblogNews'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['https://news.cnblogs.com/n/recommend']

    def parse(self, response):
        title_list = response.xpath('//div[@id="news_list"]//h2/a/text()').extract()
        if title_list:
            for title in title_list:
                print(title)

        pass
