import os
from datetime import datetime
from firepunch.git_commits_slack_client import GitCommitsSlackClient
from firepunch.inquiry_period import InquiryPeriod
from firepunch.slack_notifier import SlackNotifier


def test_commits_for_1_day(mocker):
    token = "dummy_token"
    channel_name = "#channel_name"
    slack_notifier = SlackNotifier(token=token, channel_name=channel_name)
    slack_notifier.post = mocker.MagicMock()

    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    client = GitCommitsSlackClient(repo_name=repo_name,
                                   inquiry_period=inquiry_period,
                                   access_token=access_token,
                                   slack_notifier=slack_notifier)

    client.post_commit_summary()

    expected_text = \
        "1 commits between 2019-03-20 12:39:59 and 2019-03-21 12:39:58.\n" + \
        "------------------------\ndate: 2019-03-21T12:39:58Z\nInitial commit"
    slack_notifier.post.assert_called_once_with(expected_text)


def test_commits_for_1_day_with_no_result(mocker):
    token = "dummy_token"
    channel_name = "#channel_name"
    slack_notifier = SlackNotifier(token=token, channel_name=channel_name)
    slack_notifier.post = mocker.MagicMock()

    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime.strptime("2019-03-20T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    client = GitCommitsSlackClient(repo_name=repo_name,
                                   inquiry_period=inquiry_period,
                                   access_token=access_token,
                                   slack_notifier=slack_notifier)

    client.post_commit_summary()

    expected_text = \
        "No commits between 2019-03-19 12:39:59 and 2019-03-20 12:39:58."

    slack_notifier.post.assert_called_once_with(expected_text)
