import os

db_Connnect = os.getenv("MV_DB_CONNECT", 'MusicVerse.db')
isPostreSQL = (os.getenv('MV_DB_ISPOST', 'False') == 'True')