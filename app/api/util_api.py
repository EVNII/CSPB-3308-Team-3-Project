"""
Module `app.api.util_api` defines Utilities's APIs,
typically support interfaces to query the status of
the whole server. And SHOULD NOT have any APIs needs
JWT.
"""

from flask_restx import Namespace, Resource
from app.database import Database
from app.repository import UserRepository
from app.constants import db_Connnect, isPostreSQL

util_ns = Namespace('util', description='Utlity\'s Quesring')

db = Database()
db.set_db_conn_str(db_Connnect, isPostreSQL)
user_repo = UserRepository(db_ins=db)


@util_ns.route('/user_count')
class UserCount(Resource):
    """`UserCount` support GET method to show the number of users"""

    @util_ns.doc('get the number of users')
    def get(self):
        '''Query User Counts'''
        return user_repo.get_users_counts()
