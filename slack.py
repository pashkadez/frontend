import json
import sys
import random
import requests

from config import *


def slackChannel(data):
    if data.action.labeled == "bug":
        return SLACK_BUG
    elif data.action.labeled == "user-story":
        return SLACK_US
    if data.action.labeled == "test-case":
        return SLACK_TC

def dataToMessage(data):
    user = data.issue.user.login
    action = data.action

    return f"{user} {action} something in project issues"
    

def sendToSlack(data):
    if data.action.labeled:
        url = SLACK_URL
        message = dataToMessage(data)
        title = (f"New Incoming Message :zap:")
        slack_data = {
            "icon_emoji": ":satellite:",
            "channel" : slackChannel(data),
            "attachments": [
                {
                    "color": "#9733EE",
                    "fields": [
                        {
                            "title": title,
                            "value": message,
                            "short": "false",
                        }
                    ]
                }
            ]
        }
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
