# TASK 01 ----------------------------------------------------------
def high(x):
    max_score = 0
    max_word = ""
    
    words = x.split()

    for word in words:
        word_score = sum(ord(char) - ord('a') + 1 for char in word) # sum of positions of each char
        
        if word_score > max_score:
            max_score = word_score
            max_word = word

    return max_word

# TASK 02 ------------------------------------------------------------
def encrypt(text, rule):
    
    encrypted_txt = ""

    for char in text:
        ascii_code = (ord(char) + rule) % 256 # use % to warp if the value exceeds 255
        encrypted_txt += chr(ascii_code)
        
    return encrypted_txt

# TASK 03 ------------------------------------------------------------

def queue_time(customers, n): # [2, 3, 10], 2
    arr = [0] * n  # arr = [0, 0]
    
    for time in customers:
        min_val = min(arr) # 0 # 0 # 2
        min_index = arr.index(min_val) # 0 # 1 # 2
        arr[min_index] += time  # [2, 0], # [2, 3] # [12, 3]

    return max(arr) # max[12, 3] =  12