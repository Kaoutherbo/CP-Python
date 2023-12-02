# TASK 01

def duplicate_encode(word):
    word = word.lower()
    sentence = []
    for letter in word:
        if word.count(letter) > 1:
            sentence.append(")")
        else:
            sentence.append("(")
    return ''.join(sentence)

# --------------------------------------
# TASK 02

def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# ----------------------------------------
# TASK 03
def is_pangram(s):
    s = s.lower()
    uniq_chars = set(char for char in s if char.isalpha())
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    return  alphabets <= uniq_chars

# ----------------------------------------
# TASK 04
# The hashlib.md5() function is used to calculate the 
# MD5 hash of the PIN. The PIN, converted to bytes using encode(),
# is then hashed, and hexdigest() 
# is called to obtain the hexadecimal representation of the hash.

import hashlib
def crack(md5_hash):
    for pin in range(100000):
        pin_str = f"{pin:05d}" # added zeros if it the num deosn't conatin 5 digits
        hashed_pin = hashlib.md5(pin_str.encode()).hexdigest()
        
        if hashed_pin == md5_hash:
            return pin_str
        
# ---------------------------------------------
# TASK 05

def sort_array(source_array):
    sorted_odd = sorted([num for num in source_array if num % 2 != 0])
    newArr = []
    for num in range(len(source_array)):
        if source_array[num] % 2 == 0:
            newArr.append(source_array[num])
        else:
            newArr.append(sorted_odd.pop(0))
    return newArr


# ---------------------------------------------
# TASK 06

def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros
