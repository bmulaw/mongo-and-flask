from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='template')

@app.route('/', methods =["POST", "GET"])
def insert_film():
    # retrieve data from html inputs, then save to database
    x = []
    return render_template('form.html', forms=x)

if __name__ == '__main__':
    app.run(debug=True)