from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


if __name__ == '__main__':
    app.run(debug=True)
