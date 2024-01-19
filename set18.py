


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


"""
    Description:  Rearrange the summans and print the 
    sum in such a way that Xenia can calculate the sum.
    
    helpfulMath: Function that return the new sum that Xenia can count.
"""


def helpfulMath(statement):
    numbers = list(map(int, statement.split("+")))
    sorted_numbers = sorted(numbers)
    new_statement = "+".join(map(str, sorted_numbers))
    return new_statement

"""
    Descritpion: Capitalization is writing a word with its first letter as 
    a capital letter. Your task is to capitalize the given word.

    wordCapitalize: Function that return the given word after capitalization.
"""

def wordCapitalize(word):
    return word[0].upper() + word[1:]

