import os
from datetime import datetime
from firepunch.git_repository import GitRepository

def test_change_commits_1_day_before():
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    today = datetime.strptime("2019-03-23T01:00:00Z", "%Y-%m-%dT%H:%M:%SZ")

    git_repository = GitRepository(access_token, today)

    result = git_repository.change_commits_1_day_before()
    assert 1 == len(result)
