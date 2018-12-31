import multiprocessing
from sys import getsizeof
from concurrent.futures import ThreadPoolExecutor, as_completed
from directoryHandler import DirectoryHandler
from fileHandler import FileHandler
from collections import Counter
from logger import Logger
from os.path import isfile, abspath


class WordCounter(Logger):
    def __init__(self):
        super().__init__()
        self.most_common_words = 0

    def count_must(self, most_common_words, *args):
        """
        :param most_common_words: Integer - Number of most common words in all files
        :return: Integer - Number of most common words
        """

        _counter = Counter()
        self.most_common_words = most_common_words
        _root_dir = DirectoryHandler()
        for path in map(abspath, args):
            if isfile(path):
                _counter += FileHandler().file_word_count(filename=path)
            else:
                with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
                    future_file_counts = {executor.submit(FileHandler().file_word_count, _filename):
                                              _filename for _filename in _root_dir.scan_dir(path)}

                    for future in as_completed(future_file_counts):
                        _counter += future.result()

        self.logger.debug("size of counter is {0} MB".format(round(getsizeof(_counter) / 1024 / 1024), 3))
        return _counter.most_common(self.most_common_words)

    def count_advantage(self, most_common_words, datetime_search_criteria):
        """
        :param most_common_words: Integer - Number of most common words in all files
        :param datetime_search_criteria: List - Contains all items/ranges of datetime to look for in directory
        :return: Integer - Number of most common words
        """

        _counter = Counter()
        self.most_common_words = most_common_words
        _root_dir = DirectoryHandler()
        _path = r'C:\git\word_count\max-words\test\test_resources\test_basic\subdir\unicode_subdir'

        with ThreadPoolExecutor(max_workers=2) as executor:
            future_file_counts = {executor.submit(FileHandler().file_word_count, _filename, datetime_search_criteria):
                                      _filename for _filename in _root_dir.scan_dir(_path)}

            for future in as_completed(future_file_counts):
                _counter += future.result()

        self.logger.debug("size of counter is {0} MB".format(round(getsizeof(_counter) / 1024 / 1024), 3))
        return _counter.most_common(self.most_common_words)

    def print_results(self, result):
        """
        :param result: collections.Counter - Contains results from wordCounter.count()
        """

        self.logger.info('Maximum​ ​{0}​ ​words:'.format(self.most_common_words))
        for word in result:
            self.logger.info('Word {0} occurred {1} times'.format(*word))
