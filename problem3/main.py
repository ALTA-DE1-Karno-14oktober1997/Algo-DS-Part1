def fibonacci(number):
    a=0
    b=1
    s=0
    for i in range (number):
        s=a+b
        b=a
        a=s
    return s

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144