import sys
from pipeline import (
    execute,
    OP_PROJECT,
    OP_ENVIRON,
    OP_FLAG_ST,
    START_ID, END_ID
)


print('AUTO'.center(50, '-'))
if len(sys.argv) < 3:
    print(
        'Usage: python AUTO {} <project> [{} <env>] [{} {}|{}]'.format(
            OP_PROJECT, OP_ENVIRON, OP_FLAG_ST, START_ID, END_ID
        )
    )
else:
    params = sys.argv
    print(execute({
        k: v for k, v in zip(params, params[1:]) if k.startswith('-')
    }))
print('-' * 50)
