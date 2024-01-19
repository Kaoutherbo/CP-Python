


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


""" 
    
"""

def stone(n, statement):
    count = 0
    for i in range(n-1):
          if  statement[i] == staement[i+1]:
              count += 1
    
    return count 


"""
    oddStream: Function that prints only the odd numbers from 1 to n    
"""

def oddStream(n):
    current_value = 1
    for _ in range(n):
        print(current_value)
        current_value += 2

"""
    evenStream: Function that prints only the even numbers from 0 to n    
"""
def evenStream(n):
    current_value = 0
    for _ in range(n):
        print(current_value)
        current_value += 2

"""
    print_from_stream: Function that get queries and prints 
    numbers correspending to the stream and number of stream 
"""

def print_from_stream(n, queries):
    for query in queries:
        parts = query.split()
        stream_name, n = parts[0], int(parts[1])
        if stream_name == "even":
            print_from_stream(n, evenStream)
        elif stream_name == "odd":
            print_from_stream(n, oddStream)
