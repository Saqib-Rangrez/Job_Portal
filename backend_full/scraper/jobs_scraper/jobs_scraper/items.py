import scrapy

class JobItem(scrapy.Item):
    title = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    employment_type = scrapy.Field()
    posted_date = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
