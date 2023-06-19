import pytest

from wordcounter.logic import count_words


@pytest.mark.parametrize(
    'message, expected_words', [
        ('Hello World', 2),
        ('Hello', 1),
        ('    Hello world    !  ', 2),
        ('First line\r\nSecond line\r\nThird', 5),
        ('Hello\tWorld!', 2),
    ]
)
def test_count_words(message, expected_words):
    assert count_words(message) == expected_words
