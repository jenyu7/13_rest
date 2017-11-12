'''
Jen Yu
Period 7 SoftDev
K #13: A RESTful Journey Skyward
2017-11-09
'''

from flask import Flask, render_template
from utils import read
import urllib2, json

app = Flask(__name__)
#?api-key=70995bc868a043d3bd94e12c22604be6

@app.route("/")
def start():
    #data = urllib2.urlopen("http://api.nytimes.com/svc/books/v3/lists.json?api-key=70995bc868a043d3bd94e12c22604be6")
    #d = json.loads(data.info())
    print read.get_booklist()
    return render_template("books.html", names = read.get_list_names(), dict = read.get_booklist())

#old nasa page from hw #12
@app.route("/hw12")
def hw12():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hTUDYhfxSNhyewvcLn1JJX1hl7tnbIpvNrBmgPqi")
    d = json.loads(data.read())
    print d;
    return render_template('index.html',title = d["title"], pic0url = d["url"], exp = d["explanation"], c = d["copyright"], d = d["date"])

if __name__ == "__main__":
    app.debug = True
    app.run()
