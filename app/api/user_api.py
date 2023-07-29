"""
Module `app.api.user_api` defines user relative APIs, such as
login/logout.
"""

from dataclasses import asdict
from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity
from app.database import Database
from app.repository import UserRepository
from app.constants import db_Connnect, isPostreSQL

user_ns = Namespace('user', description='User related operations')

user_login_model = user_ns.model(
    'User',
    {
        'username': fields.String(required=True, description='User name'),
        'password': fields.String(required=True, description='User password'),
    },
)

user_info_model = user_ns.model(
    'User',
    {
        'username': fields.String(required=True, description='User name'),
        'password': fields.String(required=True, description='User password'),
    },
)

db = Database()
db.set_db_conn_str(db_Connnect, isPostreSQL)
user_repo = UserRepository(db_ins=db)


@user_ns.route('/signup')
class UserSignup(Resource):
    """`UserSignup` support post method to register a new user."""

    @user_ns.doc('create_new_user')
    @user_ns.expect(user_login_model)
    def post(self):
        '''Create new user'''
        username = request.json.get('username')
        password = request.json.get('password')
        if user_repo.get_name2id():
            if username in user_repo.get_name2id():
                return {'message': 'User already exists'}, 400

        if user_repo.create_user(
            username=username,
            email="noemail@email.com",
            password=generate_password_hash(password),
        ):
            return {'message': 'User created successfully'}, 201
        return 500


@user_ns.route('/login')
class UserLogin(Resource):
    """`UserLogin` support post method to log in to an account."""

    @user_ns.doc('login_user')
    @user_ns.expect(user_login_model)
    def post(self):
        '''Login user'''
        username = request.json.get('username')
        password = request.json.get('password')
        if username in user_repo.get_name2id():
            user_id = user_repo.get_name2id()[username]
            if check_password_hash(
                user_repo.get_all_users()[user_id].passwrod, password
            ):
                access_token = create_access_token(identity=user_id)
                return {'access_token': access_token}, 200
        return {'message': 'Invalid username or password'}, 401


@user_ns.route('/login_info')
class LoginInfor(Resource):
    """
    `UserSignup` support get method to get current logged in account
        information, however, it is require the JWT login token.
    """

    @jwt_required()
    def get(self):
        '''Example route that requires login'''
        current_user_id = get_jwt_identity()
        user = user_repo.get_user_by_id(current_user_id)
        return {'logged_in_as': asdict(user)}, 200


@user_ns.route('/account/<int:user_id>')
class GetUser(Resource):
    """
    `getUser` provides Get method to get specific user
        with user's id(`id`)
    """

    def get(self, user_id):
        """Get user information with ID"""
        user = user_repo.get_user_by_id(user_id)
        if user:
            return {
                'id': user.user_id,
                'username': user.username,
                'email': user.email,
            }, 200
        return {'message': f'User with id={id} Not exists'}, 404


@user_ns.route('/account/')
class GetAllUsers(Resource):
    """
    `GetAllUsers` provides GET method to
        retrive all users's usernames, ids, and emails
    """

    def get(self):
        """Get all user information"""
        users = user_repo.get_all_users()

        res = [
            {
                'id': user_row.user_id,
                'username': user_row.username,
                'email': user_row.email,
            }
            for user_row in users.values()
        ]

        if res:
            return res, 200
        return 404
