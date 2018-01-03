from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jsw')
def jsw():
    return  render_template('jsw.html')


@app.route('/dit_mco')
def dit_mco():
    return render_template('dit_mco.html')


@app.route('/linebar')
def linebar():
    return render_template('linebar.html')


@app.route('/piebar')
def piebar():
    return render_template('piebar.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/prog")
def prog():
    render_template("prog.html")

if __name__ == '__main__':
    app.run(debug=True)
