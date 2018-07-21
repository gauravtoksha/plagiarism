# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
import json,os

class BingscraperPipeline(object):
    def __init__(self):
        self.file = open("something.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print("spider closed")
        os.rename("something.json","books1.json")
        
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print("written to file")
        return item
    
        
            
        
        
