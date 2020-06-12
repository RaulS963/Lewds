from flask import *
import os
import confidential

app = Flask(__name__)


@app.route('/')
def home():
	return ('''
		<h1>Welcome to lewds</h1>
		<a href="https://github.com/RaulS963/Lewds"> goto github <a>
		''')

@app.route('/lewds')
def lewds():
	f = open("exsist.txt",'r')
	old_img_set = set(f.read().splitlines())
	print(f'no of img exsist: {len(old_img_set)}')
	f.close()
	os.chdir(confidential.IMG_FOLDER_PATH)
	full_img_set = set(os.listdir())
	img_set = list( full_img_set - old_img_set )
	lewd_images = []
	for i in img_set:
		lewd_images.append('static/lewds/'+i)

	try:
		lewd_images.remove('static/lewds/6637dfca3905d61252cccd18f9c42644 (1).gif')
	except:
		pass

	os.chdir(confidential.MAIN_DIR_PATH)
	if(len(lewd_images) == 0):
		return ("""
			<h1>No new images found!</h1>
			""")

	return render_template('lewds.html',images = lewd_images)


if __name__ == '__main__':
	app.run(debug=True)

