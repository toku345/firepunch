#!/usr/bin/env python3
import argparse
from datetime import datetime
import os

from firepunch.git_commits_cli_viewer import GitCommitsCliViewer
from firepunch.inquiry_period import InquiryPeriod


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name",
                        help="GitHub repository name. e.g. toku345/firepunch")
    parser.add_argument("--days", type=int, default=1,
                        help="Number of days to investigate")
    return parser.parse_args()


def main():
    args = parse_args()
    now = datetime.utcnow()
    inquiry_period = InquiryPeriod(until=now, days=args.days)

    github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    viewer = GitCommitsCliViewer(args.repo_name, inquiry_period,
                                 github_access_token)
    print(viewer.commit_summary())


if __name__ == '__main__':
    main()
