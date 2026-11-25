import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('text_str, text_result', [
    ('text', 'Text'),
    ('text 1 big', 'Text 1 big')
    ])
def test_capitalize_positive(text_str, text_result):
    assert string_utils.capitalize(text_str) == text_result


@pytest.mark.negative
@pytest.mark.parametrize('text_str, text_result', [
    ('', ''),
    ('123text', '123text')
    ])
def test_capitalize_negative(text_str, text_result):
    assert string_utils.capitalize(text_str) == text_result


@pytest.mark.positive
@pytest.mark.parametrize('text_str, text_result', [
    (' text', 'text')
    ])
def test_trim_positive(text_str, text_result):
    assert string_utils.trim(text_str) == text_result


@pytest.mark.negative
@pytest.mark.parametrize('text_str, text_result', [
    ('   ', '')
    ])
def test_trim_negative(text_str, text_result):
    assert string_utils.trim(text_str) == text_result


@pytest.mark.positive
@pytest.mark.parametrize('text_str, symbol, expected', [
    ('text', 't', True),
    ('text 1 big', '', True),
    ('12345', '5', True)
])
def test_contains_positive(text_str, symbol, expected):
    assert string_utils.contains(text_str, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize('text_str, symbol, expected', [
    ('text', 'T', False),
    ('', 't', False)
])
def test_contains_negative(text_str, symbol, expected):
    assert string_utils.contains(text_str, symbol) is expected


@pytest.mark.positive
@pytest.mark.parametrize('text_str, symbol, text_result', [
    ('text', 't', 'ex'),
    ('text 1 big', '1 ', 'text big'),
    ('1234 5', ' ', '12345')
])
def test_delete_symbol_positive(text_str, symbol, text_result):
    assert string_utils.delete_symbol(text_str, symbol) == text_result


@pytest.mark.negative
@pytest.mark.parametrize('text_str, symbol, text_result', [
    ('text', 'T', 'text'),
    ('', 't', '')
])
def test_delete_symbol_negative(text_str, symbol, text_result):
    assert string_utils.delete_symbol(text_str, symbol) == text_result
