import logging
import sys

from src.enumeration.turn_off_lights.input import lights

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def turn_off_lights(lights):
    # enumerate the first column, once the status of the first column is fixed, then the next column is also fixed, ...
    # can also enumerate through rows, either is fine
    columns = len(lights[0])
    rows = len(lights)

    for status in range(0, 2**rows):
        # if there are 5 rows in one column, then we need 32 status
        found = True

        output = [[0 for _ in range(columns)] for _ in range(rows)]

        first_column = [int(c) for c in "{0:05b}".format(status)]
        logging.debug(f'first_column: {first_column}')

        # process first column
        for i in range(rows):
            output[i][0] = first_column[i]

        # process other columns depending on the lights and the assumed status
        for j in range(1, columns):
            # this is to make sure the lights in previous column are good
            for i in range(rows):
                # check what is the initial status and what is the operation in last row
                # if status is 1, then need to turn if off, so we assign 1 here
                # if status is 0, then nothing to do, so we assign 0 here
                output[i][j] = lights[i][j - 1] ^ output[i][j - 1]
                if i == 0:
                    output[i][j] = output[i][j] ^ output[i+1][j-1]
                elif i == rows - 1:
                    output[i][j] = output[i][j] ^ output[i-1][j-1]
                else:
                    output[i][j] = output[i][j] ^ output[i-1][j-1] ^ output[i+1][j-1]
                if j > 1:
                    output[i][j] = output[i][j] ^ output[i][j - 2]
            logging.debug(f'output: {output}')

        # compare last column
        for i in range(rows):
            check = lights[i][columns-1] ^ output[i][columns-1] ^ output[i][columns-2]
            if i == 0:
                check = check ^ output[i+1][columns-1]
            elif i == rows - 1:
                check = check ^ output[i-1][columns-1]
            else:
                check = check ^ output[i-1][columns-1] ^ output[i+1][columns-1]
            if check != 0:
                found = False
                break
        if found:
            return output

    return None


if __name__ == '__main__':
    result = turn_off_lights(lights)
    print(result)
    if result is None:
        print('No solution found!')
