from flask import Flask, render_template
import random
from datetime import datetime

year = datetime.now().year
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num= random_number, current_year= year, name="Prayag")


if __name__ == "__main__":
    app.run(debug=True)


