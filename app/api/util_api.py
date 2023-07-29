"""
Module `app.api.util_api` defines Utilities's APIs,
typically support interfaces to query the status of
the whole server. And SHOULD NOT have any APIs needs
JWT.
"""

from flask_restx import Namespace, Resource
from app.models import db, User

util_ns = Namespace('util', description='Utlity\'s Quesring')


@util_ns.route('/user_count')
class UserCount(Resource):
    """`UserCount` support GET method to show the number of users"""

    @util_ns.doc('get the number of users')
    def get(self):
        '''Query User Counts'''
        counts = db.session.query(User.active).filter_by(active=True).count()
        return counts
