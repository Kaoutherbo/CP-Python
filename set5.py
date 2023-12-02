# TASK 01
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

arr = [1, 2, 3, 4, 3, 2, 1]
print(find_even_index(arr))  

# --------------------------------------------
# TASK 02
def dig_pow(n, p):
    sumNum = sum(pow(int(d), p + i) for i, d in enumerate(str(n)))
    
    k = 1
    while k * n < sumNum:
        k += 1
 
    if k * n == sumNum:
        return k 
    else:
        return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))

# ---------------------------------------------------------
# TASK 03
def likes(names):
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

print(likes([]))  
print(likes(["Kaouther"]))  
print(likes(["Kaouther", "Meriem"]))
print(likes(["Kaouther", "Meriem", "Yasmine"])) 
print(likes(["Kaouther", "Meriem", "Yasmine", "Adel"])) 

# ------------------------------------------------------------
# TASK 04

# order function that sorted a given sentence based on its number
# words.split() splits the input string into a list of words.
# lambda w: int(''.join(ch for ch in word if ch.isdigit())) is a key function that extracts the number from each word.
# sorted(words, key=...) sorts the words based on the extracted numbers.
# ' '.join(sorted(words, key=...)) joins the sorted words into a single string.


def order(words):
    if not words:
        return ""
    return ' '.join(sorted(words.split(), key=lambda word: int(''.join(ch for ch in word if ch.isdigit()))))


print(order("Mess2i Le1o T4he 3is GOAT5"))

# -------------------------------------------------------------------------
# TASK 05
def uniq(seq):
    if not seq:
        return []

    result = [seq[0]]
    for item in seq[1:]:
        if item != result[-1]:
            result.append(item)

    return result

print(["a", "a", "b", "b", "c", "a", "b", "c"])