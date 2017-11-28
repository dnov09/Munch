# Setting Up Flask
from flask import Flask, render_template, redirect, url_for, request, session
from flask import flash
from functools import wraps
import sqlite3
from flask import g

# Importing Other Modules
import os
import requests


# Importing Custom Modules
# from app import main

server = Flask(__name__)
server.database = "munch.db"
server.secret_key = os.urandom(12)



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            # Flash displays messages after a condition has been met
            flash('You must login first.')
            return redirect(url_for('login'))
    return wrap


# def connect_db():
#     return sqlite3.connect(server.database)


@server.route('/')
# Adds the decorator to the route
@login_required
def home():
    # g.db = connect_db()  # Establishes a connection with db
    # cur = g.db.execute('select * from food')  # Querry the db
    # posts = [dict(cuisines=row[0]) for row in cur.fetchall()]
    # g.db.close()
    return render_template('databasetest.html', posts=posts)


@server.route('/menue')
def menu():
    return render_template('menue.html')


@server.route('/requests')
def user_requests():
    return render_template('request.html')


@server.route('/caroucel')
def caroucel():
    return render_template('C.html')


@server.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@server.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Logged out!')
    return redirect(url_for('home'))


@server.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'dnov' or request.form['password'] != 'cs100':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Login in Successful!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    server.run(debug=True)

server.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8081)))
