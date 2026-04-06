import os

CSV_PATH     = os.getenv("CSV_PATH")
QUESTDB_HOST = os.getenv("QUESTDB_HOST")
QUESTDB_PORT = int(os.getenv("QUESTDB_PORT"))
TABLE_NAME   = os.getenv("TABLE_NAME")