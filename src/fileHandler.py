from logger import Logger
from collections import Counter
from dateParser import DateParser
from datetime import datetime


class FileHandler(Logger):
    """
    As the name suggests, this object handles all interactions of a given file
    Each object reports the current thread name and holds
    """
    def __init__(self):
        super().__init__()
        self._counter = Counter()
        self.start_timestamp = 0
        self.end_timestamp = 0

    def read_lines_from_file(self, file_handler, date_time_length, date_time_format):
        """
        :param file_handler: TextIOWrapper - File handler object
        :param date_time_length: Integer - Indicates the beginning of the string after the datetime section
        :param date_time_format: String - Points to strftime format to parse string to datetime object
        This method iterates line-by-line over a file handler using a generator.
        Each line is stripped from CRLF and split using a space delimiter and sent to a collections.Counter
        """
        for line in file_handler:
            self._counter += Counter(line[date_time_length:].strip().split(' '))

    def file_word_count(self, filename, start_timestamp=0, end_timestamp=0):
        """
        :param filename: String - Absolute path to filename
        :param start_date: Optional: Integer - In case date range, will hold the beginning of the range in epoch
        :param end_date: Optional: Integer - In case date range, will hold the end of the range in epoch
        :return: collections.Counter object
        """
        self.logger.debug('Reading file {0}'.format(filename))
        with open(filename, 'rt', encoding='utf-8') as file_handler:
            _parsed_datetime, _datetime_format = DateParser().determine_file_date_format(file_handler)
            if _parsed_datetime:
                self.read_lines_from_file(file_handler=file_handler,
                                          date_time_length=_parsed_datetime,
                                          date_time_format=_datetime_format)

        return self._counter
