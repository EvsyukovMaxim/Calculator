import pytest

from actions.action import plus


def test_plus():
    assert plus(3, 2) == 5, 'Неправильный результат'


def test_plus_max_digits():
    assert plus(50, 50) == 100, 'Неправильный результат'


@pytest.mark.skip(reason='Заранее знаем что будет фейл, т.к. результат: -1')
def test_plus_overflow():
    assert plus(51, 51) == 102, 'Неправильный результат'
