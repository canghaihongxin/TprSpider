import scrapy


class CnblognewsSpider(scrapy.Spider):
    name = 'cnblogNews'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['https://news.cnblogs.com/n/recommend']
    # 只针对当前爬虫设置，
    custom_settings = {
        # 让后面的请求引用前面的cookie
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        # undetected_chromedriver 为开源项目
        # 入口可以模拟登录拿到cookie, selenium 控制浏览器会被一些网站识别出来，知乎，接勾
        import undetected_chromedriver.v2 as uc
        browser = uc.Chrome()
        browser.get("https://account.cnblogs.com/signin")
        input("请回车继续")
        cookie_dict = {}
        cookies = browser.get_cookies()
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']

        for url in self.start_urls:
            # 将cookie 交给scrapy,
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33 '
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers,
                                 dont_filter=True)

    def parse(self, response):
        title_list = response.xpath('//div[@id="news_list"]//h2/a/text()').extract()
        if title_list:
            for title in title_list:
                print(title)

        pass
