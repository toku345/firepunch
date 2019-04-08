import requests
from firepunch.slack_notifier import SlackNotifier


def test_post_slack(mocker):
    mocker.patch("requests.post")

    token = "dummy_token"
    channel_name = "#channel_name"
    text = \
        "1 commits between 2019-03-20 12:39:59 and 2019-03-21 12:39:58.\n" + \
        "------------------------\ndate: 2019-03-21T12:39:58Z\nInitial commit"

    SlackNotifier(token=token, channel_name=channel_name).post(text=text)

    exptected_url = SlackNotifier.SLACK_POST_MESSAGE_URL
    expected_params = {
        "token": token,
        "channel": channel_name,
        "text": text,
        "unfurl_links": True
    }
    requests.post.assert_called_once_with(url=exptected_url,
                                          params=expected_params)
