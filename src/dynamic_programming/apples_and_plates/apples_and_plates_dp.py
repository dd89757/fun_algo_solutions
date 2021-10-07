from src.dynamic_programming.apples_and_plates.input import m, n

def put_apples_in_plates_dp(m, n):
    # m apples and n plates
    dp_status = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):  # if there're i plates
        if i == 0:  # no plate
            continue
        for j in range(m+1):  # if there're j apples
            if j == 0:  # no apple
                dp_status[i][j] = 1
            else:
                if i > j:  # if there're more plates than apples
                    dp_status[i][j] = dp_status[j][j]
                else:
                    # if there's empty plate, then exclude that plate
                    result_w_empty = dp_status[i-1][j]

                    # if there's no empty plate, then put 1 apple in each plate first
                    result_wo_empty = dp_status[i][j-i]

                    dp_status[i][j] = result_w_empty + result_wo_empty
    return dp_status[n][m]


if __name__ == '__main__':
    result = put_apples_in_plates_dp(m, n)
    print(result)
