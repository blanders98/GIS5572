from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_polygon_from_db():
    connection = psycopg2.connect(
        dbname="lab0",
        user="postgres",
        password="Cagenewschool417!",
        host="34.27.75.243",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT ST_AsGeoJSON(geom) FROM geometries LIMIT 1;")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0]

@app.route('/')
def welcome():
    response = "Welcome to my server!"
    return response

@app.route('/polygon', methods=['GET'])
def polygon():
    geojson = get_polygon_from_db()
    return jsonify(geojson)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
