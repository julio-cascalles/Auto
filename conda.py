import os
import sys

class Conda:
    def __init__(self, env: str):
        if env not in self.env_list():
            self.create(env)
        self.activate(env)

    def env_list(self) -> list:
        lines = os.popen('conda env list').read().split('\n')[2:]
        return [d[0] for d in [c.split() for c in lines] if d]

    def activate(self, env: str):
        os.system('conda activate ' + env)

    def deactivate(self):
        os.system('conda deactivate')

    def create(self, env: str):
        if os.path.isfile(env):
            os.system('conda env create -f ' + env)
        else:
            os.system('conda create -n ' + env)
