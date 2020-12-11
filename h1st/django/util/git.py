from git.exc import InvalidGitRepositoryError
from git.repo.base import Repo


def get_git_repo_head_commit_hash(path=None):
    try:
        repo = Repo(path=path,
                    search_parent_directories=True,
                    expand_vars=True)

    except InvalidGitRepositoryError:
        return

    return repo.head.commit.hexsha
