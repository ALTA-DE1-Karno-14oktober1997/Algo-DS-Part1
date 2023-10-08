def max_sequence(arr):
    total_maksimum = float('-inf')
    total_sementara = 0
    for i in arr:
        total_sementara += i
        if total_sementara > total_maksimum:
            total_maksimum = total_sementara
        if total_sementara < 0:
            total_sementara = 0
    return total_maksimum

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12