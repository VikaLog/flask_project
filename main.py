from flask import Flask, render_template

app = Flask(__name__)


@app.route('/requirements/', methods=['GET'])
def requirements():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return f"<pre>{text}</pre><link rel =\"stylesheet\"href=\"content.html\">"
