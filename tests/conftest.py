from typing import Any, Callable, Generator
from _pytest.config import Parser
from _pytest.fixtures import FixtureRequest

import pytest

from string_utils.utils import *

def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        '--tier',
        action='store',
        default='1',
        choices=['1', '2'],
        help="Specify which tier of reverse_words to test: '1' or '2'"
    )

@pytest.fixture
def reverse_func_tier_selector(request: FixtureRequest) -> Callable[[str], str]:
    tier = request.config.getoption('tier')
    if tier == '1':
        return reverse_words
    else:
        return reverse_words_tier_2

@pytest.fixture
def get_selected_tier(request) -> str:
    return request.config.getoption('tier')

@pytest.fixture()
def edge_whitespace_examples() -> Generator[list[tuple[str, str]], None, None]:
    test_data = [
        ('\tHello World\n', '\tWorld Hello\n'),
        ('\t', '\t'),
        ('\n    some words  and more\t', '\n    more and  words some\t'),
    ]
    yield test_data

@pytest.fixture()
def invalid_inputs_examples() -> Generator[list[Any], None, None]:
    test_data = [None, 123, 3.14, [], ()]
    yield test_data