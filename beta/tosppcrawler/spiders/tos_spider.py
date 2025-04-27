import scrapy

class TosSpiderSpider(scrapy.Spider):
    name = "tos_spider"
    allowed_domains = [
        "duckduckgo.com", 
        "mozilla.org",
        "amazon.com",
        "microsoft.com",
        "healthline.com",
        "wikipedia.org",
        "khanacademy.org"
    ]
    start_urls = [
        "https://duckduckgo.com/terms",
        "https://www.mozilla.org/en-US/privacy/",
        "https://www.amazon.com/gp/help/customer/display.html?nodeId=508088",  # Amazon TOS
        "https://privacy.microsoft.com/en-us/privacystatement",               # Microsoft Privacy
        "https://www.healthline.com/privacy-policy",                          # Healthline Privacy
        "https://foundation.wikimedia.org/wiki/Terms_of_Use",                  # Wikipedia TOS
        "https://www.khanacademy.org/about/tos"                                # Khan Academy TOS
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
