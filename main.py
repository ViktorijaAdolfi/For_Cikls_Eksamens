from flask import Flask, render_template, request, redirect
#from funkcijas import Hello

app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/tests')
def tests():
  return render_template("tests.html")

app.run(host='0.0.0.0', port=8080)