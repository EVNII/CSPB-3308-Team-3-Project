"""File `app.main` is the entry of the flask api server"""

from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.api import user_ns, util_ns, score_ns
from app.constants import db_Connnect
from app.models import db


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = 'MusicVerseIsCool'

jwt = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_Connnect
db.init_app(app)

with app.app_context():
    db.create_all()

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
api.add_namespace(score_ns, path='/api/score')
