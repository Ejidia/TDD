def multiply(a, b):
   return a * b
def test_multiply_1_by_1():
    assert multiply(1, 1) == 1


def test_multiply_2_by_2():
    assert multiply(2, 2) == 4

def test_multiply_3_by_3():
    assert multiply(3, 3) == 9

def test_multiply_4_by_4():
    assert multiply(4, 4) == 16

def test_multiply_23_by_45():
    assert multiply(23, 45) == 23 * 45
