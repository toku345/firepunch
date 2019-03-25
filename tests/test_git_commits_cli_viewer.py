import os
from datetime import datetime, timedelta
from firepunch.git_commits_cli_viewer import GitCommitsCliViewer


def test_commits_1_day_before():
    repo_name = "toku345/firepunch"

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    a_day_ago = (now - timedelta(days=1)) + timedelta(seconds=1)

    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    viewer = GitCommitsCliViewer(repo_name, now, access_token)

    expected = [
        {
            "message": "Initial commit",
            "date": "2019-03-21T12:39:58Z"
        }
    ]

    assert expected == viewer.get_commits_from_now(since=a_day_ago)
