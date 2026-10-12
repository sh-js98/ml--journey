import pytest
from day2_text import parse_price_line, simple_return, group_prices_by_symbol, top_words


def test_parse_price_line_good():
    result = parse_price_line("2023-01-01, AAPL, 150.00")
    assert result == {"date": "2023-01-01", "symbol": "AAPL", "price": 150.0}


def test_parse_price_line_bad():
    with pytest.raises(ValueError):
        parse_price_line("hello")


def test_simple_return():
    assert simple_return([100, 110, 99]) == pytest.approx([0.10, -0.10])