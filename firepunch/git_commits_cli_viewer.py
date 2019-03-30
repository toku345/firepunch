from datetime import timedelta
from firepunch.git_repository import GitRepository
from firepunch.inquiry_period import InquiryPeriod


class GitCommitsCliViewer:
    def __init__(self, repo_name, until, access_token):
        self.repo_name = repo_name
        self.until = until
        self.access_token = access_token

    def __header(self, since, commits):
        return f"{len(commits)} commits between {since} and {self.until}."

    def __header_without_commits(self, since):
        return f"No commits between {since} and {self.until}."

    def __format_commits(self, commits):
        def format(commit):
            return [
                "------------------------",
                f"date: {commit['date']}",
                f"{commit['message']}"
            ]

        formated_commits = \
            [sentence for commit in commits for sentence in format(commit)]
        return formated_commits

    def commits_for_1_day(self):
        since, _until = InquiryPeriod(until=self.until).a_whole_day()
        commits = self.get_commits(since)

        if not commits:
            header = self.__header_without_commits(since)
        else:
            header = self.__header(since, commits)

        sentences = [header] + self.__format_commits(commits)

        return "\n".join(sentences)

    def get_commits(self, since):
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
