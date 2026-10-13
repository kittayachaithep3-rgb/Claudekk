import pymysql
# 1. Import database connection
from app.database.connection import get_connection

# 2. Retrieve all pets from MariaDB
def get_all_pets():
    connection = get_connection()
    # หากget_connection() กำหนด DictCursor ไว้อยู่แล้ว สามารถใช้ connection.cursor() ได้เลย
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM pets ORDER BY id;")
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()