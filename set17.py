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