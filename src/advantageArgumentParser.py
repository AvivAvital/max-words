from argumentParser import ArgParser
from logger import Logger
from wordCounter import WordCounter
from dateParser import DateParser
from exceptionHandler import *
from datetime import datetime


class AdvantageParser(ArgParser):
    def __init__(self):
        super().__init__()
        self.parser.add_argument('date_or_timestamp',
                                 # nargs='+',
                                 type=self.csv_list,
                                 help='timestamp/datetime format')  # Todo: Fix description

        self.parser.add_argument('--debug',
                                 action='store_true',
                                 default=False,
                                 help='Activate debug logs')

    @staticmethod
    def csv_list(string):
        return string.split(',')

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
            if not _beg[0] < _end[0]:
                raise InvalidRangeException
            return _beg, _end  # Only return beginning and end of epoch range
        raise InvalidDateTimeRangeException

    def decide_on_input(self, item_range):
        """
        This method tests for all valid single/multi-items and return date objects
        :param item_range: List/String - Either range (dash delimited), or singular item (String or datetime)
        :return: datetime object(s) - Either datetime, tuple(datetime_start,datetime_end)
        :raises InvalidDateTimeRangeException, InvalidDateTimeException or InvalidRangeException
        """
        range_handler = self.is_range(item_range)
        if not range_handler[1]:  # Single epoch
            return datetime.utcfromtimestamp(range_handler[0])

        elif isinstance(range_handler[1], datetime):  # Single datetime
            return range_handler[1]

        elif isinstance(range_handler, tuple):  # Multiple epoch
            if not range_handler[1][1]:
                _begin, _end = [datetime.utcfromtimestamp(item[0]) for item in range_handler]
                return _begin, _end

            elif isinstance(range_handler[1][1], datetime):  # Multiple datetime
                _begin, _end = [item[1] for item in range_handler]
                return _begin, _end
            else:
                raise InvalidDateTimeRangeException
        else:
            raise InvalidDateTimeException

    def parse(self):
        """
        :return: Parses command line arguments and return aggregated word count
        """
        self.args = self.parser.parse_args()
        word_counter = WordCounter()
        datetime_search_criteria = []
        if self.args.debug:
            Logger.__init__(self, log_level='DEBUG')

        if len(self.args.date_or_timestamp) == 1:
            item = self.args.date_or_timestamp.pop()
            datetime_search_criteria.append(self.decide_on_input(item))
        else:
            for item in self.args.date_or_timestamp:
                datetime_search_criteria.append(self.decide_on_input(item))

        result = word_counter.count_advantage(self.args.num_of_words, datetime_search_criteria)
        word_counter.print_results(result)
