from flask import Flask, render_template, request, redirect, flash
from db import *

app = Flask(__name__)

app.secret_key = b'asdasd'


@app.route("/")
def home():
    all_blogs = get_all_blogs()
    return render_template("index.html", blogs=all_blogs, title="HOME")


@app.route("/blogs/create", methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template("create.html",title="New Create")
    elif request.method == 'POST':
        save_blog(request.form)
        flash("BLOG CREATED")
        return redirect("/")



if __name__=="__main__":
    app.run()