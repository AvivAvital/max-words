class InvalidDateTimeException(Exception):
    """Raise an error when datetime string is not a valid datetime format or a timestamp"""
    def __init__(self):
        Exception.__init__(self, 'Invalid datetime string provided. String is either unknown date format or not an epoch')


class InvalidDateTimeRangeException(Exception):
    """Raise an error when timestamp/datetime range is invalid (i.e. start value is smaller than end value)"""
    def __init__(self):
        Exception.__init__(self, 'Invalid datetime range provided. Range is either unknown date format or not an epoch')


class InvalidRangeException(Exception):
    """Raise an error when string is either not a valid datetime range or a valid timestamp range"""
    def __init__(self):
        Exception.__init__(self, 'Invalid datetime range provided. Start should be smaller than end')

