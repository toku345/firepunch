#!/usr/bin/env python3
import argparse
from datetime import datetime
import os

from firepunch.git_commits_cli_viewer import GitCommitsCliViewer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name",
                        help="GitHub repository name. e.g. toku345/firepunch")
    args = parser.parse_args()

    now = datetime.utcnow()
    github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    viewer = GitCommitsCliViewer(args.repo_name, now, github_access_token)
    viewer.print_commits_1_day_before()


if __name__ == '__main__':
    main()
