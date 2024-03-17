import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' executed in {time.time() - start_time:.6f} seconds.")
        return result
    return wrapper

@measure_execution_time
def example_function(n):
    return sum(range(n))

def test_measure_execution_time():
    assert example_function(1000000) == 499999500000
    print("All tests passed successfully!")

test_measure_execution_time()