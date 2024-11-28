from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_email = "dipstha393@gmail.com"
password = "hkct tuav brka zmzv"

url = " https://api.npoint.io/35da79c1d7aa8df4f7b1"
blogs = requests.get(url).json()


@app.route("/")
def home():
    return render_template("index.html", all_blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data)
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dipeshsth00@gmail.com",
                            msg=email_message
                            )


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog in blogs:
        if blog['id'] == index:
            requested_post = blog
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
