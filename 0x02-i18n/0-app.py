#!/usr/bin/env python3
""" Modules for Babel flask"""

from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    """Welcome page"""
    return render_template('0-index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
