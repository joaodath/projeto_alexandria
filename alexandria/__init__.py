import os

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

app.config.from_object('config')

from alexandria import run