from actions.action import minus


class Test:

    def test_minus_ok(self):
        assert minus(3, 2) == 1, 'Неправильный результат'

    def test_minus_right_bigger(self):
        assert minus(7, 9) == -2, 'Неправильный результат'
