def generating_menu():
    actions = [{
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "button1",
            "emoji": True
        },
        "value": "get_covid_data"
    }]

    body = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "slackbot test for covid-alarm api."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": actions
            },
            {
                "type": "input",
                "element": {
                    "type": "datepicker",
                    "initial_date": "2021-12-20",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    },
                    "action_id": "get-start-date"
                },
                "label": {
                    "type": "plain_text",
                    "text": "From",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "datepicker",
                    "initial_date": "2021-12-20",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    },
                    "action_id": "get-end-date"
                },
                "label": {
                    "type": "plain_text",
                    "text": "To",
                    "emoji": True
                }
            },
        ]
    }
    return body
