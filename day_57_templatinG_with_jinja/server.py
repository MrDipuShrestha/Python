from flask import Flask, render_template
import random, requests, datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    response_gender.raise_for_status()
    data = response_gender.json()
    person_gender = data["gender"]

    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    response_age.raise_for_status()
    data = response_age.json()

    person_age = data["age"]
    return render_template("guess.html", name=name, age=person_age, gender=person_gender)


if __name__ == "__main__":
    app.run(debug=True)
