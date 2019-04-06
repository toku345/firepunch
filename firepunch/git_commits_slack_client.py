from firepunch.git_repository import GitRepository


class GitCommitsSlackClient:
    def __init__(self, repo_name, inquiry_period,
                 access_token, slack_notifier):
        self.repo_name = repo_name
        self.since = inquiry_period.since
        self.until = inquiry_period.until
        self.access_token = access_token
        self.slack_notifier = slack_notifier

    def __header(self, commit_count):
        return (f"*[{self.repo_name}]*\n" +
                f"{commit_count} commits between {self.since} and {self.until}.")

    def __header_with_no_commit(self):
        return (f"*[{self.repo_name}]*\n" +
                f"No commits between {self.since} and {self.until}.")

    def __response_to_dict_list(self, commits_response):
        def format(commit):
            return [
                "------------------------",
                f"date: {commit['commit']['author']['date']}",
                f"{commit['commit']['message']}"
            ]
        return [sentence for c in commits_response for sentence in format(c)]

    def __get_commits_response(self):
        git_repository = \
            GitRepository(self.repo_name, self.access_token)

        return git_repository.retrieve_change_commits(since=self.since,
                                                      until=self.until)

    def post_commit_summary(self):
        commits_response = self.__get_commits_response()

        if not commits_response:
            header = self.__header_with_no_commit()
        else:
            header = self.__header(len(commits_response))

        sentences = [header] + self.__response_to_dict_list(commits_response)

        self.slack_notifier.post("\n".join(sentences))
