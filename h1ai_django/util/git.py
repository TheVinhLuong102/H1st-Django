from git.repo.base import Repo


def get_git_repo_head_commit_hash(path=None):
    return Repo(path=path,
                search_parent_directories=True,
                expand_vars=True) \
            .head.commit.hexsha
