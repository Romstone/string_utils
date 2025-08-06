import pytest

from string_utils.utils import reverse_words

pytestmark = [pytest.mark.tier_1]

normal_string_data = [
    ('Normal sentence', 'sentence Normal'),
    ('How about this sentence, is it okay?', 'okay? it is sentence, this about How'),
    ('One more sentence, just to be sure', 'sure be to just sentence, more One'),
    ('Maybe another one, just in case?', 'case? in just one, another Maybe')
]

whitespace_string_data = [
    ('   Leading space here', 'here space Leading'),
    ('Trailing space here  ', 'here space Trailing'),
    ('  Both leading and trailing  ', 'trailing and leading Both'),
    ('Multiple   spaces  between words', 'words between spaces Multiple')
]

single_string_data = [
    ('Single', 'Single'),
    ('string', 'string'),
    ('wOrrrddDDDD', 'wOrrrddDDDD')
]

@pytest.mark.parametrize('string, reverse_str', normal_string_data)
def test_normal_string(string: str, reverse_str: str) -> None:
    assert reverse_words(string) == reverse_str

@pytest.mark.parametrize('string, reverse_str', whitespace_string_data)
def test_whitespace_string(string: str, reverse_str: str) -> None:
    assert reverse_words(string) == reverse_str

@pytest.mark.parametrize('string, reverse_str', [("", '')])
def test_empty_string(string: str, reverse_str: str) -> None:
    assert reverse_words(string) == reverse_str

@pytest.mark.parametrize('string, reverse_str', single_string_data)
def test_single_string(string: str, reverse_str: str) -> None:
    assert reverse_words(string) == reverse_str