# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string"""
    return text[::-1]

def count_words(sentence):
    """
    Count words in a sentence.
    
    Parameters:
        sentence (str): Input text whose words will be counted.
    
    Returns:
        int: Number of words, defined as segments separated by whitespace.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32