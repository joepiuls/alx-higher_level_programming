#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        s = len(sentence), None
        return s
    s = len(sentence), sentence[0]
    return s
