import sys
from pipeline import (
    execute,
    OP_PROJECT,
    OP_ENVIRON,
    OP_FLAG_ST,
)


print('AUTO'.center(50, '-'))
if len(sys.argv) < 3:
    print('Usage: python3 AUTO -p <project> [-e <env>] [-f start|end]')
    print(f"""
        {OP_PROJECT} = Project
        {OP_ENVIRON} = Environment
        {OP_FLAG_ST} = Flag ("start" OR "stop")
    """)
else:
    params = sys.argv
    print(execute({
        k: v for k, v in zip(params, params[1:]) if k.startswith('-')
    }))
print('-' * 50)
