from actions.action import minus


class Test:

    def test_minus_ok(self):
        assert minus(3, 2) == 1, 'Неправильный результат'
