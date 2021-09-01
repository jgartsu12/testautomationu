import pytest
from stuff.accum import Accumulator

# add fixture to reduce repetitive code accum()
@pytest.fixture
def accum():
    return Accumulator()

# using yield makes fixture generatr
@pytest.fixture
def accum():
    yield Accumulator()
    print("DONE-zo!")

# session scope for fixture
@pytest.fixture
def accum(scope="session"):
    return Accumulator()

# multiple fixtures
@pytest.fixture
def accum2():
    return Accumulator()



# init
def test_accumulator_init(accum, accum2):
    assert accum.count == 0