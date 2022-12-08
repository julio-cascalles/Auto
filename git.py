from terminal import Terminal


URL_GITHUB = 'https://github.com/{repo}/{path}.git'


class Git(Terminal):
    def __init__(self, path: str, repo: str=''):
        if not self.path.exists(path): 
            self.clone(URL_GITHUB.format(repo=repo, path=path))
        self.chdir(path)

    def clone(self, url: str):
        self.system('git clone ' + url)

    def pull(self):
        self.system('git pull')

    def push(self):
        self.system('git push')

    def add(self, param: str):
        self.system(f'git add {param}')

    def commit(self, message: str):
        self.add('-all')
        self.system(f'git commit -m "{message}"')

    def checkout(self, branch: str, check_new_branch: bool=True):
        option = ''
        print('Branches atuais:\n{}'.format(
            self.branch()
        ), '-'*50)
        if check_new_branch and branch not in self.branch():
            option = '-b'
        command = 'git checkout {option} {branch}'.format(
            option=option,
            branch=branch
        )
        self.system(command)

    def branch(self):
        return self.popen('git branch').read().split('\n')

    def diff(self, extension='.py') -> dict:
        result = {}
        for line in self.popen('git diff').read().split('\n'):
            if line.endswith(extension):
                file_name = line.split('/')[-1]
            elif line and line[0] in '+-':
                result.setdefault(file_name, []).append(line)
        return result
