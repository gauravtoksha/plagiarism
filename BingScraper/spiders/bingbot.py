# -*- coding: utf-8 -*-
import scrapy


class BingbotSpider(scrapy.Spider):
    name = 'bingbot'
    allowed_domains = ['https://www.bing.com/search?q=A+study+conducted+test+effectiveness+plagiarism+detection+software+higher+education+setting+.+One+part+study+assigned+one+group+students+write+paper+.+These+students+first+educated+plagiarism+informed+work+run+plagiarism+detection+system+.+A+second+group+students+assigned+write+paper+without+information+plagiarism+.+The+researchers+expected+find+lower+rates+group+one+found+roughly+rates+plagiarism+groups+']
    start_urls = ['http://https://www.bing.com/search?q=A+study+conducted+test+effectiveness+plagiarism+detection+software+higher+education+setting+.+One+part+study+assigned+one+group+students+write+paper+.+These+students+first+educated+plagiarism+informed+work+run+plagiarism+detection+system+.+A+second+group+students+assigned+write+paper+without+information+plagiarism+.+The+researchers+expected+find+lower+rates+group+one+found+roughly+rates+plagiarism+groups+/']

    def parse(self, response):
        pass
