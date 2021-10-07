from util.logging_setting import log_with_time
from src.dynamic_programming.fibonacci.input import n

def fib_dp(n):
    fib_numbers = [1, 1]
    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-2] + fib_numbers[i-1])
    return fib_numbers[n]

def fib_dp_spc_opt(n):
    # optimize the space used
    if n == 1:
        return 1
    n_1 = 1
    n_0 = 1
    for i in range(2, n+1):
        n_2 = n_1
        n_1 = n_0
        n_0 = n_2 + n_1
    return n_0

if __name__ == '__main__':
    result = log_with_time(lambda: fib_dp(n))
    print(f'fib_dp({n}) = {result}')

    result = log_with_time(lambda: fib_dp_spc_opt(n))
    print(f'fib_dp_spc_opt({n}) = {result}')

