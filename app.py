from flask import *
import os

app = Flask(__name__)


@app.route('/lewds')
def lewds():
	os.chdir('G:\\ADs music, video, picture\\Github\\other\\Lewds\\static\\lewds')
	lewd_images = []
	for i in os.listdir():
		lewd_images.append('static/lewds/'+i)
	
	return render_template('lewds.html',images = lewd_images)


if __name__ == '__main__':
	app.run(debug=True)

