from argumentParser import ArgParser
from wordCounter import WordCounter


class MustParser(ArgParser):
    def __init__(self):
        super().__init__()
        self.parser.add_argument('file_or_dir',
                                 nargs='*',
                                 help='Absolute path to file(s) or directory/directories')

    def parse(self):
        self.args = self.parser.parse_args()
        word_count = WordCounter()
        result = word_count.count_must(self.args.num_of_words, *self.args.file_or_dir)
        word_count.print_results(result)
