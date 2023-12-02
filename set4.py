# TASK 01

def expansion(matrix, n):
    size = len(matrix)
    
    for _ in range(n):
        expMat = [[0] * (size + 1) for _ in range(size + 1)]
        
        for i in range(size):
            for j in range(size):
                expMat[i][j] = matrix[i][j]
                expMat[size][j] += matrix[i][j]
                expMat[i][size] += matrix[i][j]
        
        expMat[size][size] = sum([matrix[i][j] for i in range(size) for j in range(size)])
        
        matrix = expMat
        size += 1
    
    return matrix


# TASK 02
def encrypt_this(text):
    words = text.split()

    encryptedTxt = []
    for word in words:
        if word:
            ch = str(ord(word[0]))
            if len(word) > 1:
                word = ch + word[-1] + word[2:-1] + word[1]
            else:
                word = ch
            
            encryptedTxt.append(word)


    return ' '.join(encryptedTxt)

# --------------------------------------------------
# TASK 03

def decipherThis(text):
    words = text.split()

    decryptedTxt = []
    for word in words:
        if word:
            number = ""
            i = 0
            while i < len(word) and word[i].isdigit():
                number += word[i]
                i += 1
                
            char = chr(int(number))

            rest = word[i:]
            if len(rest) > 1:
                decWord = char + rest[-1] + rest[1:-1] + rest[0]
            else:
                decWord = char

            decryptedTxt.append(decWord)

    return ' '.join(decryptedTxt)

# ------------------------------------------------------
# TASK 04

def find_outlier(integers):
    
    partCount = [0, 0]  
    for num in integers[:3]:
            partCount[num % 2] += 1
    part = 0 if  partCount[0] > partCount[1] else 1
    for num in integers:
        if num % 2 != part:
            return num
        