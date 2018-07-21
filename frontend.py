from flask import Flask,request,render_template
from serverscript import SpiderHandler
import sys
app = Flask(__name__)
sys.path.append('C:/Users/windows/BingScraperProject/')

@app.route('/index/',methods=['POST','GET'])
def index():
	return render_template('index.html')

@app.route('/submit/',methods=['POST'])
def submit():
	searchQuery=request.form['comment']
	s=SpiderHandler(searchQuery)
	hashmap=s.run_crawling()
	return render_template('result.html',result=hashmap,demo="demo",sq=searchQuery.split('.'))

if __name__ == '__main__':
   app.run()