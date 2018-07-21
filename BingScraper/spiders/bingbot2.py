# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import signals
from w3lib.html import remove_tags
import os
from bs4 import BeautifulSoup
import lxml.html
class Bingbot2Spider(scrapy.Spider):
    name = 'bingbot2'
    allowed_domains = []
    
    def __init__(self,search=None,*args,**kwargs): 
      super(Bingbot2Spider, self).__init__(*args, **kwargs)
      self.start_urls=['https://www.bing.com/search?q='+re.sub('\s','+',search)]
      self.search=search
      
    def parse(self, response):
        anchors=response.css("h2")
        for items in anchors:
            item=items.css("a::attr(href)").extract()[0]
            if "pdf" not in item:
                yield scrapy.Request(item,callback=self.parse1)
        
    def parse1(self,response):
        page_text=remove_tags(response.text).split('.')
        
        search_text=getattr(self,'search','').split('.')
        found=[]
        for line in search_text:
            for line1 in page_text:
                if line in line1:
                    found.append(line1)
                    break
        page_info={'url':response.url,'text':found}
        yield page_info
                
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Bingbot2Spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_opened(self, spider):
        try:
            os.remove("books1.json")
        except:
            pass

    def spider_closed(self, spider):
        pass
    
    
        
        