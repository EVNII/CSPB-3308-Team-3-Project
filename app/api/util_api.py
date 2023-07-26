from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.database import Database
from app.repository import UserRepository

util_ns = Namespace('util', description='Utlity\'s Quesring')

db = Database()
db.set_dbFile('MusicVerse.db')
user_repo = UserRepository(db=db)

@util_ns.route('/user_count')
class UserCount(Resource):
    @util_ns.doc('create_new_user')
    def get(self):
        '''Query User Counts'''
        return user_repo.get_users_counts()