from flask import Flask, render_template

app  = Flask("MyApp")

@app.route("/")
def hello():
    return "What's GOOD!"

@app.route("/idontexist")
def idontexist():
    return "I do exist now!"

@app.route("/connie")
def connie():
    return "My favourite dessert is ice cream!"

app.run(debug=True)
