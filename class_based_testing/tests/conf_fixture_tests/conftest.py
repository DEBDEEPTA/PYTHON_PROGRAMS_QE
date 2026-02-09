import pytest

@pytest.fixture
def fixture_t1():
    print("Fixture Test t1 executed")
    return True

@pytest.fixture
def fixture_t2():
    print("Fixture Test t2 executed")
    return False