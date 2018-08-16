from flask import Flask

from .models import Question, Answer, questions, answers

app = Flask(__name__)