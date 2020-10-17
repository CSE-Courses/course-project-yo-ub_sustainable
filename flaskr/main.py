import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

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
        return render_template("challenge_list.html")
    
    @app.route("/challenge1")
    def chall_pg1():
        return render_template("challenge_pages/challenge1.html")
    
    @app.route("/challenge2")
    def chall_pg2():
        return render_template("challenge_pages/challenge2.html")

    @app.route("/challenge3")
    def chall_pg3():
        return render_template("challenge_pages/challenge3.html")

    @app.route("/challenge4")
    def chall_pg4():
        return render_template("challenge_pages/challenge4.html")

    @app.route("/challenge5")
    def chall_pg5():
        return render_template("challenge_pages/challenge5.html")
    
    @app.route("/challenge6")
    def chall_pg6():
        return render_template("challenge_pages/challenge6.html")

    @app.route("/friends")
    def friend():
        return render_template("friends.html")

  #  @app.route("/login")
  #  def login():
  #      return render_template("login.html")
    
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

    return app
