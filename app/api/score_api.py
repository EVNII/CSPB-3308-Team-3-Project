"""
Module `app.api.util_api` defines Utilities's APIs,
typically support interfaces to query the status of
the whole server. And SHOULD NOT have any APIs needs
JWT.
"""
from io import BytesIO
from dataclasses import asdict
import json
from werkzeug.datastructures import FileStorage
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import send_file
from flask_restx import Namespace, Resource
from app.models import db, User, Score


score_ns = Namespace('score', description='Score\'s Quesring')

score_upload_parser = score_ns.parser()
score_upload_parser.add_argument('track_title', type=str, required=True)
score_upload_parser.add_argument('instrument', type=str, required=True)
score_upload_parser.add_argument('genre', type=str, required=True)
score_upload_parser.add_argument('price', type=str, required=False)
score_upload_parser.add_argument(
    'file', location='files', type=FileStorage, required=True
)


@score_ns.route('/upload')
@score_ns.expect(score_upload_parser)
class UploadeScore(Resource):
    """
    `UploadeScore` support POST method to upload pdf of a score

    JWT REQUIRED
    """

    # pylint: disable=unexpected-keyword-arg

    @score_ns.doc('upload pdf of a score')
    @jwt_required()
    def post(self):
        '''Query User Counts'''
        user_id = get_jwt_identity()

        args = score_upload_parser.parse_args()
        uploaded_file = args['file']

        if uploaded_file:
            new_score = Score(
                track_title=args['track_title'],
                instrument=args['instrument'],
                genre=args['genre'],
                price=args['price'] if args['price'] else 0,
                pdf=uploaded_file.read(),
                user_id=user_id,
            )
            db.session.add(new_score)
            db.session.commit()
            return 201

        return 500


@score_ns.route('/pdf/<int:score_id>')
class ScorePDF(Resource):
    """
    `ScorePDF` support GET method to retrive the pdf file of the score

    JWT REQUIRED
    """

    @score_ns.doc('get the pdf of a score')
    @jwt_required()
    def get(self, score_id):
        '''Query User Counts'''

        score = (
            db.session.query(Score).where(Score.score_id == score_id).first()
        )

        score.downloads += 1

        db.session.commit()

        if score:
            pdf_bytes = BytesIO()
            pdf_bytes.write(score.pdf)
            pdf_bytes.seek(0)

            return send_file(pdf_bytes, mimetype='application/pdf')

        return 404


@score_ns.route('/<int:score_id>')
class ScoreInfo(Resource):
    """
    `ScoreInfo` support GET method to retrive the information of a pdf
    """

    @score_ns.doc('get the infomation of a score')
    def get(self, score_id):
        '''Query Score's information'''

        score, author = (
            db.session.query(Score, User)
            .filter(Score.score_id == score_id)
            .join(User, User.user_id == Score.user_id)
            .first()
        )

        if score:
            return (
                json.loads(
                    json.dumps(
                        {'score': asdict(score), 'author': asdict(author)},
                        default=str,
                    )
                ),
                200,
            )

        return 404


@score_ns.route('/all/')
class GetAllScores(Resource):
    """
    `GetAllScores` provides GET method to
        retrive all score's track_title, genre, and etc.
    """

    def get(self):
        """Get all user information"""

        # pylint: disable=singleton-comparison

        scores = (
            db.session.query(
                Score.track_title,
                Score.genre,
                Score.instrument,
                Score.price,
                Score.score_id,
                Score.downloads,
                User.username,
                User.user_id,
            )
            .select_from(Score)
            .join(User, Score.user_id == User.user_id)
            .filter(User.active == True)  # noqa: E712
            .all()
        )

        print(scores[0].user_id)

        res = [score._asdict() for score in scores]

        if res:
            return json.loads(json.dumps(res, default=str)), 200
        return 404
