import logging


class Logger(object):
    def __init__(self, log_level='INFO', log_format='%(asctime)s %(levelname)s %(threadName)s %(message)s'):
        """
        :param log_level: String (default INFO)
        :param log_format: Log format - Default: [Date Time LogLevel ThreadName Message]
        """
        self.log_level = logging.getLevelName(log_level)
        self.log_format = log_format

        logging.basicConfig(level=self.log_level, format=self.log_format)
        self.logger = logging.getLogger(__name__)
