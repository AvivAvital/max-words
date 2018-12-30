from logger import Logger
from collections import Counter
from dateParser import DateParser


class FileHandler(Logger):
    """
    As the name suggests, this object handles all interactions of a given file
    Each object reports the current thread name and holds
    """
    def __init__(self):
        super().__init__()
        self._counter = Counter()

    def read_lines_from_file(self, file_handler, date_time_length):
        """
        :param file_handler: TextIOWrapper - File handler object
        This method iterates line-by-line over a file handler using a generator.
        Each line is stripped from CRLF and split using a space delimiter and sent to a collections.Counter
        """
        for line in file_handler:
            self._counter += Counter(line[date_time_length:].strip().split(' '))

    def file_word_count(self, filename):
        """
        :param filename: String - Absolute path to filename
        :return: collections.Counter object
        """
        self.logger.debug('Reading file {0}'.format(filename))
        with open(filename, 'rt', encoding='utf-8') as file_handler:
            _parsed_datetime = DateParser(file_handler).is_date_format_known()
            if _parsed_datetime:
                self.read_lines_from_file(file_handler=file_handler, date_time_length=_parsed_datetime)

        return self._counter
