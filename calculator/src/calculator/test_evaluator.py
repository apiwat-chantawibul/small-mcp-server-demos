import pytest

from calculator.evaluator import Evaluator


@pytest.mark.parametrize(
    'description, expression, expected',
    [
        (
            'Single float',
            '3.14',
            3.14,
        ),
        (
            'Single addition',
            '1+2',
            3,
        ),
        (
            'Precendence without bracket',
            '4+2**3',
            12,
        ),
        (
            'Precendence with bracket',
            '(4+2)**3',
            216,
        ),
    ],
    ids = (lambda x, *_: x),
)
def test_eval_success(description, expression, expected):
    result = Evaluator.eval(expression)
    assert result == expected


@pytest.mark.parametrize(
    'description, expression, exception',
    [
        (
            'not number',
            'adsf',
            ValueError,
        ),
    ],
    ids = (lambda x, *_: x),
)
def test_eval_failure(description, expression, exception):
    with pytest.raises(exception):
        result = Evaluator.eval(expression)

