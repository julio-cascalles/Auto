import os

URL_GITHUB = 'https://github.com/{repo}/{path}.git'


class Git:
    def __init__(self, path: str, repo: str=''):
        if not os.path.exists(path): 
            self.clone(URL_GITHUB.format(repo=repo, path=path))
        os.chdir(path)

    def clone(self, url: str):
        os.system('git clone ' + url)

    def pull(self):
        os.system('git pull')

    def push(self):
        os.system('git push')

    def commit(self, message: str):
        os.system('git add . && git commit -m "' + message + '"')

    def checkout(self, branch: str, check_new_branch: bool=True):
        option = ''
        if check_new_branch and branch not in self.branch():
            option = '-b'
        command = 'git checkout {option} {branch}'.format(
            option=option,
            branch=branch
        )
        os.system(command)

    def branch(self):
        return os.popen('git branch').read().split('\n')

    def diff(self, extension='.py') -> dict:
        result = {}
        for line in os.popen('git diff').read().split('\n'):
            if line.endswith(extension):
                file_name = line.split('/')[-1]
            elif line and line[0] in '+-':
                result.setdefault(file_name, []).append(line)
        return result
