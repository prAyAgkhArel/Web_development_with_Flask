#first web server using flask
from flask import Flask

app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function.
# / denotes our local ip address of the webpage(i.e in our computer not the actual web server)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"