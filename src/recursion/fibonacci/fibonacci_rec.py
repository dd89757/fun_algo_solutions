from util.logging_setting import log_for_func, log_with_time
from src.recursion.fibonacci.input import n

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n-1) + fib(n-2)

def fib_w_memo(n):
    def fib_memo(n, memo):
        if n not in memo:
            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

    memo = {1: 1, 2: 1}
    return fib_memo(n, memo)


if __name__ == '__main__':
    # result = log_with_time(lambda: fib(n))
    # print(f'fib({n}) = {result}')

    result_w_memo = log_with_time(lambda: fib_w_memo(n))
    print(f'fib_w_memo({n}) = {result_w_memo}')

