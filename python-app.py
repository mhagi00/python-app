from flask import Flask
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'mysql',
}

def connect_to_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS test_database;")
    cursor.execute("USE test_database;")
    cursor.close()
    conn.close()

    return "Connected to the database and created `test_database` if it didn't exist."

@app.route('/')
def hello_world():
    db_status = connect_to_database()
    return f"Hello, world! {db_status}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
