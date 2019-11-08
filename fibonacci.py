





def fibonacci(n):
    """
    Returns first n elements of fibonacci sequence.
    """
    fibonacci_series = [1,0]
    for i in range(2,n):
        num1 = fibonacci_series[i-1]
        num2 = fibonacci_series[i-2]
        fibonacci_series.append(num1+num2)
    return fibonacci_series




    
