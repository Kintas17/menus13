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

@app.route('/p3')
def p3():
    return render_template('p3.html')

if __name__ == '__main__':
    app.run(debug=True)
