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


@app.route('/covid/interactivity', methods=['POST'])
def interaction() -> str:
    req = request.form.to_dict()
    payload = json.loads(req['payload'])
    action_type = payload['type'] # block_actions, view_submission, ...
    trigger_id = payload['trigger_id']
    action_value = payload['actions'][0]['value'] #get_covid_data, ...

    if action_value == 'get_covid_data': # button을 눌렀을 때
        for id, dict in payload['state']['values'].items():
            if dict.get('get-start-date'):
                start_date = dict['get-start-date']['selected_date']
            elif dict.get('get-end-date'):
                end_date = dict['get-end-date']['selected_date']

    result = {
        'start_date': start_date,
        'end_date': end_date
    }
    print(result)
    return 'ok'


@app.route('/covid', methods=['POST'])
def test():
    req = request.form.to_dict()
    print(req)
    request_text = req['text']
    body = generating_menu()
    result = {
        "response_type": "ephemeral",
        "text": "thread_test",
        "attachments": [
            {
                "text": f'{request_text}'
            }
        ]
    }
    return body, 200


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
