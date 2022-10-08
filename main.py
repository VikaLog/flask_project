from flask import Flask, render_template, json
from faker import Faker
import pandas as pd
import numpy as np

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


@app.route('/mean/', methods=['GET'])
def avg_metrics():
    df = pd.read_csv("hw.csv", sep=',')
    avg_height = round(np.mean(df[' "Height(Inches)"'])*2.54, 2)
    avg_weight = round(np.mean(df[' "Weight(Pounds)"']) * 0.45, 2)
    return f"avg_height = {avg_height} cm, avg_weight = {avg_weight} kg"
