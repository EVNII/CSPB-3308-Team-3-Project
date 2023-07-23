from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.models import User
from app.database import Database
from app.repository import UserRepository
from dataclasses import asdict

api = Namespace('user', description='User related operations')

user_model = api.model('User', {
    'username': fields.String(required=True, description='User name'),
    'password': fields.String(required=True, description='User password'),
})

db = Database()
db.set_dbFile('MusicVerse.db')
user_repo = UserRepository(db=db)

@api.route('/signup')
class UserSignup(Resource):
    @api.doc('create_new_user')
    @api.expect(user_model)
    def post(self):
        '''Create new user'''
        username = request.json.get('username')
        password = request.json.get('password')
        if username in user_repo.get_name2id():
            return {'message': 'User already exists'}, 400
        
        if user_repo.create_user(username=username, email="noemail@email.com", password=generate_password_hash(password)):
            return {'message': 'User created successfully'}, 201
        else:
            return 500

@api.route('/login')
class UserLogin(Resource):
    @api.doc('login_user')
    @api.expect(user_model)
    def post(self):
        '''Login user'''
        username = request.json.get('username')
        password = request.json.get('password')
        if username in user_repo.get_name2id():
            id = user_repo.get_name2id()[username]
            if check_password_hash(user_repo.get_all_users()[id].passwrod, password):
                access_token = create_access_token(identity=id)
                return {'access_token': access_token}, 200
        return {'message': 'Invalid username or password'}, 401

@api.route('/login_info')
class LoginInfor(Resource):
    @jwt_required()
    def get(self):
        '''Example route that requires login'''
        current_user_id = get_jwt_identity()
        user = user_repo.get_user_by_id(current_user_id)
        return {'logged_in_as': asdict(user)}, 200
