import sys
from pipeline import execute, DESCR_OPTIONS


print('AUTO'.center(50, '-'))
if len(sys.argv) < 3:
    print('Usage: python3 AUTO -p <project> [-e <env>] [-f start|end]')
    print(DESCR_OPTIONS)
else:
    params = sys.argv
    print(execute({
        k: v for k, v in zip(params, params[1:]) if k.startswith('-')
    }))
print('-' * 50)
