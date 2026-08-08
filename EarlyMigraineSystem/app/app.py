from flask import Flask, render_template
from backend.database import get_records

app = Flask(__name__)

@app.route('/')
def home():
    data = get_records()
    return render_template("index.html", records=data)

if __name__ == '__main__':
    app.run(debug=True)