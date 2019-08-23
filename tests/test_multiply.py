from actions.action import multiply


class Test:

    #умножение работает неправильно
    def test_multiply_ok(self):
        assert multiply(3, 2) == 6, 'Неправильный результат'

    #умножение работает как деление
    def test_multiply_like_division_ok(self):
        assert multiply(6, 2) == 3, 'Неправильный результат'