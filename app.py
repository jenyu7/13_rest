'''
Jen Yu
Period 7 SoftDev
K #13: A RESTful Journey Skyward
2017-11-09
'''
from flask import Flask, render_template
import urllib2, json
app = Flask(__name__)

@app.route("/")
def welcome():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hTUDYhfxSNhyewvcLn1JJX1hl7tnbIpvNrBmgPqi")
    d = json.loads(data.read())
    print d;
    return render_template('index.html',title = d["title"], pic0url = d["url"], exp = d["explanation"], c = d["copyright"], d = d["date"])

if __name__ == "__main__":
    app.debug = True
    app.run()
