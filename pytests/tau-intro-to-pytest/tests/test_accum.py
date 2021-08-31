import pytest
from stuff.accum import Accumulator

# method verifies new instance of accumulator clas has starting count of zero
def test_accumulator_init():
    accum = Accumulator()  #this repeats in test case and violates DRY
    assert accum.count == 0

# method verifies that add() adds one to the internal count when call w/ no args
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


# method verifies that add() adds 3 to count when it is called with arg of 3
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


# method verifies that count increases appropriately with multiple add() calls
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


# method verifies that count attribute cant be assigned directly because its a read-only property, pytest.raises used to verify attribute error
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10    
