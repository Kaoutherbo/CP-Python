# TASK 01  ---------------------------------------------
def expanded_form(num):
    number = int(num)
    expnd_num = []
    position = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            expnd_num.append(str(digit * position))
        number //= 10
        position *= 10

    return ' + '.join(expnd_num[::-1])

# TASK 02 ----------------------------------------------
