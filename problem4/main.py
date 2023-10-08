def prime(start):
    if start ==1 :
            return False
    for i in range (2,start):
        if start>1 and start%i==0 :
            return False
    return True

def prima_setelah_start(start):
    while not prime(start):
        start += 1
    return start

def generate_primes_grid(width, height, start):
    result = prima_setelah_start(start - 1)  # Menggunakan bilangan prima sebelumnya
    for i in range(height):
        for j in range(width):
            result = prima_setelah_start(result + 1)  # Menggunakan bilangan prima berikutnya
            print(result, end="\t")
        print()

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """