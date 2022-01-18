class Counter:
    __slots__ = ("_min", "_max", "_current")

    def __init__(self, max=0, min=0):
        self._min = min if min <= max else max
        self._max = max if min <= max else min
        self._current = self._min
    
    def increment(self):
        if self._current < self._max:
            self._current += 1
        return self._current
    
    def reset(self):
        self._current = self._min

    def update(self, *, min=None, max=None):
        if min is None:
            min = self._min

        if max is None:
            max = self._max

        self._min = min if min <= max else max
        self._max = max if min <= max else min

        if self._current < self._min:
            self._current = self._min
        elif self._current > self._max:
            self._current = self._max
    
    def get_current(self):
        return self._current
    
    def get_min(self):
        return self._min
    
    def get_max(self):
        return self._max
    
if __name__ == "__main__":
    counter = Counter(10)
    print(f"Counter (start)      : {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.increment()
    print(f"Counter (incremented): {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.increment()
    print(f"Counter (incremented): {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.update(min=5)
    print(f"Counter (updated)    : {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.update(min=0, max=7)
    print(f"Counter (updated)    : {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.update(max=3)
    print(f"Counter (updated)    : {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")

    counter.reset()
    print(f"Counter (reset)      : {counter.get_min()} <= {counter.get_current()} <= {counter.get_max()}")