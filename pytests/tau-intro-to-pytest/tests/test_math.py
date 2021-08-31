import pytest
'''
def test_one_plus_one():
    assert 1+1 == 2

    # python -m pytest to test in cli



# failed test
def test_one_plus_two():
    a=1
    b=2
    c=0 
    assert a + b == c
# success 
def test_one_plus_two():
    a=1
    b=2
    c=3 
    assert a + b == c
'''
'''
# test case with an exception
def test_dvide_by_zero():
    num = 1 / 0
    # prints ZeroDivisionError: division by zero
'''

'''
# zero division error with pytest.raises 
def test_dvide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
# With statement stores the exceptipn obj as a var named 'e'
    assert 'division by zero' in str(e.value)
'''

# list of tuples
products = [
    (2, 3, 6),           #multiply pos ints
    (1, 99, 99),          # id
    (0, 99, 0),             #zero
    (3, -4, -12),              #pos by neg
    (-5, -5, 25),            #neg by neg
    (2.5, 6.7, 16.75)       #floats
]
'''
# multiplication tests:
# We could multiply two positive integers.
def test_multiply_two_pos_ints():
    assert 2 * 3 == 6

# We could test identity by multiplying any number by one.
def test_multiply_identity():
    assert 1 * 99 == 99
# We could test the zero property by multiplying any number by zero.
def test_multiply_zero():
    assert 0 * 100 == 0

# We can multiply a positive by a negative.
# def test_
# We could test negative numbers multiplied by negative numbers.
# def test_
# We could also multiply floating point numbers instead of integers.
# def test_
'''

# one test case function for all multiplication beh
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a,b, product):
    assert a * b == product