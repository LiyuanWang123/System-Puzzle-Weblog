import datetime
import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def index():
    # Connect to database
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all_local GET requests
    sql_all = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'local\';"""
    cur.execute(sql_all)
    all_local = cur.fetchone()[0]
    
	# Get number of all_remote GET requests
    sql_all = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'remote\';"""
    cur.execute(sql_all)
    all_remote = cur.fetchone()[0]
	
    # Get number of all succesful_local requests
    sql_success = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'local\' AND status LIKE \'2__\';"""
    cur.execute(sql_success)
    success_local = cur.fetchone()[0]

	# Get number of all succesful_remote requests
    sql_success = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'remote\' AND status LIKE \'2__\';"""
    cur.execute(sql_success)
    success_remote = cur.fetchone()[0]
	
    # Determine rate if there was at least one request
    rate = "No entries yet!"
    if all != 0:
        rate1 = str(success_local / all_local)
        rate2 = str(success_remote / all_remote)
    return render_template('index.html', rate1 = rate1, rate2 = rate2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
