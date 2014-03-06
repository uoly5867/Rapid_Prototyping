from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

class links():
    def __init__(self, link, name):
        self.link = link
        self.name = name
        
def getLink(link, name):
    alink = links(link, name)
    return alink
    
@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/home/')
def hello(welcome="Welcome to Uonsong's Webpage"):
    cnn = getLink("http://www.cnn.com/", "CNN")
    twitter = getLink("http://www.twitter.com/", "Twitter")
    facebook = getLink("http://www.facebook.com/", "Facebook")
    linkArr = []
    linkArr.append(cnn)
    linkArr.append(twitter)
    linkArr.append(facebook)
    return render_template('minTemplate.html', welcome=welcome, navigation=linkArr)
    
if __name__ == '__main__':
    app.run()
