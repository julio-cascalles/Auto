from terminal import Terminal


URL_GITHUB = 'https://github.com/{repo}/{path}.git'


class Git(Terminal):
    def __init__(self, path: str, repo: str=''):
        if not self.exists(path): 
            self.clone(URL_GITHUB.format(repo=repo, path=path))
        self.chdir(path)
        self.new_branch = ''

    def clone(self, url: str):
        self.system('git clone ' + url)

    def pull(self):
        self.system('git pull')

    def push(self):
        option = ''
        if self.new_branch:
            option = f' --set-upstream origin {self.new_branch}'
        self.system('git push'+option)

    def add(self, param: str):
        self.system(f'git add {param}')

    def commit(self, message: str, add_all: bool = True):
        if add_all:
            self.add('--all')
        self.system(f'git commit -m "{message}"')

    def checkout(self, branch: str, check_branch: bool=True):
        option = ''
        if check_branch and branch not in self.branch():
            option = '-b'
            self.new_branch = branch
        command = f'git checkout {option} {branch}'
        self.system(command)

    def branch(self) -> list:
        return [
            b.replace('*', '').strip()
            for b in self.popen('git branch') if b
        ]

    def diff(self, extension='.py') -> dict:
        result = {}
        for line in self.popen('git diff'):
            if line.endswith(extension):
                file_name = line.split('/')[-1]
            elif line and line[0] in '+-':
                result.setdefault(file_name, []).append(line)
        return result
