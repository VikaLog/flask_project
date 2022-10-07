from flask import Flask, render_template, json
from faker import Faker
from pandas.io.json import to_json

fake = Faker()

app = Flask(__name__)


@app.route('/requirements/', methods=['GET'])
def requirements():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return f"<pre>{text}</pre><link rel =\"stylesheet\"href=\"content.html\">"


@app.route('/generate-users/count=<int:num>', methods=['GET'])
def gen_user(num):
    emails = []
    for i in range(num):
        i = fake.email()
        emails.append(i)
    return render_template("table.html", data=emails)
