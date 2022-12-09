import os
from jira import Jira
from git import Git
from conda import Conda


def execute(project: str, env: str='', flag: str='') -> str:
    company_name = os.environ['COMPANY_NAME']
    jira = Jira(
        url=os.environ['JIRA_URL'],
        user=os.environ['JIRA_USERNAME'],
        token=os.environ['JIRA_TOKEN'],
        project=project,
        status='"To Do"' if flag == 'start' else '"In Progress"'
    )
    if not jira.issues:
        return 'No issues found.'.rjust(50, '-')
    task = jira.issues[0]
    conda = Conda(env or project)
    git = Git(env or project, company_name)
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
