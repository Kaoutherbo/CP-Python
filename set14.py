from itertools import permutations

def latest_clock(a, b, c, d):
    digits = [a, b, c, d]
    max_time = ""

    for h1, h2, m1, m2 in permutations(digits):
        hour = int(f"{h1}{h2}")
        minute = int(f"{m1}{m2}")

        if 0 <= hour < 24 and 0 <= minute < 60:
            current_time = f"{hour:02d}:{minute:02d}"
            max_time = max(max_time, current_time)

    return max_time


    """Function that return true if every element in an array 
    is an integer or a float with no decimals.also in an emty array ,
    and False  for every other inpu
    """

def is_int_array(arr):
    if arr is None or not hasattr(arr, '__iter__') or arr == '':
        return False  # Input is None or not iterable
    
    if arr == []: # empty array 
        return True
    
    for element in arr:
        if (type(element) != int and type(element) != float ) or element != int(element):
            return False
    return True
