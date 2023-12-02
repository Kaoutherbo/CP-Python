# function that returns the sum of the
# two lowest numbers in a list in python
def sum_of_two_lowest_numbers(nums):
    nums.sort()
    return sum(nums[:2])

# take input as a list of numbers
inputNums = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(sum_of_two_lowest_numbers(inputNums))



# function that counts the number of errors
# (characters not in the range 'a' to 'm')
# Return the error rate as a string
def printer_error(s):
    error_count = 0
    for char in s:
        if char > 'm':
            error_count += 1
    return f"{error_count}/{len(s)}"
    
    
sentence = input("Enter a text : ")
print(printer_error(sentence))  



# function that checks if the PIN is
# either 4 or 6 digits and consists only of digits
def isValidPin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

inputPin = input("Enter a number : ")
print(f"{inputPin} --> {isValidPin(inputPin)}") 


# function that that adds two numbers together
# and returns their sum in binary. The conversion
# can be done before, or after the addition.

def sumBinary(num1, num2):
    sumB = num1 + num2
    return toBinary(sumB)


# a recursion function that convert a decimal number 
# into its presentation in binary
def toBinary(num):
    if num == 0:
        return "0"
    else:
        return toBinary(num // 2) + str(num % 2)
    
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
print(f"{number1} + {number2} = {number1 + number2} in decimal or {sumBinary(number1, number2)} in binary")

# function that checks the triangle inequality theorem
def isTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

num1 = int(input("Enter first side : "))
num2 = int(input("Enter secind side : "))
num3 = int(input("Enter third side : "))
print(isTriangle(num1, num2, num3)) 



# function that accepts an array of integers, and returns
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
def isSortedArr(arr):
    if sorted(arr) == arr:
        return "yes, ascending"
    elif sorted(arr, reverse = True) == arr:
        return "yes, descending"
    else:
        return "no"


print(isSortedArr([1, 2, 3, 4]))      


# function that return an array containing the numbers from 1 to num
# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
def fizzbuzz(num):
    result = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

number = int(input("Enter a number : "))
print(fizzbuzz(number))


def toCamelCase(s):
    words = s.replace('-', '_').split('_')
    return words[0] + ''.join(word.title() for word in words[1:])

inputTxt = input("Enter a text : ")
print(toCamelCase(inputTxt))

# function that works basically like a Fibonacci,
# but summing the last 3 (instead of 2) numbers
# of the sequence to generate the next

def tribonacci(sequenceArr, size):
    if size == 0:
        return []
    elif size <= 3:
        return sequenceArr[:size]
    else:
        tribonacciSeq = sequenceArr.copy()  
        for i in range(3, size):
            nextElement = sum(tribonacciSeq[-3:])
            tribonacciSeq.append(nextElement)
    
    return tribonacciSeq

sequenceArr = [1, 1, 1]
size = int(input("Enter the number of sequence : "))
print(tribonacci(sequenceArr, size))


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