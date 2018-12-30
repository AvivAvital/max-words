from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from textwrap import dedent
from logger import Logger


class ArgParser(Logger):
    def __init__(self):
        super().__init__(log_level='INFO')
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

        self.args = Namespace()

    def parse(self):
        self.args = self.parser.parse_args()
