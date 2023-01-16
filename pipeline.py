import os
from jira import Jira
from git import Git
from conda import Conda

OP_PROJECT = '-p'
OP_ENVIRON = '-e'
OP_FLAG_ST = '-f'
DESCR_OPTIONS = f"""
    {OP_PROJECT} = Project
    {OP_ENVIRON} = Environment
    {OP_FLAG_ST} = Flag ("start" OR "stop")
"""

SEL_FIRST = lambda jira: jira.issues[0]


def execute(params: list, select: callable=SEL_FIRST) -> str:
    args = {k: v for k, v in zip(params, params[1:]) if k.startswith('-')}
    project = args[OP_PROJECT]
    env_name = args.get(OP_ENVIRON, project)
    flag = args.get(OP_FLAG_ST)
    jira = Jira(
        url=os.environ['JIRA_URL'],
        user=os.environ['JIRA_USERNAME'],
        token=os.environ['JIRA_TOKEN'],
        project=project,
        status='"To Do"' if flag == 'start' else '"In Progress"'
    )
    if not jira.issues:
        return 'No issues found.'.rjust(50, '-')
    task = select(jira)
    conda = Conda(env_name)
    git = Git(env_name, os.environ['COMPANY_NAME'])
    git.checkout(task.key, check_branch=True)
    if flag == 'start':
        task.assign_to_me()
        task.start()
        git.pull()
    elif flag == 'end':
        task.end()
        git.commit(task.summary)
        git.push()
        conda.deactivate()
    return 'Sucess!'.center(50, '*')
