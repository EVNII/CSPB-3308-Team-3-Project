"""Module `app.models` defines the models"""
from .db import db
from .user import User
from .score import Score

__all__ = ['db', 'User', 'Score']
