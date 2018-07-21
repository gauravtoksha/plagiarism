from scrapy.crawler import CrawlerRunner
import os,sys,time,json
from BingScraper.spiders.bingbot2 import Bingbot2Spider
from crochet import setup
setup()
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from pathlib import Path


class SpiderHandler():

    def __init__(self,searchText):
        self.searchText=searchText
        
        
        
    def run_crawling(self):
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        sys.path.append('BingScraperProject/BingScraper')        
        settings = Settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'BingScraper.settings'
        settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(settings_module_path, priority='project')
        try:
            runner = CrawlerRunner(settings)
            runner.crawl(Bingbot2Spider,search=self.searchText)
        except Exception as e:
            print(e)
        my_file = Path("books1.json")
        while True:
            if my_file.is_file():        
                try:
                    with open('books1.json') as f:
                        data=json.load(f)
                except:
                    time.sleep(2)
                    continue
                hashmap={}
                for items in data:
                    if items['url'] in hashmap:
                        hashmap.update({items['url']:hashmap[items['url']].append(items['text'])})
                    else:
                        hashmap[items['url']]=items['text']
                return hashmap
                

if __name__=="__main__":
    #exampletext ="""A study was conducted to test the effectiveness of plagiarism detection software in a higher education setting. One part of the study assigned one group of students to write a paper. These students were first educated about plagiarism and informed that their work was to be run through a plagiarism detection system. A second group of students was assigned to write a paper without any information about plagiarism. The researchers expected to find lower rates in group one but found roughly the same rates of plagiarism in both groups."""
    exampletext="A distributed system is a model in which components located on networked computers communicate and coordinate their actions by passing messages."
    s=SpiderHandler(exampletext)
    hashmap1=s.run_crawling()
    
    print(hashmap1)
    
    