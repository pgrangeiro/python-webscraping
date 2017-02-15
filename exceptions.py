class UnexpectedContentToParseException(Exception):
    '''
        Exception to be raised when content to be parsed does not have expected data.
    '''

    def __init__(self, message=''):
        self.message = message


class BadRequestException(Exception):
    '''
        Exception to be raised when response from requested url is not ok.
    '''

    def __init__(self, message=''):
        self.message = message
