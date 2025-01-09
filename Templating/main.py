from flask import Flask, render_template
from post import Post
import requests
response = requests.get(url=" https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = response.json()
post_objects = []

for post in blog_posts:
    temp_post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(temp_post_obj)

app = Flask(__name__)

@app.route('/blog')
def show_allposts():
    return render_template("index.html", post_objects = post_objects)

@app.route('/post/<id>')
def read_post(id):
    for post in post_objects:
        if id == post.id:
            post_object = post
    return render_template("post.html", post = post_object)


if __name__ == "__main__":
    app.run(debug=True)
