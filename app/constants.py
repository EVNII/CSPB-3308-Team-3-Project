"""File `app.constants` Defines Global Constants"""

import os

db_Connnect = os.getenv("MV_DB_CONNECT", 'sqlite:///MusicVerse.db')
