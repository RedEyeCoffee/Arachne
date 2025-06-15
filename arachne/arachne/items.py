# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChapterItem(scrapy.Item):
    number = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()


class NovelItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

    chapters = scrapy.Field()
