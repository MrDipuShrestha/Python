# from flask import Flask
#
# app = Flask(__name__)
#
#
# # rendering html
# @app.route('/')
# def hello():
#     return ('<h1 style="text-align: center">Hello World</h1>'
#             '<p>This is the paragraph</p>'
#             # '<img src="" width=200> '
#             )
#
#
# # using variable path and coverting into other types
# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f"Hello {name}!, You are {number} years old."
#
#
# @app.route('/bye')
# def bye():
#     return 'Bye!'
#
#
# if __name__ == "__main__":
#
#     app.run(debug=True)


# advance decorator function

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticted_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@is_authenticted_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new post.")


new_user = User("Dipesh")
new_user.is_logged_in = True
create_blog_post(new_user)
