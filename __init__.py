import json
import re
import ssl
import uuid

from flask import Flask
from slack import SlackAPI
from menu import generating_menu

from flask import Flask, request
from flask_classful import FlaskView, route
from slack_sdk import WebClient
from funcy import cached_property


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello() -> str:
    return "Hello Flask!"


# class TestView(FlaskView):
@app.route('/covid', methods=['POST'])
def test():
    req = request.form.to_dict()
    request_text = req['text']
    result = {
        "response_type": "in_channel",
        "text": "thread_test",
        "attachments": [
            {
                "text": f'{request_text}'
            }
        ]
    }
    return result, 200


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
