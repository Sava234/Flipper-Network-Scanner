from flask import Flask, render_template
from scanner.parser import parse_log

app = Flask(__name__)

@app.route("/")
def index():
    results = parse_log("examples/sample_log.txt")
    return render_template("index.html", results=results)
