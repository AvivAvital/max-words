import pytest
import os
import logging
from src.wordCounter import WordCounter


class Helper(object):
    def __init__(self):
        self.test_name = os.path.basename(__file__)
        self.test_dir = os.path.join(os.getcwd(), 'test_resources', self.test_name)
        self.test_log = ''.join([self.test_name, '.log'])
        logging.basicConfig(level=logging.INFO, filename=self.test_log, format='%(levelname)s %(threadName)s %(message)s')
        self.logger = logging.getLogger(__name__)
        self.word_counter = WordCounter()

    def execute(self, *handles):
        return self.word_counter.count_must(*handles)

    def print_results(self, result):
        return self.word_counter.print_results(result)


@pytest.fixture(scope='module')
def test_helper():
    return Helper()


class TestBasic(object):
    @pytest.fixture(autouse=True)
    def before_after(self, test_helper):
        try:
            os.remove('report.html')
        except FileNotFoundError:
            pass

        test_helper.test_name = os.path.basename(__file__)
        yield

    @pytest.mark.parametrize('num_of_words, filenames, expected', [
        pytest.param(5, ['five_repetative_items.txt'], [('suntan', 5), ('expenditure', 4), ('tropical', 4), ('kick', 3), ('shatter', 2)],id='test_one_file_5_most_common'),
        pytest.param(1, ['five_repetative_items.txt','ten_items_with_two_known.txt'], [('suntan', 6)], id='test_two_file_most_common_word'),
        pytest.param(1, ['.'], [('tropical', 9)], id='test_recursive_most_common_word'),
        pytest.param(2, ['.'], [('tropical', 9), (u'состязание', 8)], id='test_recursive_with_unicode_most_common_word')
    ])
    def test_basic(self, test_helper, num_of_words, filenames, expected):
        files = [os.path.join(os.path.splitext(test_helper.test_dir)[0], filename) for filename in filenames]
        assert test_helper.execute(num_of_words, *files) == expected
