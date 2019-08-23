from actions.action import plus


class Test:

    def test_plus_ok(self):
        assert plus(3, 2) == 5, 'Неправильный результат'

    def test_plus_max(self):
        assert plus(50, 50) == 100, 'Неправильный результат'

    def test_plus_overflow(self):
        assert plus(51, 51) == 102, 'Неправильный результат'