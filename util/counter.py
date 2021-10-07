class Counter(object):
    def __init__(self, func):
        self._func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._func(*args, **kwargs)
