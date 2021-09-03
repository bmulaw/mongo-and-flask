from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb://localhost:27017/movie"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/', methods =["POST"])
def insert_film():
    num = request.form.get('num')
    name = request.form.get('name')
    db.movie.insert_one(
        {'name': name, 
        'rating': num
        })
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)