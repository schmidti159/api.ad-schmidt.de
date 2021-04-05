#!/usr/bin/env python3.6
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "nothing to be seen here, but thank you for dropping by"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9003, debug=True)
