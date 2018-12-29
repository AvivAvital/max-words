from argparse import ArgumentParser, RawTextHelpFormatter
from wordCounter import WordCounter
from logger import Logger
from textwrap import dedent


class ArgParser(Logger):
    def __init__(self):
        self.parser = ArgumentParser(description='Find the most common words in given file/dir path(s)',
                                     formatter_class=RawTextHelpFormatter,
                                     usage='%(prog)s [-h] num_of_words filename_or_directory [filename_or_directory ...] [--debug]',
                                     epilog=dedent('''\
                                     Examples: 
                                     %(prog)s 3 ​/tmp​
                                     %(prog)s 5 ​​/home/user/file.txt
                                     %(prog)s 10 /var/log/ /tmp/file.txt
                                     %(prog)s -h
                                     '''))

        self.parser.add_argument('num_of_words',
                                 type=int,
                                 help='Amount of most common words returned')

        self.parser.add_argument('file_or_dir',
                                 nargs='*',
                                 help='Absolute path to file(s) or directory/directories')

        self.parser.add_argument('--debug',
                                 action='store_true',
                                 default=False,
                                 help='Activate debug logs')

        self.args = self.parser.parse_args()
        
        if self.args.debug:
            super().__init__(log_level='DEBUG')

        word_count = WordCounter()
        result = word_count.count(self.args.num_of_words, *self.args.file_or_dir)
        word_count.print_results(result)
