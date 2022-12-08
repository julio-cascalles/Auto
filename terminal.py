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
