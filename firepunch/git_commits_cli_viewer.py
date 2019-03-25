from firepunch.git_repository import GitRepository


class GitCommitsCliViewer:
    def __init__(self, repo_name, now, access_token):
        self.repo_name = repo_name
        self.now = now
        self.access_token = access_token

    def print_commits_1_day_before(self):
        print(self.commits_1_day_before())

    def commits_1_day_before(self):
        git_repository = \
            GitRepository(self.repo_name, self.now, self.access_token)

        def filter(commit_response):
            return {
                "message": commit_response["commit"]["message"],
                "date": commit_response["commit"]["author"]["date"]
            }

        commits_response = git_repository.change_commits_1_day_before()
        return [filter(cr) for cr in commits_response]
