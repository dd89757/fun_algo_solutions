import logging
import math

from util.logging_setting import log_for_func
from dynamic_programming.knapsack_problem.input import CAPACITY, ITEMS, ITEMS_MULTIPLE


class KnapsackSolutionApp:
    def __init__(self, capacity: int, items: dict, items_multiple: dict):
        logging.info('Initializing KnapsackSolutionApp...')

        self.capacity = capacity
        self.items = items
        self.items_multiple = items_multiple

        self.dp = None

    def _initialize_matrix(self):
        """
        # initialize the matrix
        :return: the initialized matrix
        """
        self.dp = [[[] for _ in range(self.capacity + 1)] for _ in range(len(self.items) + 1)]

    @log_for_func('info')
    def knapsack_01(self):
        self._initialize_matrix()
        n = len(self.items)
        c = self.capacity
        return self._knapsack_01(n, c)

    @log_for_func('debug')
    def _knapsack_01(self, n: int, c: int) -> int:
        """
        This function is to solve the classic knapsack question. 0-1 means for each item, either select or not...
        There is only 1 item each.
        There sum of final selected items can be equal to or less than the capacity.
        :param n: the n-th item
        :param c: the capacity of the knapsack
        :return: the maximum weight
        """

        if self.dp[n][c]:
            logging.debug('case 0')
            return self.dp[n][c]
        if n == 0 or c <= 0:
            logging.debug('case 1')
            result = 0
        elif self.items[n]['weight'] > c:
            logging.debug('case 2')
            result = self._knapsack_01(n - 1, c)
        else:
            logging.debug('case 3')
            tmp1 = self._knapsack_01(n - 1, c)
            tmp2 = self.items[n]['value'] + self._knapsack_01(n - 1, c - self.items[n]['weight'])
            result = max(tmp1, tmp2)

        self.dp[n][c] = result

        return result

    @log_for_func('info')
    def knapsack_full(self):
        self._initialize_matrix()
        n = len(self.items)
        c = self.capacity
        return self._knapsack_full(n, c)

    @log_for_func('debug')
    def _knapsack_full(self, n: int, c: int) -> int:
        """
        There is only 1 item each.
        There sum of final selected items must be equal to the capacity.
        :param n:
        :param c:
        :return:
        """

        if self.dp[n][c]:
            logging.debug('case 0')
            return self.dp[n][c]
        if n == 0 and c > 0:
            logging.debug('case 1')
            result = -math.inf
        elif c <= 0:
            logging.debug('case 2')
            result = 0
        elif self.items[n]['weight'] > c:
            logging.debug('case 3')
            result = self._knapsack_full(n - 1, c)
        else:
            logging.debug('case 4')
            tmp1 = self._knapsack_full(n - 1, c)
            tmp2 = self.items[n]['value'] + self._knapsack_full(n - 1, c - self.items[n]['weight'])
            result = max(tmp1, tmp2)

        self.dp[n][c] = result
        return result

    @log_for_func('info')
    def knapsack_complete(self):
        self._initialize_matrix()
        n = len(self.items_multiple)
        c = self.capacity
        return self._knapsack_complete(n, c)

    @log_for_func('debug')
    def _knapsack_complete(self, n: int, c: int) -> int:
        """
        There are infinite numbers of each item.
        There sum of final selected items can be equal to or less than the capacity.
        :param n:
        :param c:
        :return:
        """

        if self.dp[n][c]:
            logging.debug('case 0')
            return self.dp[n][c]
        if n == 0 or c <= 0:
            logging.debug('case 1')
            result = 0
        elif self.items[n]['weight'] > c:
            logging.debug('case 2')
            result = self._knapsack_complete(n - 1, c)
        else:
            logging.debug('case 3')
            tmp1 = self._knapsack_complete(n - 1, c)
            tmp2 = self.items[n]['value'] + self._knapsack_complete(n, c - self.items[n]['weight'])
            result = max(tmp1, tmp2)

        self.dp[n][c] = result
        return result

    @log_for_func('info')
    def knapsack_multiple(self):
        self._initialize_matrix()
        n = len(self.items_multiple)
        c = self.capacity
        return self._knapsack_multiple(n, c)

    @log_for_func('debug')
    def _knapsack_multiple(self, n: int, c: int) -> int:
        """
        There are specific available numbers of each item.
        There sum of final selected items can be equal to or less than the capacity.
        :param n:
        :param c:
        :return:
        """

        if self.dp[n][c]:
            logging.debug('case 0')
            return self.dp[n][c]
        if n == 0 or c <= 0:
            logging.debug('case 1')
            result = 0
        elif self.items_multiple[n]['weight'] > c:
            logging.debug('case 2')
            result = self._knapsack_multiple(n - 1, c)
        else:
            logging.debug('case 3')
            tmp1 = self._knapsack_multiple(n - 1, c)
            tmp2 = 0
            for i in range(self.items_multiple[n]['count']):
                if c < (i + 1) * self.items_multiple[n]['weight']:
                    break
                tmp3 = (i + 1) * self.items_multiple[n]['value'] + \
                    self._knapsack_multiple(n - 1, c - (i + 1) * self.items_multiple[n]['weight'])
                tmp2 = max(tmp2, tmp3)
            result = max(tmp1, tmp2)

        self.dp[n][c] = result
        return result


def run():
    app = KnapsackSolutionApp(CAPACITY, ITEMS, ITEMS_MULTIPLE)
    app.knapsack_01()
    app.knapsack_full()
    app.knapsack_complete()
    app.knapsack_multiple()


if __name__ == '__main__':
    run()
