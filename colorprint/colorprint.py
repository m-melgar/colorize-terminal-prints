"""
Author: @m-melgar
https://github.com/m-melgar
"""


def print_colored(string: str, color_id: str) -> None:
    """
    Prints string colorized as color_id.
    :param string: str
            String to be colorized.
    :param color_id: str
            Linux terminal color ID, reference https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal.
    :return: None
    """
    print(color_id + string + '\x1b[0m')


def colorize_string(string: str, color_id) -> str:
    """
    Colorizes a string to be used with "print" function.
    :param string: str
            String to be colorized.
    :param color_id: str
            Linux terminal color ID, reference https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal.
    :return: str
            Formatted string.
    """
    return color_id + string + '\x1b[0m'
