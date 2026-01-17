"""
Utility functions for simple string and temperature operations.
"""

def reverse_string(text: str) -> str:
    """Return a reversed copy of the input string.

    Args:
        text: String to reverse.

    Returns:
        The reversed string.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return text[::-1]

def count_words(sentence: str) -> int:
    """Count words in a sentence.

    Words are defined as segments separated by any whitespace. This uses
    str.split(), so punctuation attached to words is counted as part of
    the word. A string containing only whitespace returns 0.

    Args:
        sentence: Input text whose words will be counted.

    Returns:
        Number of words.

    Raises:
        TypeError: If sentence is not a str.
    """
    if not isinstance(sentence, str):
        raise TypeError("sentence must be a str")
    return len(sentence.split())

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.

    Raises:
        TypeError: If celsius is not a number.
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("celsius must be a number")
    return celsius * 9.0 / 5.0 + 32.0

# End of simple_utils.py