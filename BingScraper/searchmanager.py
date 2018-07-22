# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:13:55 2018

@author: windows
"""

class SearchManager():
    def __init__(self,engine):
        self.engine=engine
    
    def getStartUrl(self):
        if self.engine=="bing":
            return "https://www.bing.com/search?q="
        if self.engine=="google":
            pass
        if self.engine=="duckduckgo":
            #needs to implement splash for this
            pass
        if self.engine=="yahoo":
            return "http://in.search.yahoo.com/search?q="
    
    def getLinks(self,response):
        links=[]
        if self.engine=="bing":
            try:
                for items in response.css("li[class=b_algo]"):
                    item=items.css("a::attr(href)").extract()[0]
                    if "pdf" not in item:
                        links.append(item)
                return links
            except Exception as e:
                print("in search manager:"+str(e))
        if self.engine=="yahoo":
        	try:
        		links=response.css(".searchCenterMiddle").css("a.ac-algo::attr(href)").extract()
        		return links
        	except Exception as e:
        		print(str(e))