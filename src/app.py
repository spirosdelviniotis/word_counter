# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from models import Result
from models import *


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/<name>')
def hello_name(name='casper'):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
