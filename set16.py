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
    
    
    