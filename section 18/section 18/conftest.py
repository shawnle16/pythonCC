import pytest

@pytest.fixture
def setup1():
    print("I will execute testing")
    yield
    print("I will close testing")

# Use the fixture in a test
def test_fixture_demo(setup1):
    print(" I will execute the steps in text_fixture method")

@pytest.fixture()
def data_load():
    print("This profile is created")
    return ("Son", "Le")