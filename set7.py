# TASK 01 -----------------------------
# Implement the function unique_in_order which
# takes as argument a sequence and returns a
# list of items without any elements with the
# same value next to each other and preserving
# the original order of elements.
def unique_in_order(sequence):
    if not sequence:
        return []

    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)

    return result

# TASK 02 -----------------------------
# There is an array with some numbers.
# All numbers are equal except for one.

def find_uniq(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        
# TASK 03 -----------------------------
# In this kata you are required to,
# given a string, replace every letter
# with its position in the alphabet.
def alphabet_position(text):
    text = text.lower()
    resText = []
    for char in text:
        if char.isalpha():
            resText.append(str(ord(char) - ord('a') + 1))
    return ' '.join(resText)