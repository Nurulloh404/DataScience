import pytest
from financial import parse

def test_parse_success():
    """
    Test case for a successful API call.
     Checks if the 'parse' function correctly retrieves data for a valid ticker and field.
    """

    result = parse('MSFT', 'Open')

    assert isinstance(result, tuple)
    assert len(result) == 2
    
    assert result[0] == 'Open'

    value = result[1].replace('.', '').replace(',', '')
    assert value.isdigit()

def test_parse_invalid_ticker():
    """
    Test case for handling an invalid ticker symbol.
    Expected behavior: The function should raise a ValueError.
    """
    with pytest.raises(ValueError, match="not found"):
        parse('INVALID_TICKER_XYZ', 'Open')

def test_parse_invalid_field():
    """
    Test case for handling an invalid field name for a valid ticker.
    Expected behavior: The function should raise a ValueError.
    """
    with pytest.raises(ValueError, match="not found on page"):
        parse('MSFT', 'InvalidField')