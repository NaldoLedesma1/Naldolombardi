from flask import Flask, render_template

app = Flask (__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/abaout')
def abaout():
    return render_template("abaout.html")

if __name__ == '__main__':
    app.run(debug= True)
