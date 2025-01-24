import pytest


@pytest.mark.parametrize("weight_input, expected", [
    ("20 lb", 9),
    ("50 kg", 50),'
    ("23.5 kg", 23.5),
    ("20 lbs", 9),
    ("-20 lbs", -9),
    ("-20 lb", -9),
    ("20 g", 0.02),
    ("20 pounds", 9),
    ("10000000 kg", 10000000),
    ("20       kg", 20)
    ("   20 kg", 20)
    ("20kg", 20),
    ("20 LB", 9),
])
def test_parse_weight_input(weight_input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(weight_input)
    assert answer == expected
