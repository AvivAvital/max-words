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

    def read_lines_from_file(self, file_handler, date_time_length, date_time_format, datetime_search_criteria):
        """
        :param file_handler: TextIOWrapper - File handler object
        :param date_time_length: Integer - Indicates the beginning of the string after the datetime section
        :param date_time_format: String - Points to strftime format to parse string to datetime object
        :param datetime_search_criteria: List - Contains all datetime search criteria
        This method iterates line-by-line over a file handler using a generator.
        Each line is stripped from CRLF and split using a space delimiter and sent to a collections.Counter
        """

        for line in file_handler:
            datetime_string = datetime.strptime(line[:date_time_length+1], date_time_format)
            for criteria in datetime_search_criteria:
                if not isinstance(criteria, tuple):  # Not a range
                    if criteria == datetime_string:
                        self._counter += Counter(line[date_time_length+1:].strip().split(' '))
                else:  # If range
                    if criteria[0] <= datetime_string <= criteria[1]:
                        self._counter += Counter(line[date_time_length+1:].strip().split(' '))

    def file_word_count(self, filename, datetime_search_criteria):
        """
        :param filename: String - Absolute path to filename
        :param datetime_search_criteria: List - Contains all datetime search criteria
        :return: collections.Counter object
        """
        self.logger.debug('Reading file {0}'.format(filename))
        with open(filename, 'rt', encoding='utf-8') as file_handler:
            _parsed_datetime, _datetime_format = DateParser().determine_file_date_format(file_handler)

            if _parsed_datetime:
                self.read_lines_from_file(file_handler=file_handler,
                                          date_time_length=_parsed_datetime,
                                          date_time_format=_datetime_format,
                                          datetime_search_criteria=datetime_search_criteria)

        return self._counter
