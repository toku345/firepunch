import requests


class SlackNotifier:
    SLACK_POST_MESSAGE_URL = "https://slack.com/api/chat.postMessage"

    def __init__(self, token, channel_name):
        self.token = token
        self.channel_name = channel_name

    def post(self, text):
        params = {
            "token": self.token,
            "channel": self.channel_name,
            "text": text,
            "unfurl_links": True
        }
        return requests.post(url=self.SLACK_POST_MESSAGE_URL, params=params)
