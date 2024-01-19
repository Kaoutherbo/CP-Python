


"""
    Description: he friends decided that they will implement a 
    problem if at least two of them are sure about the solution.
    Otherwise, the friends won't write the problem's solution.  
    
    team: Function that return the number of problems the 
    friends will implement on the contest.    
"""
def team(matrix, n, m):
    nbrSol = 0

    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i][j] == 1:
                count += 1
        if count >= 2:
            nbrSol += 1

    return nbrSol
