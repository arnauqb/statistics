from fibonacci import fibonacci

def test_first_number():
    n = 10
    fibonacci_series = fibonacci(n)
    assert(fibonacci_series[0] == 1)

def test_second_number():
    n = 10
    fibonacci_series = fibonacci(n)
    assert(fibonacci_series[1] == 1)

def test_mid_number():
    n = 10
    fibonacci_series = fibonacci(n)
    assert (fibonacci_series[3] == 3)
