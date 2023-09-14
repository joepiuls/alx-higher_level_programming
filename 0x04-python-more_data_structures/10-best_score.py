#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
	return None
    max_score = None
    best_key = None
    for k, v in a_dictionary.items():
	if max_score is None or v > max_score:
	    max_score = value
	    best_key = k
    return best_key
