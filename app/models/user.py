"""Defines the model of `user`"""

from dataclasses import dataclass
from datetime import datetime
from .db import db


@dataclass
class User(db.Model):
    """database model of user"""

    # pylint: disable=too-many-instance-attributes

    user_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    created: datetime = db.Column(db.DateTime, nullable=False)
    surname: str = db.Column(db.String(50), nullable=False)
    firstname: str = db.Column(db.String(50), nullable=False)
    active: bool = db.Column(db.Boolean, nullable=False, default=True)
    password = db.Column(db.Text, nullable=False)
    recovery_question: str = db.Column(db.Text)
    recovery_answer: str = db.Column(db.Text)
