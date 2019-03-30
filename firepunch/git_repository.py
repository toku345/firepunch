import requests


class GitRepository:
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, repo_name, access_token):
        self.repo_name = repo_name
        self.access_token = access_token

    def change_commits(self, since, until):
        request_uri = f"{self.GITHUB_API_URL}/repos/{self.repo_name}/commits"
        params = {
            "access_token": self.access_token,
            "since": since.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "until": until.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        r = requests.get(request_uri, params=params)
        return r.json()
