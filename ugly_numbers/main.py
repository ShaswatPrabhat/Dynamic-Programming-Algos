def generate_nth_ugly_number(n):
    result_ugly_number_array = [0 for _ in range(n)]
    result_ugly_number_array[0] = 1
    multiple_2 = multiple_3 = multiple_5 = 0
    next_multiple_of_2 = result_ugly_number_array[multiple_2] * 2
    next_multiple_of_3 = result_ugly_number_array[multiple_3] * 3
    next_multiple_of_5 = result_ugly_number_array[multiple_5] * 5
    for i in range(1, n):
        next_ugly_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        result_ugly_number_array[i] = next_ugly_number
        if next_ugly_number % 2 == 0:
            multiple_2 += 1
            next_multiple_of_2 = result_ugly_number_array[multiple_2] * 2
        if next_ugly_number % 3 == 0:
            multiple_3 += 1
            next_multiple_of_3 = result_ugly_number_array[multiple_3] * 3
        if next_ugly_number % 5 == 0:
            multiple_5 += 1
            next_multiple_of_5 = result_ugly_number_array[multiple_5] * 5

    return result_ugly_number_array


if __name__ == '__main__':
    print(generate_nth_ugly_number(150)[-1])
