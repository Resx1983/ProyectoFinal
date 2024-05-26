from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

db_file_path = os.path.join(os.path.dirname(__file__), "data/comments.json")

def save_comment(comments):
    with open(db_file_path, "w") as f:
        json.dump(comments, f, indent=4)
        
def load_comments():
    with open(db_file_path, "r") as f:
        return json.load(f)
    
def insert_comment():
    return load_comments()["comments"]

@app.route("/base", methods=["GET","POST"])
def base():
    
    if request.method == "POST":
        name = request.form["name"]
        comment = request.form["comment"]
        new_comment = {"name": name, "comment":comment}
        jsonfile = load_comments()
        jsonfile["comments"].append(new_comment)
        save_comment(jsonfile)
        return redirect(url_for("home"))
    jsonfile = load_comments() 
    return render_template("base.html", comments=jsonfile["comments"])

@app.route("/")
def home():
    return render_template("/home.html", comments=insert_comment())

@app.route("/comunidad")
def comunidad():
    
    return render_template("comunidad.html", comments=insert_comment())

if __name__ == "__main__":
    app.run(debug=True)