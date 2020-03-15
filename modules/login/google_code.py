# coding=utf-8
import pyotp

"""
This python script is used to parse google auth code.
"""


def get_google_code(token):
    """
    Parse google auth code
    :param token: token
    :return: code with six numbers
    """
    totp = pyotp.TOTP(token)
    return totp.now()


# replace to your own token
print(get_google_code("abc"))
