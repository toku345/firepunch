import os
from datetime import datetime
from pytz import utc

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

    now = datetime(2019, 3, 21, 12, 39, 58, tzinfo=utc)
    inquiry_period = InquiryPeriod(until=now, days=1)

    client = GitCommitsSlackClient(repo_name=repo_name,
                                   inquiry_period=inquiry_period,
                                   access_token=access_token,
                                   slack_notifier=slack_notifier)

    client.post_commit_summary()

    expected_calls = [
        mocker.call("*[toku345/firepunch]*\n1 commits between 2019-03-20 21:39:59 and 2019-03-21 21:39:58."),  # noqa: E501
        mocker.call("https://github.com/toku345/firepunch/commit/421db6df5d6be3e7026ab2de1203f7d09a09d08f")    # noqa: E501
    ]
    slack_notifier.post.assert_has_calls(expected_calls)


def test_commits_for_1_day_with_no_result(mocker):
    token = "dummy_token"
    channel_name = "#channel_name"
    slack_notifier = SlackNotifier(token=token, channel_name=channel_name)
    slack_notifier.post = mocker.MagicMock()

    repo_name = "toku345/firepunch"
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    now = datetime(2019, 3, 20, 12, 39, 58, tzinfo=utc)
    inquiry_period = InquiryPeriod(until=now, days=1)

    client = GitCommitsSlackClient(repo_name=repo_name,
                                   inquiry_period=inquiry_period,
                                   access_token=access_token,
                                   slack_notifier=slack_notifier)

    client.post_commit_summary()

    expected_text = \
        "*[toku345/firepunch]*\n" + \
        "0 commits between 2019-03-19 21:39:59 and 2019-03-20 21:39:58."

    slack_notifier.post.assert_called_once_with(expected_text)
