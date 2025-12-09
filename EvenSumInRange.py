for num in range(100, 201):
    temp = num
    sum_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        temp //= 10

    if sum_digits % 2 == 0:
        print(num)
