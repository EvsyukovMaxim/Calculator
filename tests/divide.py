from actions.action import divide


class Test:

    def test_divide_ok(self):
        assert divide(3, 3) == 1, 'Неправильный результат'
