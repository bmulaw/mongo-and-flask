from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb://localhost:27017/form"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/', methods =["POST", "GET"])
def insert_film():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    db.form.insert_one(
        {'name': name, 
        'email': email,
        'phone': phone,
        'message': message
        })

    x   = [i for i in db.form.find()]
    return render_template('form.html', forms=x)

if __name__ == '__main__':
    app.run(debug=True)