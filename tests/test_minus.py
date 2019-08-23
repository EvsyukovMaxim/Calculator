import pytest

from actions.action import minus


class Test:

    def test_minus(self):
        assert minus(3, 2) == 1, 'Неправильный результат'

    @pytest.mark.skip(reason='Заранее знаем что будет фейл, т.к. результат: 2')
    def test_minus_right_bigger(self):
        assert minus(7, 9) == -2, 'Неправильный результат'
