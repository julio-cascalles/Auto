import os

class Terminal:
    def system(self, command: str):
        print(f'\t{command}')
        os.system(command)

    def popen(self, command: str) -> list:
        print(f'\t{command}')
        return os.popen(command).read().split('\n')

    def chdir(self, path: str):
        os.chdir(path)

    def isfile(self, filename: str) -> bool:
        return os.path.isfile(filename)

    def exists(self, path: str) -> bool:
        return os.path.exists(path)
