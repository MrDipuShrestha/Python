from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_database.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get('id')
    one_movie = Movie.query.get(movie_id)
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        if request.method == "POST":
            mid = request.args.get('movie_id')
            movie_to_update = Movie.query.get(mid)
            movie_to_update.rating = float(edit_form.rating.data)
            movie_to_update.review = edit_form.review.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('edit.html', movie=one_movie, form=edit_form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        if request.method == "POST":
            movie_title = add_form.title.data
            response = requests.get(
                "https://api.themoviedb.org/3/search/multi?include_adult=false&language=en-US&page=1",
                params={"api_key": "8c3889bd1568a0ae99214f31b249997e",
                        "query": movie_title})

            data = response.json()['results']
            return render_template('select.html', options=data)

    return render_template('add.html', form=add_form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"{"https://api.themoviedb.org/3/movie"}/{movie_api_id}"
        response = requests.get(movie_api_url,
                                params={"api_key": "8c3889bd1568a0ae99214f31b249997e", "language": "en-US"})
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
