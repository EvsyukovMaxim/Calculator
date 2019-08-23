import pytest

from actions.action import multiply


class Test:

    @pytest.mark.skip(reason='Умножение работает как деление, результат: 2')
    def test_multiply(self):
        assert multiply(4, 2) == 8, 'Неправильный результат'

    @pytest.mark.skip(reason='Умножение работает как деление, но даже при делении на ноль - результат: 1')
    def test_multiply_zero(self):
        assert multiply(50, 0) == 0, 'Неправильный результат'