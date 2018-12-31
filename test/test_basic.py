import pytest
import os
import logging
from src.advantageArgumentParser import AdvantageParser
from exceptionHandler import *


class Helper(object):
    def __init__(self):
        self.test_name = os.path.basename(__file__)
        self.test_dir = os.path.join(os.getcwd(), 'test_resources', self.test_name)
        self.test_log = ''.join([self.test_name, '.log'])
        logging.basicConfig(level=logging.INFO, filename=self.test_log, format='%(levelname)s %(threadName)s %(message)s')
        self.logger = logging.getLogger(__name__)
        self.argument_parser = AdvantageParser()

    def execute(self, num_of_words, date_or_timestamp, path):
        return self.argument_parser.do_count(num_of_words, date_or_timestamp, path)


@pytest.fixture(scope='module')
def test_helper():
    return Helper()


class TestBasic(object):
    @pytest.fixture(autouse=True)
    def before_after(self, test_helper):
        test_helper.test_resources = os.path.join(os.getcwd(), 'test_resources')
        try:
            os.remove('report.html')
        except FileNotFoundError:
            pass

        test_helper.test_name = os.path.basename(__file__)
        yield

    @pytest.mark.parametrize('num_of_words, date_or_timestamp, path, expected', [

    pytest.param(3, ['1300000000-1300000001'], os.path.join(os.getcwd(), 'test_resources'), [
        ('This', 3), ('Should', 3), ('Appear', 3)],
                 id='Test epoch range'),

    pytest.param(6, ['Sat Mar 12 00:00:00 IDT 2011-Mon Mar 14 00:00:00 IDT 2011'], os.path.join(os.getcwd(),
        'test_resources'), [
        ('This', 3), ('Should', 3), ('Appear', 3), ('Also', 3), ('Range', 3), ('Here', 3)],
                 id='Test Datetime range'),

    pytest.param(6, ['Wed Dec 12 00:00:00 IDT 2018-Wed Dec 12 10:52:39 IDT 2018'], os.path.join(os.getcwd(),
        'test_resources'), [
        ('состязание', 9), ('автограф', 5), ('обнаружение', 4), ('совокупление', 4), ('дружеский', 3)],
                 id='Test Datetime range with unicode'),

    pytest.param(2, ['Sun Aug 30 14:32:28 IDT 2015-Sun Aug 30 14:32:36 IDT 2015'], os.path.join(os.getcwd(),
        'test_resources'), [('tropical', 6), ('discriminate', 1)], id='Test different datetime format'),


    pytest.param(2, ['Sun Aug 30 14:32:28 IDT 2015-Sun Aug 30 14:32:36 IDT 2015','Wed Dec 12 00:00:00 IDT 2018-Wed Dec 12 10:52:39 IDT 2018'],
        os.path.join(os.getcwd(),'test_resources'), [('состязание', 9), ('tropical', 6)],
                id='Test Datetime ranges with unicode'),
    ])
    def test_functional(self, test_helper, num_of_words, date_or_timestamp, path, expected):
        result = test_helper.execute(num_of_words, date_or_timestamp, path)
        assert result == expected

    @pytest.mark.parametrize('num_of_words, date_or_timestamp, path, expected', [
    pytest.param(2, ['1300000001-1300000000'], os.path.join(os.getcwd(), 'test_resources'), InvalidRangeException,
                 id='Test invalid epoch range exception')])
    def test_exception(self, test_helper, num_of_words, date_or_timestamp, path, expected):
        with pytest.raises(expected_exception=expected):
            test_helper.execute(num_of_words, date_or_timestamp, path)
