from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def index():
    db_url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(db_url)
    cur = connection.cursor()
    cur.execute('SELECT * FROM estates;')
    estates = cur.fetchall()
    cur.close()
    connection.close()
    return render_template('index.html', estates=estates)