# TASK 01 ----------------------------------------------
def something_acci(num_digits):
    a, b = 0, 1
    position = 1  
    while True:
        a, b = b, a + b
        position += 1

        if len(str(b)) >= num_digits:
            return position, len(str(b))
