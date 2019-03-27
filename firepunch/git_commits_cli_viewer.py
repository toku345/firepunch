from datetime import timedelta
from firepunch.git_repository import GitRepository


class GitCommitsCliViewer:
    def __init__(self, repo_name, now, access_token):
        self.repo_name = repo_name
        self.now = now
        self.access_token = access_token

    def print_commits_1_day_before(self):
        def printer(commit):
            print("\n--------------")
            print(f"date: {commit['date']}")
            print(f"{commit['message']}")

        def print_header():
            print(f"{len(commits)} commits between {a_day_ago} and {self.now}.")

        def print_header_without_commits():
            print(f"No commits between {a_day_ago} and {self.now}.")

        a_day_ago = (self.now - timedelta(days=1)) + timedelta(seconds=1)
        commits = self.get_commits_until_now(since=a_day_ago)
        if not commits:
            print_header_without_commits()
        else:
            print_header()

        [printer(commit) for commit in commits]

    def get_commits_until_now(self, since):
        def filter(commit_response):
            return {
                "message": commit_response["commit"]["message"],
                "date": commit_response["commit"]["author"]["date"]
            }

        git_repository = \
            GitRepository(self.repo_name, self.access_token)
        commits_response = \
            git_repository.change_commits(since=since, until=self.now)
        return [filter(cr) for cr in commits_response]
