from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"adrian Aguinaga"}
    return json.dumps(me)

@app.get("/footer")#i know that this is a section not a page
def footer():
    pageName = {"pageName":"organika"}
    return json.dumps(pageName)
# please create an API to footer that contains the name of the page (organika)

app.run(debug=True)