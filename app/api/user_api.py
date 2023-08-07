"""
Module `app.api.user_api` defines user relative APIs, such as
login/logout.
"""
import json
from dataclasses import asdict
from datetime import datetime
from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity
from app.models import db, User

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

user_info_full_parser = user_ns.parser()
user_info_full_parser.add_argument('username', type=str, required=False)
user_info_full_parser.add_argument('password', type=str, required=False)
user_info_full_parser.add_argument('surname', type=str, required=False)
user_info_full_parser.add_argument('firstname', type=str, required=False)
user_info_full_parser.add_argument('active', type=bool, required=False)
user_info_full_parser.add_argument(
    'recovery_question', type=str, required=False
)
user_info_full_parser.add_argument('recovery_answer', type=str, required=False)


@user_ns.route('/signup')
class UserSignup(Resource):
    """`UserSignup` support post method to register a new user."""

    @user_ns.doc('create_new_user')
    @user_ns.expect(user_login_model)
    def post(self):
        '''Create new user'''

        # pylint: disable=unexpected-keyword-arg

        username = request.json.get('username')
        password = request.json.get('password')

        user = db.session.query(User).filter_by(username=username).first()
        if user:
            return f"Username with {username} already exists", 500

        db.session.add(
            User(
                username=username,
                created=datetime.now(),
                surname="",
                firstname="",
                password=generate_password_hash(password),
            )
        )
        db.session.commit()

        return {'message': 'User created successfully'}, 201


@user_ns.route('/login')
class UserLogin(Resource):
    """`UserLogin` support post method to log in to an account."""

    @user_ns.doc('login_user')
    @user_ns.expect(user_login_model)
    def post(self):
        '''Login user'''
        username = request.json.get('username')
        password = request.json.get('password')

        user = db.session.query(User).filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.user_id)
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
        user = (
            db.session.query(User).filter_by(user_id=current_user_id).first()
        )
        return json.loads(json.dumps(asdict(user), default=str)), 200


@user_ns.route('/account/<int:user_id>')
@user_ns.doc(params={'user_id': 'An User\'s ID'})
class UserWithID(Resource):
    """
    `UserWithID` provides Get method to get specific user
        with user's id(`id`)
    """

    @jwt_required(optional=True)
    def get(self, user_id):
        """Get user information with ID"""
        current_user_id = get_jwt_identity()

        user = db.session.query(User).filter_by(user_id=user_id).first()
        if user:
            if current_user_id == user_id:
                resultdict = asdict(user)
                scores = [asdict(s) for s in user.scores]
                resultdict['score'] = scores
                return json.loads(json.dumps(resultdict, default=str)), 200
            resultdict = {'user_id': user.user_id, 'username': user.username}
            scores = [asdict(s) for s in user.scores]
            resultdict['score'] = scores
            return json.loads(json.dumps(resultdict, default=str)), 200
        return {'message': f'User with id={user_id} Not exists'}, 404

    @jwt_required()
    @user_ns.expect(user_info_full_parser)
    @user_ns.doc(responses={201: 'Success: No Content', 404: 'Not Found'})
    def put(self, user_id):
        """Update user information with ID"""
        current_user_id = get_jwt_identity()

        if user_id != current_user_id:
            return {
                'message': f'You cannot update user info with id={user_id}'
            }, 403

        user = db.session.query(User).filter_by(user_id=user_id).first()

        if user:
            args = user_info_full_parser.parse_args()
            if args['username']:
                user.username = args['username']
            if args['surname']:
                user.surname = args['surname']
            if args['firstname']:
                user.firstname = args['firstname']
            if args['active']:
                user.active = args['active']
            if args['password']:
                user.password = generate_password_hash(args['password'])
            if args['recovery_question']:
                user.recovery_question = args['recovery_question']
            if args['recovery_answer']:
                user.recovery_answer = args['recovery_answer']

            db.session.commit()

            return 201
        return "Not Found", 404


@user_ns.route('/account/')
class GetAllUsers(Resource):
    """
    `GetAllUsers` provides GET method to
        retrive all users's usernames, ids, and emails
    """

    def get(self):
        """Get all user information"""
        users = (
            db.session.query(User.user_id, User.username)
            .filter_by(active=True)
            .all()
        )

        res = [u._asdict() for u in users]

        if res:
            return res, 200
        return 404
