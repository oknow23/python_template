#!/usr/bin/env python3
"""
python template
google docstring style:
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""
import os
import sys

global_variable1 = None
UPPER_CASE_CONSTANT = 'hello world'
global_variant2 = None


class PascalCaseClass:
    """ class docstring """

    def __init__(self, name):
        self.name = name

    def snake_case_member_func(self, snake_case_arg1):
        print(self.name, snake_case_arg1)


def multiple_return_func():
    """multiple return func

    Returns:
        string: result string
        bool: True if successful, False otherwise
    """
    return 'ret str', True


def tuple_return_func():
    """tuple return func

    Returns:
        {
            int: indicates tuple's first arg,
            boolean: indicates tuple's second arg,
        }
    """
    global_var2hello = 'hello world'
    print(global_var2hello)

    return (1, True)


def snake_case_func(arg1, arg2, arg3):
    """test func

    Args:
        arg1 (string): arg1 string
        arg2 (int): arg2 integer
        arg3 (tuple): arg3 tuple

    Returns:
        True if successful, False otherwise
    """
    if not isinstance(arg1, str) or not isinstance(arg2, int) or not isinstance(
            arg3, tuple):
        print('error occurred')
        return False

    print('arg1: {} arg2: {} arg3: {} global: {}'.format(
        arg1, arg2, arg3, global_variable1))
    return True


def main():
    global global_variable1

    global_variable1 = os.path.abspath(os.path.curdir)
    print(global_variable1)
    snake_case_func('this is string', 456, (1, 2))
    print("args passed in: '{}'".format(sys.argv))

    cl = PascalCaseClass('archer')
    cl.snake_case_member_func('hihi')


if __name__ == '__main__':
    main()
