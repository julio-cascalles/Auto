import os
from jira import Jira
from git import Git
from conda import Conda

OP_PROJECT = '-p'
OP_ENVIRON = '-e'
OP_FLAG_ST = '-f'

SEL_FIRST = lambda jira: jira.issues[0]
START_ID = 'start'


def execute(args: dict, select: callable=SEL_FIRST) -> str:
    project = args[OP_PROJECT]
    env_name = args.get(OP_ENVIRON, project)
    flag = args.get(OP_FLAG_ST)
    jira = Jira(
        url=os.environ['JIRA_URL'],
        user=os.environ['JIRA_USERNAME'],
        token=os.environ['JIRA_TOKEN'],
        assignee=None if flag == START_ID else 'currentUser()',
        project=project,
        status='"To Do"' if flag == START_ID else '"In Progress"'
    )
    if not jira.issues:
        return 'No issues found.'.rjust(50, '-')
    task = select(jira)
    conda = Conda(env_name)
    git = Git(env_name, os.environ['COMPANY_NAME'])
    git.checkout(task.key, check_branch=True)
    if flag == START_ID:
        task.assign_to_me()
        task.start()
        git.pull()
    elif flag == 'end':
        task.end()
        git.commit(task.summary)
        git.push()
        conda.deactivate()
    return 'Sucess!'.center(50, '*')
