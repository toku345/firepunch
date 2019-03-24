import os
from datetime import datetime
from firepunch.git_repository import GitRepository


# FIREPUNCH commits:
# - 2019-03-24Txx:xx:xxZ
# - 2019-03-22T01:25:52Z
# - 2019-03-21T12:42:30Z
# - 2019-03-21T12:39:58Z

def test_get_1_commit_call_at_just_commit_time():
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    git_repository = GitRepository(now, access_token)

    result = git_repository.change_commits_1_day_before()
    assert 1 == len(result)


def test_get_0_commit_call_at_after_whole_day():
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    now = datetime.strptime("2019-03-23T01:25:52Z", "%Y-%m-%dT%H:%M:%SZ")

    git_repository = GitRepository(now, access_token)

    result = git_repository.change_commits_1_day_before()
    assert 0 == len(result)
