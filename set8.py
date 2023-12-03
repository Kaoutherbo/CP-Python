# TASK 01 --------------------------------
from math import sqrt

def sec_deg_solver(a, b, c):
    if a == 0:
        if b != 0 and c != 0:
            return f"It is a first degree equation. Solution: {round(-c / b, 10)}"
        elif b == 0 and c == 0:
            return "The equation is indeterminate"
        elif b == 0 and c != 0:
            return "Impossible situation. Wrong entries"
        elif b != 0 and c == 0:
            return f"It is a first degree equation. Solution: {round(0.0, 10)}"
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "There are no real solutions"
        elif d == 0:
            return f"It has one double solution: {round(-b / (2 * a), 10)}"
        else:
            s1, s2 = (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
            solutions = sorted([round(s1, 10), round(s2, 10)])
            return f"Two solutions: {solutions[0]}, {solutions[1]}"

# TASK 02 ------------------------------------------------------

def what_century(year):
    century = (int(year) - 1) // 100 + 1
    if 10 <= century % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th")
    return f"{century}{suffix}"

# TASK 03-----------------------------------------------------------
