# test_calculator.py

import pytest
from calculator import add, divide

# ✅ Fixture
@pytest.fixture
def numbers():
    return (10, 5)

# ✅ Using the fixture
def test_add_with_fixture(numbers):
    a, b = numbers
    assert add(a, b) == 15

# ✅ Parametrize
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# ✅ Exception Testing
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# ✅ Mocking (simple usage with monkeypatch)
def test_mocking(monkeypatch):
    def fake_divide(a, b):
        return 42  # Simulated fake result

    monkeypatch.setattr("calculator.divide", fake_divide)
    assert divide(10, 5) == 42
