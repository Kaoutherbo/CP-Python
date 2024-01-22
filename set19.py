"""
    oddDivisor: Function that check if number has odd divisors greater 
    then 1 and return YES,otherwise return NO
"""

def oddDivisor(n):
    for i in range(2, n//2 + 1):
        if n % i == 0 and i % 2 != 0:
            return "YES"
    return "NO"

"""
    sale: Function that return the maximum sum of money that 
    Bob can earn, given that he can carry at most m TV sets.
"""

def sale(nums, m):
    nums.sort()  
    money = 0

    for num in nums:
        if num <= 0 and m > 0:
            money += abs(num)  
            m -= 1

    return money


# def candies(num):
    




"""
    newYearNumber: Function that return YES if the year can written with 2020 and 2021 
    and NO otherwise
"""
def newYearNumber(year):
    while(year > 2021):
        year -= 2020
    
    if year == 2021:
        return "YES"
    else:
        return "NO"
  
  
    """
    keyBoard: Function that return the new statement after fix it
    """
  
def keyBoard(pos, statement):
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    newStatement = []

    for letter in statement:
        if pos == "R":
            index = keyboard.find(letter) - 1
            newStatement.append(keyboard[index])
        elif pos == "L":
            index = keyboard.find(letter) + 1
            newStatement.append(keyboard[index])

    return "".join(newStatement)


"""
    multiplyby: Function that return he minimum number of moves needed to obtain 1 from n
    if it's possible to do that or -1 if it's impossible to obtain 1 from n
"""

def multiplyby(num):
    count = 0
    while num != 1:
        if num % 6 == 0:
            num //= 6
        elif num % 3 == 0:
            num *= 2
        else:
            return -1
        count += 1
    
    return count