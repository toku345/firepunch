import os
from datetime import datetime
from firepunch.git_commits_cli_viewer import GitCommitsCliViewer
from firepunch.inquiry_period import InquiryPeriod


def test_commits_for_1_day():
    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    viewer = GitCommitsCliViewer(repo_name, inquiry_period, access_token)

    expected = \
        "1 commits between 2019-03-20 12:39:59 and 2019-03-21 12:39:58.\n" + \
        "------------------------\ndate: 2019-03-21T12:39:58Z\nInitial commit"

    assert expected == viewer.commit_summary()


def test_commits_for_1_day_with_no_result():
    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime.strptime("2019-03-20T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    viewer = GitCommitsCliViewer(repo_name, inquiry_period, access_token)

    expected = \
        "No commits between 2019-03-19 12:39:59 and 2019-03-20 12:39:58."

    assert expected == viewer.commit_summary()
