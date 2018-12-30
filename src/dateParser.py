from knownDateFormats import KnownDateFormats


class DateParser:
    def __init__(self,file_handler):
        self.file_handler = file_handler
        self._date_format = KnownDateFormats().format_matcher

    def is_date_format_known(self):
        _line = self.file_handler.readline()
        for matcher in self._date_format.keys():
            try:
                _start, _end = matcher.match(_line).span()
                return _end
            except AttributeError:
                pass

        return None
