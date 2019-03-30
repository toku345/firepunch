#!/usr/bin/env python3
import argparse
from datetime import datetime
import os

from firepunch.git_commits_cli_viewer import GitCommitsCliViewer
from firepunch.inquiry_period import InquiryPeriod


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name",
                        help="GitHub repository name. e.g. toku345/firepunch")
    args = parser.parse_args()

    now = datetime.utcnow()
    inquiry_period = InquiryPeriod(until=now, days=1)

    github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    viewer = GitCommitsCliViewer(args.repo_name, inquiry_period,
                                 github_access_token)
    print(viewer.commit_summary())


if __name__ == '__main__':
    main()
