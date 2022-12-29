from flask import Flask, request, render_template
import requests, os, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
