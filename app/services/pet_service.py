import os
import pymysql
from dotenv import load_dotenv

# โหลดค่าต่าง ๆ จากไฟล์ .env
load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "happy_paw3"),
        port=int(os.getenv("DB_PORT", 3306)),
        cursorclass=pymysql.cursors.DictCursor
    )

def get_all_pets():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, type, breed, age, owner_name FROM pets")
            return cursor.fetchall()
    finally:
        connection.close()

def update_pet_owner(pet_id: int, new_owner: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE pets SET owner_name = %s WHERE id = %s",
                (new_owner, pet_id)
            )
            connection.commit()
            return True
    finally:
        connection.close()