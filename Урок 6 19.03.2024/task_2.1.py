import sys
from task_2 import gen_num

arguments = list(map(int, sys.argv[1:4]))

low_limit, high_limit, tries = 1, 100, 10

if len(arguments) == 1:
    high_limit = arguments[0]
elif len(arguments) == 2:
    low_limit, high_limit = arguments
else:
    low_limit, high_limit, tries = arguments

print(gen_num(low_limit, high_limit, tries))