import pytest
from stuff.accum import Accumulator

# add fixture to reduce repetitive code accum()
@pytest.fixture
def accum():
    return Accumulator()

# multiple fixtures
@pytest.fixture
def accum2():
    return Accumulator()

# init
def test_accumulator_init(accum, accum2):
    assert accum.count == 0