import re
from argumentParser import ArgParser
from logger import Logger
from wordCounter import WordCounter
from dateParser import DateParser
from exceptionHandler import InvalidDateTimeException, InvalidDateTimeRangeException
from datetime import datetime


class AdvantageParser(ArgParser):
    def __init__(self):
        super().__init__()
        self.parser.add_argument('date_or_timestamp',
                                 nargs='*',
                                 type=str,
                                 help='')

        self.parser.add_argument('--debug',
                                 action='store_true',
                                 default=False,
                                 help='Activate debug logs')

    @staticmethod
    def is_datetime_or_epoch(item):
        """
        This method examines a string and determines if it is a valid datetime or epoch
        :param item: String - Holds a datetime string or an epoch range
        :return: Tuple - Either (int, datetime) if datetime or (int,None) if epoch
        :raises InvalidDateTimeException if not a valid string
        """
        if not item.isdigit():
            _end_pos, _strftime_string = DateParser().is_date_format_known(item)
            if not _end_pos:
                raise InvalidDateTimeException
            return _end_pos, datetime.strptime(item, _strftime_string)
        return int(item), None

    def is_range(self, item):
        """
        This method examines a string and determines if it is a valid datetime or epoch range
        :param item: String - Either holds a datetime/epoch string or a datetime/epoch range, separated by dash (-)
        :return: Tuple - Either Integer or Datetime objects
        :raises InvalidDateTimeRangeException if not a valid range
        """
        if '-' not in item:
            return self.is_datetime_or_epoch(item)

        _beg, _end = map(self.is_datetime_or_epoch, item.split('-'))  # If either invalid, raise exception
        if _beg[1] and _end[1]:
            return _beg, _end
        elif not (_beg[1] and _end[1]):
            return _beg[0], _beg[0]  # Only return beginning and end of epoch range
        raise InvalidDateTimeRangeException

    def parse(self):
        self.args = self.parser.parse_args()
        if self.args.debug:
            Logger.__init__(self, log_level='DEBUG')

        time_and_date_ranges = self.args.date_or_timestamp.split(',')
        word_count = WordCounter()
        result = ''

        for item_range in time_and_date_ranges:
            range_handler = self.is_range(item_range)
            if not range_handler[1]:
                # Single epoch
                result = word_count.count_advantage(self.args.num_of_words, single_epoch=range_handler[0])

            elif isinstance(range_handler[1], datetime):
                # Single datetime
                result = word_count.count_advantage(self.args.num_of_words, single_datetime=range_handler)

            elif isinstance(range_handler[1], tuple):
                if isinstance(range_handler[1][0], int):
                    # Multiple epoch
                    result = word_count.count_advantage(self.args.num_of_words, multi_epoch=range_handler[1])

                elif isinstance(range_handler[1][1], datetime):
                    # Multiple datetime
                    result = word_count.count_advantage(self.args.num_of_words, multi_datetime=range_handler[1])
                    word_count.print_results(result)
                else:
                    raise InvalidDateTimeRangeException

        word_count.print_results(result)



