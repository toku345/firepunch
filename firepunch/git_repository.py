import requests
from datetime import timedelta


class GitRepository:
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, access_token, today):
        self.access_token = access_token
        self.today = today

    def change_commits_1_day_before(self):
        yesterday = self.today - timedelta(days=1)
        request_uri = f"{self.GITHUB_API_URL}/repos/toku345/firepunch/commits"

        params = {
            "access_token": self.access_token,
            "since": yesterday.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "until": self.today.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        r = requests.get(request_uri, params=params)
        return r.json()
