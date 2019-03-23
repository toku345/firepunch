import os
from datetime import date
from firepunch.git_repository import GitRepository

def test_change_commits_1_day_before():
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    today = date(2019, 3, 22)

    git_repository = GitRepository(access_token, today)

    result = git_repository.change_commits_1_day_before()

    assert 1 == len(result["commits"])
