from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps(URL)", validators=[DataRequired(),
                                                                            URL(message='Invalid url..')])
    opening_time = StringField("Opening Time e.g 8AM", validators=[DataRequired()])
    closing_time = StringField("Closing Time e.g 6:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[('☕', '☕'),
                                                          ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),
                                                          ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=[('✖️', '✖️'), ('💪', '💪'),
                                                               ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                                               ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')],
                              validators=[DataRequired()])

    power_availability = SelectField("Power Sucket Availability", choices=[('✖️', '✖️'), ('🔌', '🔌'),
                                                                           ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                                                           ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                                     validators=[DataRequired()])
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        dict_data = form.data
        selected_dict = {key: value for key, value in dict_data.items() if key not in ["submit", 'csrf_token']}
        to_list = list(selected_dict.values())
        with open("cafe-data.csv", "a", newline="\n", encoding="utf-8") as csv_file:
            csv_write = csv.writer(csv_file, delimiter=",")
            csv_write.writerow(to_list)

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
