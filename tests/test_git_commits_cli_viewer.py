import os
from datetime import datetime, timedelta
from firepunch.git_commits_cli_viewer import GitCommitsCliViewer
from firepunch.inquiry_period import InquiryPeriod


def test_get_commits():
    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    since, until = InquiryPeriod(until=now).a_whole_day()

    viewer = GitCommitsCliViewer(repo_name, until, access_token)

    expected = [
        {
            "message": "Initial commit",
            "date": "2019-03-21T12:39:58Z"
        }
    ]

    assert expected == viewer.get_commits(since=since)


def test_commits_for_1_day():
    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    until = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    viewer = GitCommitsCliViewer(repo_name, until, access_token)

    expected = \
        "1 commits between 2019-03-20 12:39:59 and 2019-03-21 12:39:58.\n" + \
        "------------------------\ndate: 2019-03-21T12:39:58Z\nInitial commit"

    assert expected == viewer.commits_for_1_day()


def test_commits_for_1_day_no_commit():
    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    until = datetime.strptime("2019-03-20T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    viewer = GitCommitsCliViewer(repo_name, until, access_token)

    expected = \
        "No commits between 2019-03-19 12:39:59 and 2019-03-20 12:39:58."

    assert expected == viewer.commits_for_1_day()
