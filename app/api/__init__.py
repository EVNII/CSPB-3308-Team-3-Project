"""Module`app.api` Defines API's `flask_restx.Namespace`s"""

from .user_api import user_ns
from .util_api import util_ns
from .score_api import score_ns

__all__ = ['user_ns', 'util_ns', 'score_ns']
