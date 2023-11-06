from morse import decode
import pytest


@pytest.mark.parametrize(
    "dot_dash, message",
    [('... --- ...', 'SOS'),
     ('', ''),
     ('.---- ..--- ...--', '123')]
)
def test_decode(dot_dash, message):
    assert decode(dot_dash) == message
