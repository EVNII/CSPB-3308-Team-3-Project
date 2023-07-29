"""Defines the model of `user`"""

from dataclasses import dataclass


@dataclass
class User:
    """dataclass of user"""

    user_id: int
    username: str
    email: str
    passwrod: str
