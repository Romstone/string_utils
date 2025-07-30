from typing import Generator, List, Any

import pytest
from string_utils.utils import reverse_words_tier_2

@pytest.fixture()
def edge_whitespace_examples() -> Generator[List[Any], None, None]:
    test_data = [
        ('\tHello World\n', '\tWorld Hello\n'),
        ('\t', '\t'),
        ('\n    some words  and more\t', '\n    more and  words some\t'),
    ]
    yield test_data

@pytest.fixture()
def invalid_inputs_examples() -> Generator[List[Any], None, None]:
    test_data = [None, 123, 3.14, [], ()]
    yield test_data

def test_edge_whitespace(edge_whitespace_examples) -> None:
    for original, expected in edge_whitespace_examples:
        assert reverse_words_tier_2(original) == expected

def test_invalid_inputs(invalid_inputs_examples) -> None:
    for invalid in invalid_inputs_examples:
        with pytest.raises(TypeError):
            reverse_words_tier_2(invalid)

