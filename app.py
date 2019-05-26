from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/galo')
def galo():
    return render_template('galo.html')

@app.route('/space')
def space():
    return render_template('space.html')

if __name__ == '__main__':
    app.run(debug=True)
