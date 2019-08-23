from actions.action import multiply


class Test:

    #умножение работает неправильно и выдаёт единицу
    def test_multiply_gives_1(self):
        assert multiply(3, 2) == 1, 'Неправильный результат'

    #умножение работает как деление
    def test_multiply_like_division_ok(self):
        assert multiply(6, 2) == 3, 'Неправильный результат'