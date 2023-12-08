# TASK 01  ---------------------------------------------
def expanded_form(num):
    number = int(num)
    expnd_num = []
    position = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            expnd_num.append(str(digit * position))
        number //= 10
        position *= 10

    return ' + '.join(expnd_num[::-1])

# TASK 02 ----------------------------------------------
def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        odd_chars = text[1::2]
        even_chars = text[0::2]
        text = odd_chars + even_chars

    return text

def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    length = len(encrypted_text)
    half_length = length // 2

    for _ in range(n):
        odd_chars = encrypted_text[:half_length]
        even_chars = encrypted_text[half_length:]
        encrypted_text = ''.join(''.join(pair) for pair in zip(even_chars, odd_chars)) # zip make pairs (135 , 024) => (1, 0), (3, 2), (5, 4)

    return encrypted_text

# TASK 03 ----------------------------------------------