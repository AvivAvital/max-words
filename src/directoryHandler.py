import os
from logger import Logger


class DirectoryHandler(Logger):
    def __init__(self, max_dir_depth):
        """
        :param max_dir_depth: Maximum number of sub directories
        :param file_extension: Filter by file extension
        """
        super().__init__(log_level='WARNING')
        self.MAX_DIR_DEPTH = max_dir_depth

    def scan_dir(self, dir_path):
        """
        :param dir_path: String - Absolute path to directory where files reside.
        :return: Generator - Absolute path to files under given directory, within max_dir_depth.
        """

        for entry in os.scandir(dir_path):
            if entry.is_file():
                yield os.path.abspath(os.path.join(entry.path))
            elif entry.is_dir():
                if self.MAX_DIR_DEPTH > 0:
                    self.MAX_DIR_DEPTH -= 1
                    yield from self.scan_dir(entry.path)
                else:
                    self.logger.warning('File tree is too big to fit all files. Please increase max_dir_depth')
