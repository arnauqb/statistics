from mean import mean


def test_result():
    """
    TEsts mean result.
    """

    number_list = [1,2,3]
    expected_mean = 2
    assert mean(number_list) == expected_mean

def test_negative_numbers():
    number_list = [-1, -2, -3]
    assert mean(number_list) == -2

def test_empty_list():
    number_list = []
    assert mean(number_list) == 0



