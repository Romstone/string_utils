import pytest

from string_utils.utils import reverse_words_tier_2

pytestmark = [pytest.mark.tier_2]

def test_edge_whitespace(edge_whitespace_examples) -> None:
    for original, expected in edge_whitespace_examples:
        assert reverse_words_tier_2(original) == expected

def test_invalid_inputs(invalid_inputs_examples) -> None:
    for invalid in invalid_inputs_examples:
        with pytest.raises(TypeError):
            reverse_words_tier_2(invalid)

################## Testing addoption ####################

def test_reverse_func_selector(reverse_func_tier_selector, get_selected_tier) -> None:
    result = reverse_func_tier_selector("   One   Two   ")
    if get_selected_tier == '1':
        assert result == "Two One"
        print('Ya jiva istota')
    else:
        assert result == "   Two   One   "
        print('Ya beru u rota')