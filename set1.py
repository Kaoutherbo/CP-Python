# TASK 01
# function that removes vowels from an input text
def removeVowels(inputStr):
    vowels = "AEIOUaeiou"
    outStr = ""
    
    for char in inputStr:
        if char not in vowels:
            outStr += char
    
    return outStr

inputTxt = input("Enter a text: ")
outputTxt = removeVowels(inputTxt)
print(outputTxt)

# -----------------------------------------------------

# TASK 02
# function that returns true if the first argument
# passed in ends with the 2nd argument
def solution(str, end):
    endLen = len(end)
    suffix = str[-endLen:]
    return suffix == end
    
string = input("Enter the first string : ")
endStr = input("Enter the second string : ")

print(solution(string , endStr))  

# ------------------------------------------------------

# TASK 03
# function that takes a number and returns the 
# square of every digit of the number and concatenates them.
def squareDigit(num):
    result = 0
    mul = 1
    
    while num > 0:
        digit = num % 10
        sqr = digit ** 2
        result += sqr * mul
        mul *= 10
        num //= 10
    
    return result


number = int(input("Enter a number : "))
print(squareDigit(number))  

# -------------------------------------------------------

# TASK 04
# function that finds the high and low
# numbers in a given list of numbers

def HighAndLow(numStr):
    numList = list(map(int, numStr.split()))
    highNum = max(numList)
    lowNum = min(numList)
    return f"{highNum} {lowNum}"

inputNums =input("Enter list of numbers : ")
print(HighAndLow(inputNums))

# -------------------------------------------------------

# TASK 05 
# function that return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def getMiddle(word):
    length = len(word)
    if length % 2 == 0:
        middle = length // 2
        return word[middle - 1 : middle + 1]
    else:
        middle = length // 2
        return word[middle]

inputStr = input("Enter a word : ")
print(getMiddle(inputStr))

# ---------------------------------------------------------

# TASK 06
# function that  takes a list of non-negative 
# integers and strings and returns a new list 
# with the strings filtered out.

def fillter_list(str):
    result = []
    for item in str:
        if isinstance(item, int):
            result.append(item)
    
    return result_list
inputList = input("Enter a list : ")
print(fillter_list(inputList))

# -------------------------------------------------------

# TASK 07
from math import *

# function that determines if a number
# is a square number or not
 
def isSquareNum(num):
    if num < 0:
        return False
    else:
        root = int(sqrt(num))
        return root * root == num

inputNum = int(input("Enter a number : "))
print(isSquareNum(inputNum))

# --------------------------------------------

# TASK 08
def XO(str):
    count_x = str.lower().count('x')
    count_o = str.lower().count('o')
    return count_x == count_o


inputStr = input("Enter a string : ")
print(XO(inputStr))  

# ----------------------------------------------
# TASK 09
# function that capitalizes every word in a given sentence
# using title() function that returns a version of 
# the string where each word is titlecased.

def jadenCased(sentence):
    return sentence.title()

quote = input("Enter a sentence : ") 
print(jadenCased(quote))

# -----------------------------------------------

# TASK 10
# function that returns the compelement of given DNA sentence
# maketrans method returns a translation table that 
# maps each character in the first string ("ATCG") to 
# the corresponding character in the second string ("TAGC").
# this table can be used with the translate method to replace specified characters.

def complementaryDNA(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))

inputDNA = input("Enter the DNA : ")
print(f"{inputDNA} --> {complementaryDNA(inputDNA)}")  

# ------------------------------------------------

# TASK 11
# this function takes a sentence as input,
# splits it into words, reverses words
# with five or more letters, joins them
# back into a sentence, and then prints the result.


def spinWords(sentence):
    words = sentence.split()
    revdWords = []
    for word in words:
        if len(word) >= 5:
            revdWords.append(word[::-1]) 
        else:
            revdWords.append(word) 
    result = ' '.join(revdWords) 
    return result

inputStr = input("Enter a sentence : ")
print(spinWords(inputStr))