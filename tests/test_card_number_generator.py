import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (5, 5, ["0000 0000 0000 0005"]),
        (5, 2, []),
    ],
)
def test_card_generator_simple(x, y, expected):
    result = list(card_number_generator(x, y))

    assert result == expected
