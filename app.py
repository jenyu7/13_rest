from flask import Flask, render_template
import urllib2, json
app = Flask(__name__)

@app.route("/")
def welcome():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hTUDYhfxSNhyewvcLn1JJX1hl7tnbIpvNrBmgPqi")
    d = json.loads(data.read())
    print d;
    return render_template('index.html', picurl = d["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
