from time import perf_counter
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = perf_counter() - self.start
        print(f"Время выполнения: {elapsed:.6f} секунд")
        return False


@contextmanager
def timer():
    start = perf_counter()

    try:
        yield
    finally:
        elapsed = perf_counter() - start
        print(f"Время выполнения: {elapsed:.6f} секунд")


with Timer():
    sum(range(1_000_000))


with timer():
    sum(range(1_000_000))