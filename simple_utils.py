# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the input string with its characters in reverse order.
    
    Also prints the reversed string to standard output.
    
    Parameters:
        text (str): The string to reverse.
    
    Returns:
        str: The input string with characters reversed.
    """
    print(text[::-1])
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

def str_count(string):
    """
    Return the number of characters in the given string.
    
    Parameters:
        string (str): The input string whose characters are to be counted; counts all characters including whitespace.
    
    Returns:
        int: The length of `string` (number of characters).
    """
    return len(string)

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32