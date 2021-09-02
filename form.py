from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/', methods =["GET", "POST"])
def form():
    if request.method == "POST":
        num = str(request.form.get('num'))
        name =  (request.form.get('name'))
        return name + ", " + num

    return render_template('form.html')


        


if __name__ == '__main__':
    app.run(debug=True)