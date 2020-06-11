import requests
import os

html = requests.get("http://127.0.0.1:5000/lewds").text
f = open('index.html','w')
f.write(html)
print("index.html file updated!")
f.close()

