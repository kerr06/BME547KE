
import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.1 lb", 10),
    ("35.5 kg", 36),
    ("22 lbs", 10),
    # ("too much", False), not testing bc it will happen later in class
    # ("22", False),
    ("22 KG", 22),
    ("22 Kg", 22),
    # ("64 g", False),
    # ("22kg", 22),
    # ("ten kg", False), not testing
    ("-22 lb", -10)
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected
