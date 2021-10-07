from src.recursion.apples_and_plates.input import m, n

def put_apples_in_plates(m, n):
    # m apples and n plates
    if m == 0:  # no apple
        return 1
    if n == 0:  # no plate
        return 0

    # if plates are more than apples, we can put apples at most in n plates
    # it doesn't matter which plates we leave as empty, because all plates are the same
    if n > m:
        return put_apples_in_plates(m, m)

    # if there's empty plates, then we can remove the empty plate:
    result_w_empty = put_apples_in_plates(m, n-1)
    # if there's no empty plates, then we need to put 1 apple to all plates first:
    result_wo_empty = put_apples_in_plates(m-n, n)

    return result_w_empty + result_wo_empty


if __name__ == '__main__':
    result = put_apples_in_plates(m, n)
    print(result)
