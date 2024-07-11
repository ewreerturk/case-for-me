from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# PostgreSQL bağlantı bilgileri
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

# Redis bağlantı bilgileri
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))

# PostgreSQL bağlantısı oluşturma
def connect_to_postgres():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    return conn

# Redis bağlantısı oluşturma
def connect_to_redis():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    return r

# PostgreSQL'den string al ve Redis'te key'i arttır
def get_string_from_postgres():
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages ORDER BY id DESC LIMIT 1")  # Son eklenen mesajı al
    message = cur.fetchone()[0]
    conn.close()

    r = connect_to_redis()
    r.incr('message_count')  # Redis'te 'message_count' adlı key'i arttır

    return message

# Flask uygulaması
@app.route('/')
def get_message():
    message = get_string_from_postgres()
    return jsonify({'message': message})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)