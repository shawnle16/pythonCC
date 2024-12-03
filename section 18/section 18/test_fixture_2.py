import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture_demo(self):
        print("I will execute steps in fixture_demo")

    def test_fixture_demo1(self):
        pass