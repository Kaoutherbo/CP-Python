

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


