class UnexpectedContentToParseException(Exception):
    '''
        Exception to be raised when content to be parsed does not have expected data.
    '''


class BadRequestException(Exception):
    '''
        Exception to be raised when response from requested url is not ok.
    '''
