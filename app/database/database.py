"""
`Database` class

This class is a singleton wrapper around SQLite3 execute command ensuring
    thread safety.

Author: Yuzhou Shen

Last Edit: UTC+8 2023/7/22 10:20
"""
from typing import Optional, List
from threading import Lock

import sqlite3
import psycopg2

from app.utility import Singleton


class Database(metaclass=Singleton):
    """
    A singleton class for managing SQLite/PostgreSQL database operations in
        a thread-safe manner.

    # Example:
    ```python
    db = database()
    db.set_dbFile('file_path_to.db') #Must set up at least onece

    ...

    db2 = database() # No set_dbFile() any more, but the same object with db.
    ```

    """

    db_conn_str: str
    """The db File Path"""
    conn: Optional[sqlite3.Connection | psycopg2.extensions.connection]
    """Connection instance member"""
    _lock: Lock
    """Thread Lock to ensure the `conn` is thread safe."""
    is_postre_sql: bool
    """Indicatet the types of connection"""

    def __init__(self) -> None:
        """
        Constructor

        #Example:

        ```python
        db = Database() # Call it anywhere to get the same database instance.
        ```

        """
        self.db_conn_str = ""
        self.conn = None
        self._lock = Lock()
        self.is_postre_sql = False

    def set_db_conn_str(
        self, db_name: str, is_postre_sql: bool = False
    ) -> None:
        """
        set_db_conn_str() must setup once at least to declare the db file path

        #Args:
        - `db_name` (`str`): file path to the `.db` file.

        ```python
        db = Database() # Call it anywhere to get the same database instance.
        db.set_db_conn_str('file_path_to.db') # Recommend to call this function
            every time after get the Database instance.

        ...

        db2 = Database()
        db.set_dbFile('file_path_to.db')
        ```

        """

        if (db_name == self.db_conn_str) and (
            self.is_postre_sql == is_postre_sql
        ):
            return

        if self.conn:
            with self._lock:
                self.close()
                self.conn = None
        self.db_conn_str = db_name
        self.is_postre_sql = is_postre_sql

    def get_conn(self) -> sqlite3.Connection:
        """
        Get a sqlite3 Connection object from the database instance. **Not**
            intended for external use.

        ```python

        class Database:

            ...

            def a_method():
                with self._lock:
                    self.get_conn().anyfunction()
        ```
        """
        if self.conn is None:
            if self.is_postre_sql:
                self.conn = psycopg2.connect(self.db_conn_str)
            else:
                self.conn = sqlite3.connect(
                    self.db_conn_str, check_same_thread=False
                )
                self.conn.row_factory = sqlite3.Row
        return self.conn

    def close(self):
        """
        Close the SQLite3 connection. Should only be called when the database
            is no longer in use.
        """
        with self._lock:
            self.get_conn().close()

    def executescripts(self, sql_query: str) -> None:
        """
        Execute a block of SQL scripts.

        #Args:
        - `sql_query` (`str`): The SQL scripts to execute.

        #Examples:
        ```python
        db=Database()

        db.executescripts(\"\"\"
        CREATE TABLE ....
        \"\"\")

        ```
        """
        if self.is_postre_sql:
            with self._lock:
                cursor = self.get_conn().cursor()
                cursor.execute(sql_query)
                cursor.close()
                self.get_conn().commit()
        else:
            with self._lock:
                cursor = self.get_conn().executescript(sql_query)
                cursor.close()
                self.get_conn().commit()

    def execute(self, sql_query: str, parameters: tuple = ()) -> None:
        """
        Execute a single SQL statement with parameters.

        #Args:
        - `sql_query` (`str`): The SQL scripts to execute.
        -  `parameters` (`tuple`): The parameters for the SQL statement.

        #Examples:
        ```python
        db=Database()

        db.execute(\"\"\"
        INSERT INTO anytable VALUES
        (?, ?, ?)
        \"\"\", (value1, value2, value3))

        ```
        """

        if self.is_postre_sql:
            with self._lock:
                cursor = self.get_conn().cursor()
                cursor.execute(sql_query)
                cursor.close()
                self.get_conn().commit()
        else:
            with self._lock:
                cursor = self.get_conn().execute(sql_query, parameters)
                cursor.close()
                self.get_conn().commit()

    def execute_many(self, sql_query: str, parameters: tuple = ()) -> None:
        """
        Execute multiple SQL statements with parameters.

        #Args:
        - `sql_query` (`str`): The SQL scripts to execute.
        -  `parameters` (`tuple`): The parameters for the SQL statement.

        #Examples:
        ```python
        db=Database()

        db.execute_many(\"\"\"
        INSERT INTO anytable VALUES
        (?, ?, ?)
        \"\"\", ((value1, value2, value3)
                ,(value4, value5, value6)))

        ```
        """
        with self._lock:
            self.get_conn().executemany(sql_query, parameters)
            self.get_conn().commit()

    def fetch_all(
        self, sql_query: str, parameters: tuple = ()
    ) -> List[sqlite3.Row]:
        """
        Fetch all results from an SQL query with parameters.

        #Args:
        - `sql_query` (`str`): The SQL scripts to execute.
        -  `parameters` (`tuple`): The parameters for the SQL statement.

        #Returns:
        - `List[sqlite3.Row]` : A list of all rows returned by the query.

        #Examples:
        ```python
        db=Database()

        db.execute_many(\"\"\"
        SELECT * FROM anytable WHERE id=?
        \"\"\", (id1,))
        ```
        """
        if self.is_postre_sql:
            with self._lock:
                cursor = self.get_conn().cursor()
                cursor.execute(sql_query, parameters)
                rows = cursor.fetchall()
                cursor.close()
                self.get_conn().commit()
                return rows
        else:
            with self._lock:
                cursor = self.get_conn().execute(sql_query, parameters)
                rows = cursor.fetchall()
                cursor.close()
                self.get_conn().commit()
                return rows

    def fetch_one(self, sql_query: str, parameters: tuple = ()) -> sqlite3.Row:
        """
         Fetch one result from an SQL query with parameters.

        #Args:
         - `sql_query` (`str`): The SQL scripts to execute.
         -  `parameters` (`tuple`): The parameters for the SQL statement.

         #Returns:
         - `sqlite3.Row` : A list of all rows returned by the query.

         #Examples:
         ```python
         db=Database()

         db.execute(\"\"\"
         SELECT * FROM anytable WHERE id=?
         \"\"\", (id1,)) # Even there are rows of data
            in talbe satify the WHERE, only one result will be fetched.
         ```
        """
        if self.is_postre_sql:
            with self._lock:
                cursor = self.get_conn().cursor()
                cursor.execute(sql_query, parameters)
                row = cursor.fetchone()
                cursor.close()
                self.get_conn().commit()
                return row
        else:
            with self._lock:
                cursor = self.get_conn().execute(sql_query, parameters)
                row = cursor.fetchone()
                cursor.close()
                self.get_conn().commit()
                return row
