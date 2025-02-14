from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    for commit in pull_request.get_commits():
        print(commit.commit.message)
        return commit.commit.message

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    remote_file = repo.get_contents(file_path, ref=target_branch)
    with open(file_path) as f: 
        new_file_content = f.read()

    ##TODO use update_file from github.Repository to push the new file contents to the open PR 

get_latest_commit_message(PullRequest)