def prime(start):
    if start == 1:
        return False
    for i in range(2, start):
        if start > 1 and start % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    start += 1
    for i in range(height):
        row = []
        for j in range(width):
            while True:
                if prime(start):
                    row.append(start)
                    start += 1
                    break
                start += 1
        result += " ".join("{:<2}".format(start) for start in row) + "\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7  11
    13 17 19 23 29
    """