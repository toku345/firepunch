from datetime import timedelta
from firepunch.git_repository import GitRepository
from firepunch.inquiry_period import InquiryPeriod


class GitCommitsCliViewer:
    def __init__(self, repo_name, now, access_token):
        self.repo_name = repo_name
        self.until = now
        self.access_token = access_token

    def print_commits_1_day_before(self):
        def printer(commit):
            print("\n--------------")
            print(f"date: {commit['date']}")
            print(f"{commit['message']}")

        def print_header():
            print(f"{len(commits)} commits between {since} and {self.until}.")

        def print_header_without_commits():
            print(f"No commits between {since} and {self.until}.")

        since, _until = InquiryPeriod(until=self.until).a_whole_day()
        commits = self.get_commits(since)

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
            git_repository.change_commits(since=since, until=self.until)
        return [filter(cr) for cr in commits_response]
