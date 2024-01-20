

def oddDivisor(n):
    for i in range(2, n//2 + 1):
        if n % i == 0 and i % 2 != 0:
            return "YES"
    return "NO"

