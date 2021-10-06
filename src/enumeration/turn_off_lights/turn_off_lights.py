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

        # assign first column to the assumed operations
        for i in range(rows):
            output[i][0] = first_column[i]

        # process following columns depending on the lights and the assumed status
        for j in range(1, columns):
            # this is to make sure the lights in previous column can be turned off
            for i in range(rows):
                # check what is the initial status and what are the operations in previous 1/2 rows
                # if status is 1, then need to turn if off, so we assign 1 here
                # if status is 0, then nothing to do, so we assign 0 here

                # it will be affected by the initial status, and what operation we do with the light itself
                output[i][j] = lights[i][j - 1] ^ output[i][j - 1]
                if i == 0:
                    # if it's the first row, then will be affected by next row
                    output[i][j] = output[i][j] ^ output[i+1][j-1]
                elif i == rows - 1:
                    # if it's the last row, then will be affected by last row
                    output[i][j] = output[i][j] ^ output[i-1][j-1]
                else:
                    # for other rows, it will be affected by both last row and next row
                    output[i][j] = output[i][j] ^ output[i-1][j-1] ^ output[i+1][j-1]
                if j > 1:
                    # starting from 2nd row, it will also be affected by previous row
                    output[i][j] = output[i][j] ^ output[i][j - 2]
            logging.debug(f'output: {output}')

        # above operations can make sure that the first (columns-1) rows are turned off, leaving the last column

        # this is to check if lights in the last column are turned off
        # if they are, then we found the correct first-column assumption and the final solution
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
