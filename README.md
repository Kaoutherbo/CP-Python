# CP-Python

# TASK O2 from set 9:
* We use a stack to keep track of the opening braces.
* We iterate through each character in the input string.
* If the character is an opening brace ('(', '[', '{'), we push it onto the stack.
* If the character is a closing brace (')', ']', '}'), we check if the stack is empty or if the corresponding opening brace is at the top of the stack.
* If it's a valid match, we pop the opening brace from the stack.
* If it's not a valid match, or if there's an invalid character, we return False.
* After iterating through the entire string, if the stack is empty, it means all braces are matched, and we return True. Otherwise, we return False.

# TASK 01 from set 10:

* calculates the word_score by summing up the values 
* for each character in the word. It  uses a generator expression 
* with sum() to iterate over each character, calculate 
* its  score (based on its position in the alphabet), 
* and then sum all the scores.
* 
