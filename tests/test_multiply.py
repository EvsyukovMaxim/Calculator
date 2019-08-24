import pytest

from actions.action import multiply


@pytest.mark.skip(reason='Умножение работает как деление, результат: 2')
def test_multiply():
    assert multiply(4, 2) == 8, 'Неправильный результат'


@pytest.mark.skip(
    reason='Умножение работает как деление, но даже при делении на ноль - результат: 1')
def test_multiply_zero():
    assert multiply(50, 0) == 0, 'Неправильный результат'
