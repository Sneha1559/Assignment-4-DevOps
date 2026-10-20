import os
import pymysql
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "localdevpassword"),
        database=os.getenv("DB_NAME", "appdb"),
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return "Hello! My application is running inside Docker."

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/db-health")
def db_health():
    try:
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 AS result")
                result = cursor.fetchone()
            return {"status": "connected", "database_test": result["result"]}
        finally:
            connection.close()
    except Exception:
        app.logger.exception("Database connection failed")
        return {"status": "unavailable"}, 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
