# TASK 01
# function that checks if it is leap year or not
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year to check if it is a leap year or not : "))
if isLeapYear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# -----------------------------------------------------

# TASK 02
# function that counts the number of ones in 
# a number after tansforming it into binary representation
# Using bin() to get the binary representation and count () methods '1' characters
def countBits(num):
    return bin(num).count('1')

number = int(input("Enter a number : "))
print(f"The number of set bits in the binary representation of {number} is: {countBits(number)}")

# ---------------------------------------------------------
# TASK 03
# function that calculate the numer of persistence of 
# a given number. A number has persistence if the sum of
# its digits until reaching single digit numbers
def persistence(num):
    count = 0
    
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        
        num = product
        count += 1
    
    return count


number = int(input("Enter a number : "))
print(f"The multiplicative persistence of {number} is: {persistence(number)}")

# ----------------------------------------------------------------------------
# TASK 04
# function that transpose matrix
def transpose(matrix):
    transMat = list(map(list, zip(*matrix)))
    return transMat


originalMat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultMat = transpose(originalMat)

print("Original Matrix:")
for row in originalMat:
    print(row)

print("\nTransposed Matrix:")
for row in resultMat:
    print(row)

# -----------------------------------------------------
# TASK 05
# function that generate a string which start with hashtag 
# follows with capitalize words in the string
def generateHashtag(str):
    if not str or len(str.strip()) == 0: # strip method calculate the lenght of str after removing white sapce
        return False

    words = str.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        return False

    return hashtag


inputStr = input("Enter a sentence : ")
print(generateHashtag(inputStr))