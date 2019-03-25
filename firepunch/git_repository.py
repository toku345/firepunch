import requests
from datetime import timedelta


class GitRepository:
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, repo_name, now, access_token):
        self.repo_name = repo_name
        self.now = now
        self.access_token = access_token

    def change_commits_1_day_before(self):
        a_day_ago = (self.now - timedelta(days=1)) + timedelta(seconds=1)
        request_uri = \
            f"{self.GITHUB_API_URL}/{self.repo_name}/firepunch/commits"
        params = {
            "access_token": self.access_token,
            "since": a_day_ago.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "until": self.now.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        r = requests.get(request_uri, params=params)
        return r.json()
