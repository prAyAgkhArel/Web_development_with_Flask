from flask import url_for, Flask, render_template, request
import requests
from post import Post
import smtplib
import os

#sender email connection
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))



post_objects = []
response = requests.get(url="https://api.npoint.io/6c9d0e80a9ae677ff1cf")
posts = response.json()
for post in posts:
    post_objects.append(Post(post['id'], post['title'], post['subtitle'], post['body']))


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', post_objects = post_objects)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    if request.method == "POST":
        data = request.form
        username = data["username"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        connection.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=email, msg=f"Subject: Hello {username}!\n\n I got your message:\n{message}! Thank you!")
        return render_template('contact.html', msg_sent = True)
    return render_template('contact.html', msg_sent= False)


@app.route('/post/<int:id>')
def post_page(id):
    for post in post_objects:
        if post.id == id:
            print(id)
            requested_post = post

    return render_template('post.html', post= requested_post)


if __name__ == "__main__":
    app.run(debug=True)

