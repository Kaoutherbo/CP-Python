def wetermelon(w): 
    if w %2 ==0:
        num = w/2
        if num % 2 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
        
def tooLongWord(word):
    if len(word) <= 10:
        return word
    else:
        first = word[0]
        last = word[-1]
        count = len(word) - 2  
        return f"{first}{count}{last}"
    
    
def beautifulMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    if matrix[2][2] == 1:
        return 0
    else:
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    count += abs(2 - i) + abs(2 - j)
                    break
    return count
        
def boyGirl(username):
    username = username.lower()
    distinct_chars = []
    for char in username:
        if char not in distinct_chars:
            distinct_chars.append(char)
    if len(distinct_chars) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


def find_zero_sum_groups(arr, n):
    result = []
    
    if len(arr) < n:
        return "No elements to combine"
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    current_combination = sorted([arr[i], arr[j], arr[k]])
                    if current_combination not in result:
                        result.append(current_combination)
    
    if len(result) == 1:
        return result[0] 
    elif result:
        return sorted(result)
    else:
        return "No combinations"
