# -*- coding: utf-8 -*-
# @Author: Pan Chao
# @Date:   2017-09-04 12:52:36
# @Last Modified by:   Pan Chao
# @Last Modified time: 2017-09-04 13:24:29

'''
Scrapy quickstart example.

Reference:
  - https://doc.scrapy.org/en/latest/intro/tutorial.html
'''

# Create a new scrapy project
scrapy startproject <project_name>

# Create a spider class
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    ## Instead of implementing a start_requests(), we can just define a 
    ## start_urls class attribute as follows:
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]    

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

# Sraping and Storing data
scrapy crawl quotes -o quotes.jl