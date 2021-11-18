from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/', methods =["POST", "GET"])
def insert_customer():
    # retrieve data from html inputs, then save to database
    customers = []
    return render_template('form.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)