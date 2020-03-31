from flask import Flask, render_template

app = Flask('내 서버')


@app.route('/')
def home():
    return render_template('hw1.html')


@app.route('/music')
def music():
    return '<h1>Music</h1>'


@app.route('/music/top100')
def music100():
    return '<h1>Music Top 100</h1>'


app.run('0.0.0.0', port=5000, debug=True)
