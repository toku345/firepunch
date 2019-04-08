#!/usr/bin/env python3
import argparse
from datetime import datetime
from pytz import utc
import os

from firepunch.inquiry_period import InquiryPeriod
from firepunch.git_commits_cli_client import GitCommitsCliClient
from firepunch.git_commits_slack_client import GitCommitsSlackClient
from firepunch.slack_notifier import SlackNotifier


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name",
                        help="GitHub repository name. e.g. toku345/firepunch")
    parser.add_argument("--days", type=int, default=1,
                        help="Number of days to investigate")
    parser.add_argument("--output-to", metavar="output_to", default="stdout",
                        help="Output to `stdout` or `slack`. (default: slack)")
    parser.add_argument("--slack-channel", metavar="slack_channel",
                        help="Slack channel name. e.g. general")
    parser.add_argument("--tzlocal", default="Asia/Tokyo",
                        help="Display date & time in `tzlocal`")
    return parser.parse_args()


def main():
    args = parse_args()
    now = datetime.now(tz=utc)
    inquiry_period = InquiryPeriod(until=now, days=args.days)

    github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    if args.output_to == 'slack':
        slack_token = os.getenv("SLACK_TOKEN")
        notifier = SlackNotifier(token=slack_token,
                                 channel_name=args.slack_channel)
        client = GitCommitsSlackClient(args.repo_name, inquiry_period,
                                       github_access_token, notifier,
                                       args.tzlocal)
        client.post_commit_summary()
        print("OK!")
    else:
        client = GitCommitsCliClient(args.repo_name, inquiry_period,
                                     github_access_token)
        print(client.commit_summary())


if __name__ == '__main__':
    main()
