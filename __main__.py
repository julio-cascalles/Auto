import sys
from pipeline import execute


print('AUTO'.center(50, '-'))
print('-' * 50)
if len(sys.argv) < 3:
    print('Usage: python3 AUTO <project> <env> [start/end]')
else:
    params = [a for i, a in enumerate(sys.argv) if i > 0]
    print(execute(*params))
