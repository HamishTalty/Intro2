#!/usr/bin/env python

from subprocess import run as run_process
from requests import get
from bottle import template, route, request, run as run_app
from sys import stderr, exit

# HTML Template
page = """
%for para in displayText.splitlines():
    <p>{{para}}</p>
%end

<form action="/" method="GET">
    <input type="submit" name="getnewcontent" value="getnewcontent">
    <input type="submit" name="transformcontent" value="transformcontent">
</form>
"""

def getNewContent(paraCount="5", paraLen="short", paraFormat="plaintext"):
    print("getting fresh content", file=stderr)
    return get(f"https://loripsum.net/api/{paraCount}/{paraLen}/{paraFormat}").text

def processText(text):
    print("transforming text", file=stderr)
    inputb = bytearray(text,"utf-8")

    # call our external module via stdio
    resp = run_process(["./reverseTextLines2.py"], shell=True, input= inputb, capture_output= True)
    
    return resp.stdout.decode("utf-8")

@route('/')
def index( method="GET"):

    global displayText

    if request.query.transformcontent == "transformcontent":
        displayText = processText(displayText)

    else:
        displayText = getNewContent()

    return template(page, displayText=displayText)

if __name__ == "__main__":
    displayText = getNewContent()
    run_app(host='localhost', port=8080, debug=True, reloader=True)
