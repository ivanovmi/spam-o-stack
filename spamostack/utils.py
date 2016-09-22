import random
import string

_ASCII_LETTERS_AND_DIGITS = string.ascii_letters + string.digits


def generate_random_name(prefix="", length=16,
                         choice=_ASCII_LETTERS_AND_DIGITS):
    """Generates pseudo random name.

    :param prefix: str, custom prefix for random name
    :param length: int, length of random name
    :param choice: str, chars for random choice
    :returns: str, pseudo random name
    """

    rand_part = "".join(random.choice(choice) for i in range(length))
    return prefix + rand_part

print generate_random_name()