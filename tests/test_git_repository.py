import os
from datetime import datetime, timedelta
from firepunch.git_repository import GitRepository


# FIREPUNCH commits:
# - 2019-03-24Txx:xx:xxZ
# - 2019-03-22T01:25:52Z
# - 2019-03-21T12:42:30Z
# - 2019-03-21T12:39:58Z

def test_get_1_commit_call_at_just_commit_time():
    repo_name = "toku345/firepunch"

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    a_day_ago = (now - timedelta(days=1)) + timedelta(seconds=1)

    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    git_repository = GitRepository(repo_name, access_token)

    result = git_repository.retrieve_change_commits(since=a_day_ago, until=now)
    assert 1 == len(result)


def test_get_0_commit_call_at_after_whole_day():
    repo_name = "toku345/firepunch"

    now = datetime.strptime("2019-03-23T01:25:52Z", "%Y-%m-%dT%H:%M:%SZ")
    a_day_ago = (now - timedelta(days=1)) + timedelta(seconds=1)

    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    git_repository = GitRepository(repo_name, access_token)

    result = git_repository.retrieve_change_commits(since=a_day_ago, until=now)
    assert 0 == len(result)
