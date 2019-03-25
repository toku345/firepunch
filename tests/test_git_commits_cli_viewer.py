import os
from datetime import datetime
from firepunch.git_commits_cli_viewer import GitCommitsCliViewer


def test_commits_1_day_before():
    repo_name = "toku345/firepunch"
    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    viewer = GitCommitsCliViewer(repo_name, now, access_token)

    expected = [
        {
            "message": "Initial commit",
            "date": "2019-03-21T12:39:58Z"
        }
    ]

    assert expected == viewer.commits_1_day_before()
