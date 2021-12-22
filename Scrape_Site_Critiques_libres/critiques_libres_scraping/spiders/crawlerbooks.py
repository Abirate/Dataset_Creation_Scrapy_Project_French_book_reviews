import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AbirItem


class CrawlerbooksSpider(CrawlSpider):

    name = 'crawlerbooks'

    start_urls = ['http://www.critiqueslibres.com/i.php/list/newcrit']\
    +[f'http://www.critiqueslibres.com/i.php/list/newcrit/?p={i}' for i in range(2,8)]\
    +['http://www.critiqueslibres.com/i.php/list/newecl/']\
    +[f'http://www.critiqueslibres.com/i.php/list/newecl?p={i}' for i in range(2,8)]\
    +['http://www.critiqueslibres.com/i.php/list/topstar/']\
    +[f'http://www.critiqueslibres.com/i.php/list/topstar/?p={i}' for i in range(2,8)]\
    +['http://www.critiqueslibres.com/i.php/list/newparu/']\
    +[f'http://www.critiqueslibres.com/i.php/list/newparu/?p={i}' for i in range(2,8)]
    
    # We add the rules for the crawler, specifying the xpaths of links to follow.
    # Here I used restrict_paths, but there are other prams: allow = ..., deny = ..
    # and restrict_css = ... (If you are more comfortable with CSS selectors)

    rules = (
        Rule(LinkExtractor(restrict_xpaths= '//div[@class ="media-body"]/h4/a[@class ="lientexte"]'), callback='parse_item', follow=True),)

    # We define the parse_item function of the callback (included in the rule).
    # In this function, we define all the xpaths of the elements we want to extract
    def parse_item(self, response):
        block_book = response.xpath('//div[@class= "panel-body"]')[0]
        title = block_book.xpath('normalize-space(.//div[@class="media-body"]/strong/text())').get()
        author = response.xpath('normalize-space(//h3/a/text())').get()
        rating = response.xpath('//div[@id= "summary"]/img/@alt').get()
        review = response.xpath('normalize-space(//p[@class ="critic"]/text())').get()

        # We instantiate an object from the AbirItem class (defined in the items.py file).
        # See items.py file
        # Note: we have to import this class here in the crawler file (see above in the import section).
        french_reviews = AbirItem()

        # we define each item
        french_reviews['book_title'] = title
        french_reviews['author'] = author
        french_reviews['reader_review'] = review
        french_reviews['rating'] = rating
        
        return french_reviews



