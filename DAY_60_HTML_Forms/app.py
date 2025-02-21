from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def receive_data():
    if request.form.get('form') == "form2":
        name = request.form.get("username")
        password = request.form.get("password")
        return render_template('success.html', name=name, password=password)
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)