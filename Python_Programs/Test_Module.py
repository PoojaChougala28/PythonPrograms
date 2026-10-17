import pytest
@pytest.fixture
def demo():
    print("Fixture Demo")

def test_one(demo):
    print("one")

def test_two(demo):
    print("two")