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
    Function that 
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

