import json
import requests
import threading

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
    for key, value in payload.items():
        if key == 'response_url':
            response_url = value
    payload_type = payload['type']
    actions = payload['actions'][0]

    if payload_type == 'block_actions':
        if actions['type'] == 'button':
            for _, value in payload['state']['values'].items():
                if value.get('get-start-date'):
                    start_date = value['get-start-date']['selected_date']
                elif value.get('get-end-date'):
                    end_date = value['get-end-date']['selected_date']
                else:
                    result = {
                        "response_type": "ephemeral",
                        "text": "Press submit after picking both dates.",
                        "attachments": [
                            {
                                "text": f'pick date! :('
                            }
                        ]
                    }
                    requests.post(response_url, json=result)

        elif actions['type'] == 'datepicker':
            return 'ok', 200

        result = {
            "response_type": "ephemeral",
            "text": "complete",
            "attachments": [
                {
                    "text": f'from {start_date} to {end_date}'
                }
            ]
        }
        requests.post(response_url, json=result)
        return 'ok', 200


@app.route('/covid', methods=['POST'])
def test():
    req = request.form.to_dict()
    body = generating_menu()

    return body, 200


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
