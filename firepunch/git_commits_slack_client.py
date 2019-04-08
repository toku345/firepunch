from firepunch.git_repository import GitRepository
from pytz import timezone


class GitCommitsSlackClient:
    def __init__(self, repo_name, inquiry_period,
                 access_token, slack_notifier, tzlocal='Asia/Tokyo'):
        self.repo_name = repo_name
        self.since = inquiry_period.since
        self.until = inquiry_period.until
        self.access_token = access_token
        self.slack_notifier = slack_notifier
        self.timezone = timezone(tzlocal)

    def __header(self, commit_count):
        since = self.since.astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S")  # noqa: E501
        until = self.until.astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S")  # noqa: E501
        return (f"*[{self.repo_name}]*\n" +
                f"{commit_count} commits between {since} and {until}.")

    def __response_to_dict_list(self, commits_response):
        def format(commit):
            return [
                f"{commit['html_url']}"
            ]
        # flatten
        return [sentence for c in commits_response for sentence in format(c)]

    def __get_commits_response(self):
        git_repository = \
            GitRepository(self.repo_name, self.access_token)

        return git_repository.retrieve_change_commits(since=self.since,
                                                      until=self.until)

    def post_commit_summary(self):
        commits_response = self.__get_commits_response()
        header = self.__header(len(commits_response))

        sentences = [header] + self.__response_to_dict_list(commits_response)

        for sentence in sentences:
            self.slack_notifier.post(sentence)
