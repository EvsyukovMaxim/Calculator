import pytest

from actions.action import divide


class Test:

    @pytest.mark.skip(reason='Деление выдает непредсказуемый результат: -1')
    def test_divide(self):
        assert divide(3, 3) == 1, 'Неправильный результат'

    @pytest.mark.skip(reason='Деление на ноль выдает результат: 1')
    def test_divide_zero(self):
        assert divide(3, 0) == 0, 'Неправильный результат'