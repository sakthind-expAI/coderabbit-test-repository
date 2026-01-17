import pytest

from simple_utils import count_words


def test_empty_string():
    assert count_words("") == 0

def test_whitespace_only():
    assert count_words("   \t\n  ") == 0

def test_multiple_spaces_and_newlines():
    # "Hello   world\nthis\tis a test" -> ["Hello","world","this","is","a","test"]
    assert count_words("Hello   world\nthis\tis a test") == 6

def test_normal_sentence():
    assert count_words("Hello, world!") == 2

def test_non_str_raises_type_error():
    with pytest.raises(TypeError):
        count_words(None)
    with pytest.raises(TypeError):
        count_words(123)
