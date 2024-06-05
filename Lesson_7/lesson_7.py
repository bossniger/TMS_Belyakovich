import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        count_time = end_time - start_time
        return result, count_time
    return wrapper


@measure_time
def test_func(seconds):
    time.sleep(seconds)
    a = 0
    for i in range(1000):
        a += (i ** 100)
    return f"Функция выполнится через {seconds} секунд."


result, elapsed_time = test_func(1)
print(result)
print(f"Функция выполнилась за {elapsed_time} секунд")