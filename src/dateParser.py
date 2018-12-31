from knownDateFormats import KnownDateFormats


class DateParser:
    def __init__(self):
        self._date_format = KnownDateFormats().format_matcher

    def determine_file_date_format(self, file_handler):
        """
        This method reads the first line to determine if file holds known datetime format
        :param file_handler: io.TextIOWrapper object
        :return: Calls is_date_format_known
        """
        _line = file_handler.readline()
        file_handler.seek(0)
        return self.is_date_format_known(_line)

    def is_date_format_known(self, string):
        """
        :param string: String - Usually first line of a file
        :return: If line with known file format, returns endpos of datetime format and strftime string. If not returns None tuple
        """
        for strftime_matcher in self._date_format:
            try:
                _start, _end = strftime_matcher.search(string).span()
                return _end, self._date_format[strftime_matcher]
            except AttributeError:
                pass

        return None, None
