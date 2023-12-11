# TASK 01 ----------------------------------------------
def something_acci(num_digits):
    a, b = 0, 1
    position = 1  
    while True:
        a, b = b, a + b
        position += 1

        if len(str(b)) >= num_digits:
            return position, len(str(b))


def cumulative_triangle(n):
    if n < 1 or n > 10000:
        return "Invalid input. n should be between 1 and 10,000."

    start_num = sum(range(1, n))

    row_sum = sum(range(start_num + 1, start_num + n + 1))

    return row_sum