from terminal import Terminal


class Conda(Terminal):
    def __init__(self, env: str=''):
        if not env:
            return
        if env not in self.env_list():
            self.create(env)
        self.activate(env)

    def env_list(self) -> list:
        lines = self.popen('conda env list')[2:]
        return [d[0] for d in [c.split() for c in lines] if d]

    def activate(self, env: str):
        self.system('conda activate ' + env)

    def deactivate(self):
        self.system('conda deactivate')

    def create(self, env: str):
        if self.exists(env):
            self.system('conda env create -f ' + env)
        else:
            self.system('conda create -n ' + env)
