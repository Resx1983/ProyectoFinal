from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/comunidad")
def comunidad():
    return render_template("comunidad.html")

if __name__ == "__main__":
    app.run(debug=True)