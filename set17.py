""" 
    Function to find the number of participants 
    who advance to the next round 
"""
def nextRound(n,k, nums):
    count = 0
    
    for i in range(n):
        if nums[i] >= nums[k-1] and nums[i] > 0:
            count += 1
            
    return count

"""
    Description: Operation ++ increases the value of variable x by 1.
                 Operation -- decreases the value of variable x by 1
                 
    Function that return the final value of x.
"""
def bitPlus(n, statements):
    x = 0

    for statement in statements:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1

    return x

""" 
    Description : You are given a rectangular board of M × N squares. 
    Also you are given an unlimited number of standard 
    domino pieces of 2 × 1 squares. You are allowed to rotate the pieces.
    
    dominoPiling : Function that find the maximal number of dominoes, which can be placed.
"""
def dominoPiling(n, m):
    num = n*m
    return num // 2 

"""
    Description: The strings consist of uppercase and lowercase Latin letters.
    Now Petya wants to compare those two strings lexicographically. 
    The letters' case does not matter, that is an uppercase letter is 
    considered equivalent to the corresponding lowercase letter 
    
    petyaString : Function that return "-1" If the first string is less 
    than the second one, and "1" If the second string is less than the first on, 
    otherwaise return "0" (equal strings)
"""   
def petyaString(statement1, statement2):
    statement1 = statement1.lower()
    statement2 = statement2.lower()

    for letter1, letter2 in zip(statement1, statement2):
        if letter1 < letter2:
            return -1
        elif letter1 > letter2:
            return 1

    return 0
