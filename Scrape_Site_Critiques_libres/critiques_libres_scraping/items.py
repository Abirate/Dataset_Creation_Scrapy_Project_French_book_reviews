# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AbirItem(scrapy.Item):
    book_title = scrapy.Field()
    author = scrapy.Field()
    reader_review = scrapy.Field()
    rating = scrapy.Field()
