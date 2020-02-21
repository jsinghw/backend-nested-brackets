#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Validate that various types of brackets are properly nested.
"""
__author__ = "jsinghw"

import sys


def valid_parentheses_star(string):
    cnt = 0
    pos = 0
    char = ''
    for char_n in string:
        if char == '(' and char_n == '*':
            cnt += 1
            char = ''
        elif char == '*' and char_n == ')':
            cnt -= 1
            char = ''
            if cnt < 0:
                return('NO ' + str(pos))
        else:
            pos += 1
            char = char_n
    if cnt == 0:
        return('YES')
    else:
        return('NO ' + str(pos - 1))


def valid_parentheses(string):
    cnt = 0
    pos = 0
    for char in string:
        if char == '(':
            cnt += 1
        if char == ')':
            cnt -= 1
        if cnt < 0:
            return('NO ' + str(pos))
        pos += 1
    if cnt == 0:
        return('YES')
    else:
        return('NO ' + str(pos))


def valid_square_bracket(string):
    cnt = 0
    pos = 0
    for char in string:
        if char == '[':
            cnt += 1
        if char == ']':
            cnt -= 1
        if cnt < 0:
            return('NO ' + str(pos))
        pos += 1
    if cnt == 0:
        return('YES')
    else:
        return('NO ' + str(pos))


def valid_curly_brace(string):
    cnt = 0
    pos = 0
    for char in string:
        if char == '{':
            cnt += 1
        if char == '}':
            cnt -= 1
        if cnt < 0:
            return('NO ' + str(pos))
        pos += 1
    if cnt == 0:
        return('YES')
    else:
        return('NO ' + str(pos))


def valid_angle_brace(string):
    cnt = 0
    pos = 0
    for char in string:
        if char == '<':
            cnt += 1
        if char == '>':
            cnt -= 1
        if cnt < 0:
            return('NO ' + str(pos))
        pos += 1
    if cnt == 0:
        return('YES')
    else:
        return('NO ' + str(pos))


def is_nested(line):
    """Validate a single input line for correct nesting"""
    if valid_parentheses_star(line) != 'YES':
        return(valid_parentheses_star(line))
    if valid_parentheses(line) != 'YES':
        return(valid_parentheses(line))
    if valid_square_bracket(line) != 'YES':
        return(valid_square_bracket(line))
    if valid_curly_brace(line) != 'YES':
        return(valid_curly_brace(line))
    if valid_angle_brace(line) != 'YES':
        return(valid_curly_brace(line))

    return('YES')


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open(args) as f:
        content = f.readlines()
    content = [x for x in content]
    for line in content:
        print(is_nested(line))


if __name__ == '__main__':
    main(sys.argv[1])
