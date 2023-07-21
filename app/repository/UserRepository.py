"""
`UserRepository()` class

Author: Yuzhou Shen

Last Edit: UTC+8 2023/7/21 21:25
"""

from app.database import Database
from threading import Lock
from app.models import User

class UserRepository:
    """
    The UserRepository class provides a convenient abstraction for performing CRUD operations on users.
    It also caches the results of some operations to improve performance.
    """
    user_cache = {}  # Cache for storing user data
    lock = Lock()  # Lock for thread-safety when modifying cache
        
    def __init__(self, db):
        self.db = db  # Database instance
        
    def get_all_users(self):
        """
        Retrieve all users. If the users have been fetched before, 
        return the cached result. Otherwise, query the database and cache the result.
        Usage: users = UserRepository().get_all_users()
        """
        all_users = self.db.fetch_all('SELECT * FROM users')
        with UserRepository.lock:
            for user_row in all_users:
                user = User(*user_row) if user_row else None
                UserRepository.user_cache[user.id] = user
        return UserRepository.user_cache
    
    def get_user_by_id(self, id):
        """
        Retrieve a user by username. If the user has been fetched before,
        return the cached result. Otherwise, query the database and cache the result.
        Usage: user = UserRepository().get_user_by_username('example')
        """
        if id in UserRepository.user_cache:
            return UserRepository.user_cache[id]

        user_row = self.db.fetch_one('SELECT * FROM users WHERE id = ?', (id,))
        user = User(*user_row) if user_row else None
        with UserRepository.lock:
            UserRepository.user_cache[user.id] = user
        return user

    def get_user_by_username(self, username):
        """
        Retrieve a user by username. If the user has been fetched before,
        return the cached result. Otherwise, query the database and cache the result.
        Usage: user = UserRepository().get_user_by_username('example')
        """
        for user in UserRepository.user_cache.values():
            if(user.username == username):
                return user

        user_row = self.db.fetch_one('SELECT * FROM users WHERE username = ?', (username,))
        user = User(*user_row) if user_row else None
        with UserRepository.lock:
            UserRepository.user_cache[user.id] = user
        return user

    def create_user(self, username, email, password):
        """
        Create a new user and clear the cache since the data has changed.
        Usage: UserRepository().create_user('example', 'example@example.com')
        """
        self.db.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        user = self.get_user_by_username(username)
        with UserRepository.lock:
            UserRepository.user_cache.clear()
        return user

    def update_user_email(self, id, new_email):
        """
        Update the email of an existing user and clear the cache since the data has changed.
        Usage: UserRepository().update_user_email('example', 'new_example@example.com')
        """
        self.db.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, id))
        with UserRepository.lock:
            UserRepository.user_cache.clear()

    def delete_user(self, username):
        """
        Delete an existing user and clear the cache since the data has changed.
        Usage: UserRepository().delete_user('example')
        """
        self.db.execute('DELETE FROM users WHERE username = ?', (username,))
        with UserRepository.lock:
            UserRepository.user_cache.clear()
