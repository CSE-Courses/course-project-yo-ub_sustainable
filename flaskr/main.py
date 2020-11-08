import os
import re

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'passwrd'
# app.config['MYSQL_DB'] = 'login'

# mysql = MySQL(app)



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # MYSQL_HOST='localhost',
        MYSQL_HOST='2.tcp.ngrok.io',
        MYSQL_PORT=15551,
        MYSQL_USER='root',
        MYSQL_PASSWORD='passwrd',
        MYSQL_DB='login'
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    mysql = MySQL(app)

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

    @app.route("/publicProfileFriend")
    def publicProfileFriend():
        return render_template("publicProfileFriend.html")

    @app.route("/publicProfileNotFriend")
    def publicProfileNotFriend():
        return render_template("publicProfileNotFriend.html")

    @app.route("/login", methods = ['GET', 'POST'])
    def login():
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password, ))
            data = cur.fetchone()
            # print(data)
            if data:
                session['logged_in'] = True
                session['id'] = data[0]
                session['username'] = data[1]
                flash('You are logged in')
                return redirect(url_for('home'))
            else:
                msg = 'Invalid Credentials. Please try again.'
        return render_template("login.html", msg = msg)
    
    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     error = None
    #     if request.method == 'POST':
    #         if (request.form['username'] != 'test') or request.form['password'] != 'test': error = 'Invalid Credentials. Please try again.'
    #         else:
    #             session['logged_in'] = True
    #             flash('You are logged in.')
    #             return redirect(url_for('home'))
    #     return render_template('login.html', error=error)
     
    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        session.pop('id', None)
        session.pop('username', None)
        flash('You are logged out.')
        return redirect(url_for('home'))

    @app.route("/signup", methods = ['GET', 'POST'])
    def signup():
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM accounts WHERE username = %s', (username,))
            data = cur.fetchone()
            if data:
                # Account already exists
                msg = 'Account already exists.'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                # Invalid email address
                msg = 'Inavlid email address.'
            elif not re.match(r'[A-Za-z0-9]+', username):
                # Invalid username
                msg = 'Username must only contain characters and numbers.'
            elif not username or not password or not email:
                # Form was not filled out
                msg = 'Please enter your information.'
            else:
                cur.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
                mysql.connection.commit()
                msg = 'You have successfully registered!'
        elif request.method == 'POST':
            #Form is empty
            msg = 'Please enter your information.'
        return render_template("signup.html", msg = msg)

    @app.route("/css")
    def css():
        return render_template("static/css/style.css")

    return app
    

# if __name__ == "__main__":
#     app.run(debug=True)
