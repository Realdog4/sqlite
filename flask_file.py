from flask import Flask, jsonify
import customers
import tracks

app = Flask(__name__)

@app.route('/')
def openPage():
    return "Hello!"

@app.errorhandler(404)
def page_not_found(error):
    return "Помилка, введіть коректну адресу!", 404



@app.route('/names/')
def viewName():
    con = customers.sqlite3.connect('tutorial.db')
    cur = con.execute("SELECT COUNT(DISTINCT name) AS unique_names FROM Customers;")
    result = cur.fetchall()
    con.close()
    return f"Кількість унікальних імен в таблиці Customers - {result}"


@app.route('/tracks/')
def viewTracks():
    con = tracks.sqlite3.connect('tutorial.db')
    cur = con.execute("SELECT COUNT(*) FROM tracks")
    result = cur.fetchall()
    con.close()
    return f"Кількість записів в таблиці Tracks - {result}"



@app.route('/tracks-sec/')
def viewTracksSeconds():
    con = tracks.sqlite3.connect('tutorial.db')
    cursor = con.execute("SELECT title, duration FROM tracks")
    result = [{'title': row[0], 'duration_sec': row[1]} for row in cursor.fetchall()]
    con.close()
    return jsonify({'tracks': result})

if __name__ == '__main__':
    app.run()
