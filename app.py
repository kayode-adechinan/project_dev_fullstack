from flask import Flask, render_template, jsonify
from mysql.connector import connect

app = Flask(__name__)

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


db_conn = connect(
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
)

cursor = db_conn.cursor()

select_records_query = "SELECT id, latitude, longitude FROM  records"


coordinates = []


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/coordinates", methods=["GET"])
def get_tasks():
    cursor.execute(select_records_query)
    result = cursor.fetchall()
    for row in result:
        coordinates.append({"id": row[0], "latitude": row[1], "longitude": row[2]})
    return jsonify({"coordinates": coordinates})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
