# TASK 01 ----------------------------------------
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) - ord(chars[i]) > 1:
            return chr(ord(chars[i]) + 1)
        
# TASK 02 -----------------------------------------
def valid_braces(string):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False

    return not stack
