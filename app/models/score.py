"""Defines the model of `score`"""

from dataclasses import dataclass
from .db import db


@dataclass
class Score(db.Model):
    """database model of score"""

    # pylint: disable=too-many-instance-attributes

    score_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_title: str = db.Column(db.String(50), nullable=False)
    instrument: str = db.Column(db.String(50), nullable=False)
    genre: str = db.Column(db.String(50), nullable=False)
    downloads: int = db.Column(db.Integer, nullable=False, default=0)
    price: str = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    pdf = db.Column(db.LargeBinary, nullable=False)

    user_id: int = db.Column(
        db.Integer, db.ForeignKey('user.user_id'), nullable=False
    )
