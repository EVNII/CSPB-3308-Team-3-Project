"""File `app.main` is the entry of the flask api server"""

from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.database import Database
from app.api import user_ns, util_ns
from app.constants import db_Connnect, isPostreSQL


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = 'MusicVerseIsCool'

jwt = JWTManager(app)

db = Database()
db.set_db_conn_str(
    db_Connnect if db_Connnect else 'MusciVerse.db', isPostreSQL
)

authorizations = {
    'apikey': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}
}

api = Api(
    app,
    doc='/SwaggerUI/',
    version='1.0',
    title='Music Verse API',
    description='Music Verse RESTful API',
    authorizations=authorizations,
    security='apikey',
)
api.add_namespace(user_ns, path='/api/user')
api.add_namespace(util_ns, path='/api/util')
