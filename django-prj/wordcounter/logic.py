def count_words(message: str) -> int:
    """
    Return the number of words in the provided message.
    :param message: the message
    :return: the number of words in the provided message.
    """
    return len(message.split(" "))
