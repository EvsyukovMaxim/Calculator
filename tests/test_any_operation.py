from actions.action import any_op


def test_any_op_ok():
    assert any_op(3, 2,
                  ']') == '"operation" value must be one of "[\'-\', \'+\', \'/\', \'*\']"', \
        'Неправильный результат'


def test_any_op_no_op():
    assert any_op(3, 2,
                  '') == '"operation" value must be one of "[\'-\', \'+\', \'/\', \'*\']"', \
        'Неправильный результат'
