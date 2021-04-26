def generate_nth_fibonacci(n):
    n = n - 1
    fibonacci = [0 for _ in range(n + 1)]
    fibonacci[0] = 1
    fibonacci[1] = 1
    for i in range(2, n+1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci


if __name__ == '__main__':
    print(generate_nth_fibonacci(100)[-1])
