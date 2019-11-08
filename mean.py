def mean(number_list):
    """
    Computes the mean of a list of numbers.
    """
    list_length = len(number_list)
    #assert list_length > 0
    try:
        mean = sum(number_list) / (list_length)
    except TypeError as detail:
        raise TypeError("you did not pass me a list of numbers")

    except ZeroDivisionError:
        #raise ZeroDivisionError("you passed me an empty list") 
        return 0
    
        # do something instead
    return mean

print(mean([]))
