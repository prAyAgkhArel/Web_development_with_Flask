from flask import Flask, render_template
import requests

app = Flask(__name__)


parameters={
    "name": "Prayag"
}

response1 = requests.get(url="https://api.agify.io", params= parameters)
data1 = response1.json()
my_age = data1["age"]

response2 = requests.get(url="https://api.genderize.io", params=parameters)
data2 = response2.json()
gender = data2["gender"]


@app.route('/')
def get_home():
    return render_template("index.html")
@app.route('/guess/<name>')
def guess(name):
    return render_template("guess.html", name=name, age=my_age, gender=gender)

@app.route('/blog')
def get_blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("blog.html", blog_posts = data)

if __name__ == "__main__":
    app.run(debug=True)


