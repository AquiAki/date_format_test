import pytest
from script import format_date

def test_format_date():
    assert format_date("1995.2.4") == "1995-02-04"
    assert format_date("2008/12/23") == "2008-12-23"
    assert format_date("平成5年2月6日") == "1993-02-06"
    assert format_date("R3/08/30") == "2021-08-30"
    assert format_date("20180506") == "2018-05-06"
    assert format_date("invalid_date") is None