from flask import Flask

class validate:

    validated = False
    def __init__(self):
        self.validated = False

validate = validate()
app = Flask(__name__)
from app import views


