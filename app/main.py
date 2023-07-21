from flask import Flask, url_for, render_template, request
from database import Database

app = Flask(__name__)

db = Database()
db.set_dbFile('MusicVerse.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')