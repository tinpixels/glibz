

class CustomException(Exception):
    """ Base class for all custom exceptions. """
    pass


class InvalidCharacterSet(CustomException):
    """ Exception raised when an invalid character set is encountered.

    Attributes:
        expression -- input expression in which the error occurred.
        message -- explanation of the error to be returned to the user.
    """

    def __init__(self, message=''):

        if message == '':
            self.message = 'Exception: an invalid or unsupported character set specification was encountered.'
        else:
            self.message = message


class InvalidLineEnding(CustomException):
    """ Exception raised when an invalid character set is encountered.

    Attributes:
        expression -- input expression in which the error occurred.
        message -- explanation of the error to be returned to the user.
    """

    def __init__(self, message=''):

        if message == '':
            self.message = 'Exception: an invalid line ending specification was encountered.\n' \
                'Valid values are:\n' \
                '\t"unix" for line-feed (\\n)\n' \
                '\t"win"  for carriage-return line-feed (\\r\\n)\n' \
                '\t"mac9" for carriage-return (\\r)\n'
        else:
            self.message = message
