' a test module '

__author__ = 'Laity'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private(name):
    return 'Hi %s ' % name


def _private1(name):
    return 'Hello %s' % name


def greet(name):
    if len(name) > 4:
        return _private(name)
    else:
        return _private1(name)
