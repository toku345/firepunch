import requests
from firepunch.slack_notifier import SlackNotifier


def test_post_slack(mocker):
    mocker.patch("requests.post")

    SlackNotifier().post(text="xxxxx")

    exptected_url = "http://hoge.com"
    expected_params = {
        "token": "dummy token",
        "channels": "dummy channel"
    }
    requests.post.assert_called_once_with(url=exptected_url,
                                          params=expected_params)
