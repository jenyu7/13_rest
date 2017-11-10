from flask import Flask, render_template
import urllib2
app = Flask(__name__)

@app.route("/")
def welcome():
    url = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hTUDYhfxSNhyewvcLn1JJX1hl7tnbIpvNrBmgPqi")
    d = url.loads()
    return render_template("index.html", picurl = d["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
