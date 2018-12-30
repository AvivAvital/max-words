from knownDateFormats import KnownDateFormats


class DateParser:
    def __init__(self):
        self._date_format = KnownDateFormats().format_matcher

    def determine_file_date_format(self, file_handler):
        _line = file_handler.readline()
        return self.is_date_format_known(_line)

    def is_date_format_known(self, string):
        for strftime_matcher in self._date_format.keys():
            try:
                _start, _end = strftime_matcher.match(string).span()
                return _end, self._date_format[strftime_matcher]
            except AttributeError:
                pass

        return None, None
