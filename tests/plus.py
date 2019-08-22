from actions.action import plus, minus


class Test:
    def test_plus_ok(self):
        assert plus(3, 2) == 5, 'Неправильный результат'

    def test_minus_ok(self):
        assert minus(3, 2) == 1, 'Неправильный результат'