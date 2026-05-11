from demo.calculator import calculate_discount, divide


def test_divide():
    assert divide(10, 2) == 5


def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 25) == 150