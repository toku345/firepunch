import requests


class SlackNotifier:
    def post(self, text):
        SLACK_FILES_UPLOAD_URL = "http://hoge.com"
        params = {
            "token": "dummy token",
            "channels": "dummy channel"
        }
        requests.post(url=SLACK_FILES_UPLOAD_URL, params=params)
