"""
`Database()` class

Author: Yuzhou Shen

Last Edit: UTC+8 2023/7/21 21:25
"""

import sqlite3
from typing import Optional, List
from threading import Lock
from app.utility import Singleton


class Database(metaclass=Singleton):
    """A class wrapp excute from sqlite3, and it is singleton to ensure thread safety.
    
    # Example:
    ```python
    db = Database()
    db.set_dbFile('file_path_to.db') #Must set up at least onece
    
    ...
    
    db2 = Database() # No set_dbFile() any more, but the same object with db.
    ```
    
    """
    db_name: Optional[str]
    """The db File Path"""
    conn: Optional[sqlite3.Connection]
    """Connection instance member"""
    _lock: Lock
    """Thread Lock to ensure the `conn` is thread safe."""
    
    def __init__(self) -> None:
        """
        Constructor
        
        #Example:
        
        ```python
        db = Database() # Call it anywhere to get the same database instance.
        ```
        
        """
        self.db_name = None
        self.conn = None
        self._lock = Lock()

    def set_dbFile(self, db_name: str) -> None:
        """
        set_dbFile() must setup once at least to declare the db file path
        
        #Args:
        - `db_name` (`str`): file path to the `.db` file.
        
        ```python
        db = Database() # Call it anywhere to get the same database instance.
        db.set_dbFile('file_path_to.db') # Recommend to call this function every time after get the Database instance.
        
        ...
        
        db2 = Database()
        db.set_dbFile('file_path_to.db')
        ```
        
        """
        if not self.conn == None:
            self.close()
            self.conn = None
        self.db_name = db_name

    def get_conn(self) -> sqlite3.Connection:
        """
        Get sqlite3.Connection object from database instance, NOT RECOMMEND to manually call this function outside.
        
        It is usually to call it in member function with `_lock` to ensure the thread safety.
        
        ```python
        
        class Database:
        
            ...
            
            def a_method():
                with self._lock:
                    self.get_conn().anyfunction()
        ```
        """
        if self.conn == None:
            self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def close(self):
        """
        Close the sqlite3 connection, only close whent the database is not use anymore.
        """
        with self._lock:
            self.get_conn().close()

    def executescripts(self, sql_query: str) -> None:
        """
        Excute SQL scripts.
        
        #Args:
        - `sql_query` (`str`): SQL Query String
            
        #Examples:
        ```python
        db=Database()
        
        db.executescripts(\"\"\"
        CREATE TABLE ....
        \"\"\")
        
        ```
        """
        with self._lock:
            cursor = self.get_conn().executescript(sql_query)
            cursor.close()
            self.get_conn().commit()

    def execute(self, sql_query: str, parameters: tuple =()) -> None:
        """
        Excute ONE LINE of SQL scripts with parameters.
        
        #Args:
        - `sql_query` (`str`): SQL Query String
        -  `parameters` (`tuple`): parameter in tuple.
            
        #Examples:
        ```python
        db=Database()
        
        db.execute(\"\"\"
        INSERT INTO anytable VALUES
        (?, ?, ?)
        \"\"\", (value1, value2, value3))
        
        ```
        """
        
        with self._lock:
            cursor = self.get_conn().execute(sql_query, parameters)
            self.get_conn().commit()
        
    def execute_many(self, sql_query: str, parameters: tuple =()) -> None:
        """
        Excute MUTIPLE LINE of SQL scripts with parameters.
        
        #Args:
        - `sql_query` (`str`): SQL Query String
        -  `parameters` (`tuple`): parameter in tuple.
            
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

    def fetch_all(self, sql_query: str, parameters: tuple =()) -> List[sqlite3.Row]:
        """
        Fetch ALL Result FROM SQL scripts with parameters.
        
        #Args:
        - `sql_query` (`str`): SQL Query String
        -  `parameters` (`tuple`): parameter in tuple.
            
        #Examples:
        ```python
        db=Database()
        
        db.execute_many(\"\"\"
        SELECT * FROM anytable WHERE id=?
        \"\"\", (id1,))
        ```
        """
        with self._lock:
            cursor = self.get_conn().execute(sql_query, parameters)
            rows = cursor.fetchall()
            cursor.close()
            return rows

    def fetch_one(self, sql_query: str, parameters: tuple =()) -> sqlite3.Row:
        """
        Fetch only One Result FROM SQL scripts with parameters.
        
        #Args:
        - `sql_query` (`str`): SQL Query String
        -  `parameters` (`tuple`): parameter in tuple.
            
        #Examples:
        ```python
        db=Database()
        
        db.execute(\"\"\"
        SELECT * FROM anytable WHERE id=?
        \"\"\", (id1,)) # Even there are rows of data in talbe satify the WHERE, only one result will be fetched.
        ```
        """
        with self._lock:
            cursor = self.get_conn().execute(sql_query, parameters)
            row = cursor.fetchone()
            cursor.close()
            return row


