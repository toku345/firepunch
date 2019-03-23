import requests
from datetime import timedelta


class GitRepository:
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, access_token, today):
        self.access_token = access_token
        self.today = today

    def change_commits_1_day_before(self):
        today = self.today.strftime("%Y-%m-%d")
        yesterday = (self.today - timedelta(days=1)).strftime("%Y-%m-%d")

        request_uri = \
            "%s/repos/toku345/firepunch/compare/master@{%s}...master@{%s}" % (
                self.GITHUB_API_URL, yesterday, today)

        params = {"access_token": self.access_token}
        r = requests.get(request_uri, params=params)
        return r.json()
