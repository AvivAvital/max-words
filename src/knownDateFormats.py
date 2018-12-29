import re
from singleton_decorator import singleton


@singleton
class KnownDateFormats:
    def __init__(self):
        self.MMMddhhmmss = re.compile(r'.+\d*:\d*:\d*')
        self.DDDMMMddhhmmssIDTYYYY = re.compile(r'.+\d*:\d*:\d*\sIDT\s\d*')
        self.yyyymmddhhmmssfff = re.compile(r'(?<=[)\d*:\d*:\d*,\d*(?=])')
        self.format_matcher = {
                                self.yyyymmddhhmmssfff: 'anaconda',
                                self.DDDMMMddhhmmssIDTYYYY: ['dracut', 'httpd'],
                                self.MMMddhhmmss: ['secure', 'messages', 'cron', 'yum.log', 'maillog']
                            }
