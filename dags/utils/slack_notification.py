from airflow.models import Variable
import requests
import json

SLACKCONFIG = Variable.get("slack_webhook", deserialize_json=True)
SLACKUSER= 'Airflow'

def success(context=""):
    url= SLACKCONFIG["webhookurl"]
    requests.post(url, data = json.dumps({
        'username': SLACKUSER,
        'channel': SLACKCONFIG["channel"],
        'text':'処理に成功しました！！',
        'icon_emoji': ':sun_with_face:',
        'attachments': [{
            'title': 'Success: {}.{}.{}'.format(context['dag'], context['task'], context['execution_date']),
            "color": 'good'
            }]
        }))

def fail(context=""):
    url= SLACKCONFIG["webhookurl"]
    requests.post(url, data = json.dumps({
        'username': SLACKUSER,
        'channel': SLACKCONFIG["channel"],
        'text':'処理に失敗しました！！',
        'icon_emoji': ':ghost:',
        'attachments': [{
            'title': 'fail: {}.{}.{}'.format(context['dag'], context['task'], context['execution_date']),
            "color": 'danger'
            }]
        }))