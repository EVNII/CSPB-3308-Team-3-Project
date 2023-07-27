from flask import Flask, url_for, render_template, request
from app.database import Database
from flask_restx import Api 
from app.api import user_ns, util_ns
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.constants import db_Connnect, isPostreSQL


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = 'MusicVerseIsCool'

jwt = JWTManager(app)

db = Database()
db.set_dbFile(db_Connnect if db_Connnect else 'MusciVerse.db', isPostreSQL)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
    
api = Api(app, doc='/SwaggerUI/', version='1.0', title='Music Verse API', description='Music Verse RESTful API', authorizations=authorizations, security='apikey')
api.add_namespace(user_ns, path='/api/user')
api.add_namespace(util_ns, path='/api/util')