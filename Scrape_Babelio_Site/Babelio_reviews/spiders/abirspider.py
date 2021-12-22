import scrapy

class AbirspiderSpider(scrapy.Spider):
    name = 'abirspider'
    start_urls = ['https://www.babelio.com/dernierescritiques.php?p=2']
   

    def parse(self, response):
        
        # I retrieved all the xpahs of the fields to extract
        
        block_reviews = response.xpath('//div[@class="post_con"]')
        for block in block_reviews:
            
            book_title = block.xpath('.//a[@class ="titre1"]/text()').get()
            author = block.xpath('.//a[@class="libelle"]/text()').get()
            review = block.xpath('normalize-space(.//div[@class="text row"]/div/text())').get()
            rating = block.xpath('.//td/div[@data-rateit-mode= "font"]/@data-rateit-value').get()

            yield{
                'book_title':book_title,
                'author': author,
                'review': review,
                'rating' : rating
            }
        # Check if the next button exists (to re-chain the parse function).
        next_button = response.xpath('//a[@class="fleche icon-next"]/@href').get()
        if next_button:
            new_url = response.urljoin(next_button)
            yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)

        
        