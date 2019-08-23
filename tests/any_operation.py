from actions.action import any_op


class Test:

    def test_any_op_ok(self):
        assert any_op(3, 2, ']') == '"operation" value must be one of "[\'-\', \'+\', \'/\', \'*\']"', \
                                                                                'Неправильный результат'

    def test_any_op_no_op(self):
        assert any_op(3, 2, '') == '"operation" value must be one of "[\'-\', \'+\', \'/\', \'*\']"', \
                                                                                'Неправильный результат'