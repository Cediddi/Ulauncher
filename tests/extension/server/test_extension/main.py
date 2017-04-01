from __future__ import print_function
import sys
from time import sleep

for i in range(3):
    print('stdout check', file=sys.stdout)
    sleep(2)
    print('stderr check', file=sys.stderr)
