import requests
import os
import json

html = requests.get("http://127.0.0.1:5000/lewds").text
f = open('index.html','w')
f.write(html)
print("index.html file updated!")
f.close()


main_dir = os.getcwd()
os.chdir('G:\\ADs music, video, picture\\Github\\other\\Lewds\\static\\lewds')
files = os.listdir()
links = []
for filename in files:
	if(filename != '6637dfca3905d61252cccd18f9c42644 (1).gif'):
		links.append("https://rauls963.github.io/Lewds/static/lewds/"+filename)

os.chdir(main_dir)
with open('links.json','w') as f:
	json.dump(links,f)

print("links.json updated!")
