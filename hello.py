from flask import Flask, render_template, request

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

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK - thanks so much, dude!"

app.run(debug=True)
