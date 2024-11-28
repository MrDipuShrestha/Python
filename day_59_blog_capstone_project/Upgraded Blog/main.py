from flask import Flask, render_template
import requests

app = Flask(__name__)

url = " https://api.npoint.io/35da79c1d7aa8df4f7b1"
blogs = requests.get(url).json()


@app.route("/")
def home():
    return render_template("index.html", all_blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog in blogs:
        if blog['id'] == index:
            requested_post = blog
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
