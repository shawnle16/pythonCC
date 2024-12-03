import pytest

@pytest.fixture
def setup1():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture
def setup2():
    print("I will execute testing")
    yield
    print("I will close testing")

# Use the fixture in a test
def test_fixture_demo(setup1):
    print(" I will execute the steps in text_fixture method")

def test_second_program(setup2):
    print("Good morning")