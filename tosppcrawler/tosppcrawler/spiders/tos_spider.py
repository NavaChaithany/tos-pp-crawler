import scrapy


class TosSpiderSpider(scrapy.Spider):
    name = "tos_spider"
    allowed_domains = ["duckduckgo.com", "mozilla.org"]
    start_urls = [
    "https://duckduckgo.com/terms",
    "https://www.mozilla.org/en-US/privacy/"
     ]


    def parse(self, response):
        title = response.css('title::text').get()
        content = response.css('body *::text').getall()
        cleaned_content = ' '.join([line.strip() for line in content if line.strip()])

        yield {
            "title": title,
            "url": response.url,
            "text": cleaned_content
        }
