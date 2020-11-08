import os

from flask import Flask, render_template, request, redirect, url_for, session, flash
from users import Users

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dash")
    def dash():
        return render_template("userdashboard.html")

    @app.route("/challenge")
    def chall():
        return render_template("challenge.html")

    @app.route("/friends")
    def friend():  
        return render_template("friends.html",
            friendList=Users['friends'],
            notFriendList=Users['notFriends'])

    @app.route("/publicProfileFriend")
    def publicProfileFriend():
        return render_template("publicProfileFriend.html")

    @app.route("/publicProfileNotFriend")
    def publicProfileNotFriend():
        return render_template("publicProfileNotFriend.html")
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if (request.form['username'] != 'test') or request.form['password'] != 'test': error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                flash('You are logged in.')
                return redirect(url_for('home'))
        return render_template('login.html', error=error)
     
    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You are logged out.')
        return redirect(url_for('home'))
    
    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/css")
    def css():
        return render_template("static/css/style.css")
    
    #Friends Stuff 
    
    def getUserName(name):
        for uType in Users:
            for user in Users[uType]:
                if user['name'] == name:
                    return user['username']
        return None

    def getProfilePic(name):
        for uType in Users:
            for user in Users[uType]:
                if user['name'] == name:
                    return user['profilePic']
        return None
    
    @app.route("/addFriend", methods = ['POST'])
    def addFriend():
        if request.method == 'POST':
            name = request.form['notFriend']
            newFriend = {'username': getUserName(name), 'name': name, 'profilePic':  getProfilePic(name)}
            Users['friends'].append(newFriend)
            Users['notFriends'].remove(newFriend)
        return redirect(url_for('friend'))
    @app.route("/remFriend", methods = ['POST'])
    
    def remFriend():
        if request.method == 'POST':
            name = request.form['friend']
            unFriend = {'username': getUserName(name), 'name': name, 'profilePic': getProfilePic(name)}
            Users['notFriends'].append(unFriend)
            Users['friends'].remove(unFriend)
        return redirect(url_for('friend'))
    return app