#adding style to text "bye" using decorators

from flask import Flask
app = Flask(__name__)

def underlined(function):
    def wrapper():
        content = function()
        return f'<u>{content}</u>'
    return wrapper
def make_bold(function):
    def wrapper():
        content = function()
        return f'<b>{content}</b>'
    return wrapper

def make_italic(function):
    def wrapper():
        content = function()
        return f'<em>{content}</em>'
    return wrapper

@app.route("/")
@underlined
@make_bold
@make_italic
def bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run(debug=True)