"""
`UserRepository()` class

Author: Yuzhou Shen

Last Edit: UTC+8 2023/7/21 21:25
"""
from typing import Dict
from threading import Lock
from app.database import Database
from app.models import User


class UserRepository:
    """
    The UserRepository class provides a convenient abstraction for performing
        CRUD operations on users.
    It also caches the results of some operations to improve performance.
    """

    user_cache: Dict[int, User] = {}
    """Cache for storing user data"""
    user_name2id: Dict[str, int] = {}
    """Cache for mapping username to userid"""
    lock: Lock = Lock()
    """Lock for thread-safety when modifying cache"""
    db_ins: Database
    """Database instance"""

    def __init__(self, db_ins: Database):
        self.db_ins = db_ins

        if db_ins.is_postre_sql:
            db_ins.executescripts(
                """
            CREATE TABLE IF NOT EXISTS Users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(45) UNIQUE NOT NULL,
            email VARCHAR(128),
            password TEXT NOT NULL
        );
        """
            )
        else:
            db_ins.executescripts(
                """
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(45) UNIQUE NOT NULL,
                email VARCHAR(128),
                password TEXT NOT NULL
            );
            """
            )

    def get_all_users(self) -> Dict[int, User]:
        """
        Retrieve all users. If the users have been fetched before,
        return the cached result. Otherwise, query the database and
            cache the result.
        Usage: users = UserRepository().get_all_users()
        """

        if self.user_cache and self.user_name2id:
            return self.user_cache

        all_users = self.db_ins.fetch_all('SELECT * FROM users')
        print(all_users)
        with self.lock:
            for user_row in all_users:
                user = User(*user_row) if user_row else None
                if user:
                    self.user_cache[user.user_id] = user
                    self.user_name2id[user.username] = user.user_id
        return self.user_cache

    def get_name2id(self) -> Dict[str, int]:
        """get name2id dict"""

        if self.user_cache and self.user_name2id:
            return self.user_name2id

        all_users = self.db_ins.fetch_all('SELECT * FROM users')
        with self.lock:
            if all_users:
                for user_row in all_users:
                    user = User(*user_row) if user_row else None
                    if user:
                        self.user_cache[user.user_id] = user
                        self.user_name2id[user.username] = user.user_id

        return self.user_name2id

    def get_user_by_id(self, user_id):
        """
        Retrieve a user by username. If the user has been fetched before,
        return the cached result. Otherwise, query the database and cache
            the result.
        Usage: user = UserRepository().get_user_by_username('example')
        """
        if user_id in UserRepository.user_cache:
            return UserRepository.user_cache[user_id]

        if self.db_ins.is_PostreSQL:
            user_row = self.db_ins.fetch_one(
                f"SELECT * FROM users WHERE id = '{user_id}'"
            )
        else:
            user_row = self.db_ins.fetch_one(
                'SELECT * FROM users WHERE id = ?', (user_id,)
            )
        user = User(*user_row) if user_row else None
        if user:
            with UserRepository.lock:
                UserRepository.user_cache[user.user_id] = user
                self.user_name2id[user.username] = user.user_id
        return user

    def get_user_by_username(self, username):
        """
        Retrieve a user by username. If the user has been fetched before,
            return the cached result. Otherwise,
            query the database and cache the result.
        Usage: user = UserRepository().get_user_by_username('example')
        """
        if username in self.user_name2id:
            user_id = self.user_name2id[username]
            return self.user_cache[user_id]

        if self.db_ins.is_PostreSQL:
            user_row = self.db_ins.fetch_one(
                f"SELECT * FROM users WHERE username = '{username}'"
            )
        else:
            user_row = self.db_ins.fetch_one(
                'SELECT * FROM users WHERE username = ?', (username,)
            )
        user = User(*user_row) if user_row else None

        if user:
            with self.lock:
                self.user_name2id[user.username] = user.user_id
                self.user_cache[user.user_id] = user

        return user

    def create_user(self, username, email, password):
        """
        Create a new user and clear the cache since the data has changed.
        Usage: UserRepository().create_user('example', 'example@example.com')
        """
        if not isinstance(username, str):
            raise TypeError('username should be "str" type.')
        if not isinstance(email, str):
            raise TypeError('email should be "str" type.')
        if not isinstance(password, str):
            raise TypeError('password should be "str" type.')

        if self.db_ins.is_PostreSQL:
            self.db_ins.execute(
                f"""
                    INSERT INTO users (username, email, password)
                        VALUES ('{username}', '{email}', '{password}');
                """
            )
        else:
            self.db_ins.execute(
                """INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)""",
                (username, email, password),
            )
        user = self.get_user_by_username(username)
        with self.lock:
            self.user_cache.clear()
            self.user_name2id.clear()
        return user

    def update_user_email(self, user_id, new_email):
        """
        Update the email of an existing user and clear the cache since the
            data has changed.
        Usage:
            ```python
            UserRepository().update_user_email('example',
                'new_example@example.com')
            ```
        """
        self.db_ins.execute(
            'UPDATE users SET email = ? WHERE id = ?', (new_email, user_id)
        )
        with self.lock:
            self.user_cache.clear()
            self.user_name2id.clear()

    def get_users_counts(self) -> int:
        """
        Get the number of users.
        Usage: UserRepository().get_users_counts()
        """
        res = self.db_ins.fetch_one('SELECT COUNT(*) FROM users;')
        if not self.db_ins.is_postre_sql:
            user_count = int(res['COUNT(*)'])
            return user_count
        return -1

    def delete_user(self, username):
        """
        Delete an existing user and clear the cache since the data has changed.
        Usage: UserRepository().delete_user('example')
        """
        self.db_ins.execute(
            'DELETE FROM users WHERE username = ?', (username,)
        )
        with self.lock:
            self.user_cache.clear()
            self.user_name2id.clear()
