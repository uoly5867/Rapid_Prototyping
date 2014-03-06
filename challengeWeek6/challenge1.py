from flask import render_template
from flask import Flask
app = Flask(__name__)
app.debug = True

class Link(object):
	href = ""
	caption = ""
	def __init__(self, href, caption):
		self.href = href
		self.caption = caption

def makelink(href, caption):
	link = Link(href, caption)
	return link

@app.route('/home')
def home():
	link1 = makelink("http://www.cnn.com/", "CNN")
	link2 = makelink("http://www.facebook.com/", "Facebook")
	link3 = makelink("http://www.google.com/", "Google")
	navarray = []
	navarray.append(link1)
	navarray.append(link2)
	navarray.append(link3)
	string1 = "Welcome to Alex's page!!!!"
	return render_template('minimal_temp.html', navigation = navarray, a_variable = string1)

if __name__ == '__main__':

    app.run()
