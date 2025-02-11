from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db",
        port="5432"
    )
    return conn

@app.route('/api/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT message FROM test;')
    data = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"message": data[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
