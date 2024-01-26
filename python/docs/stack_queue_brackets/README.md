# Stack, Queue, Brackets

This code defines a Python function __multi_bracket_validation__ which checks if brackets in a given string are correctly balanced and nested. It handles three types of __brackets:__ square brackets [], curly braces {}, and parentheses (). The function iterates through the input string, using a stack to keep track of opening brackets. When a closing bracket is encountered, the function ensures it matches the corresponding opening bracket. The function returns True if all brackets are properly matched and nested, and False otherwise. The time and space complexity of this function are both linear, O(n), where n is the length of the input string.

## Whiteboard Process
[White Board](./whiteboard.png)

## Approach & Efficiency 

__Time Complexity:__ O(n) - The function processes each character in the input string once.
__Space Complexity:__ O(n) - In the worst case, the stack might hold half of the characters in the string, proportional to its length.