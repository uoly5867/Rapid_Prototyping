from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def __repr__(self):
        return '%s, %s' % (str(self.username), str(self.email)) 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users/')
def users():
    allUsers = User.query.all()
    #print allUsers
    return str(allUsers)

@app.route('/users_template/')
def users_template():
    allUsers = User.query.all()
    userArr = []
    for item in allUsers:
        userArr.append(item)
        
    for item in userArr:
        print item.username
        print item.email

    return render_template('users_template.html',allUsers=userArr)

if __name__ == '__main__':
    app.run()
