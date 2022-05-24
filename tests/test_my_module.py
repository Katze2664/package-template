"""Test my module"""

import pytest

from my_module.my_mod import terminator, mod_v2


def test_terminator():
    """Say hey."""
    output = terminator("hey")
    assert output == "hey."

@pytest.mark.parametrize(
    "x,n,expectation",
    [
        (3, 3, 3),
        (2, 3, 2),
        (6, 3, 3),
        (0, 3, 3)
    ]
)
def test_mod_v2(x,n,expectation):
    """Test the superior mod."""
    output = mod_v2(x,n)
    assert output == expectation
