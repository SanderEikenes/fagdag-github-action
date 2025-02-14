from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    latestCommitMessage = ""
    for commit in pull_request.get_commits():
        latestCommitMessage = commit.commit.message
    return latestCommitMessage

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    remote_file = repo.get_contents(file_path, ref=target_branch)
    with open(file_path) as f: 
        new_file_content = f.read()

    ##TODO use update_file from github.Repository to push the new file contents to the open PR 
    repo.update_file(
        remote_file.path,
        "",
        new_file_content,
        remote_file.sha,
        branch = target_branch,
        author = author
    )