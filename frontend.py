from flask import Flask,request,render_template,url_for
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
	engine=request.form['selector']
	s=SpiderHandler(searchQuery,engine)
	hashmap=s.run_crawling()
	return render_template('result.html',result=hashmap,demo="demo",sq=searchQuery.split('.'))

if __name__ == '__main__':
   app.run()