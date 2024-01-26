from data_structures.queue import Queue


def multi_bracket_validation(input_string):
    bracket_pairs = {"[":"]","{":"}","(": ")"}

    stack = []


    for char in input_string:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack or bracket_pairs[stack.pop()] != char:
                return False
            
    return not stack