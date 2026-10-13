import os
import pymysql
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# สร้าง Database connection โดยใช้ PyMySQL
def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 2000)),
        user=os.getenv("DB_USER", "happyuser"),
        password=os.getenv("DB_PASSWORD", "happypassword"),
        database=os.getenv("DB_NAME", "happy_paw3"),
        cursorclass=pymysql.cursors.DictCursor
    )

# ทดสอบการเชื่อมต่อ
if __name__ == "__main__":
    try:
        connection = get_connection()
        print("Connected to MariaDB successfully!")
        connection.close()
    except Exception as e:
        print(f"Connection failed: {e}")