import os
from logger import Logger


class DirectoryHandler(Logger):
    def __init__(self):
        super().__init__(log_level='INFO')

    def scan_dir(self, dir_path):
        """
        :param dir_path: String - Absolute path to directory where files reside.
        :return: Generator - Absolute path to files under given directory.
        """

        for entry in os.scandir(dir_path):
            if entry.is_file():
                yield os.path.abspath(os.path.join(entry.path))
            elif entry.is_dir():
                yield from self.scan_dir(entry.path)
