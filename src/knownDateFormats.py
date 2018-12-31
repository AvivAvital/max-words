import re
from singleton_decorator import singleton


@singleton
class KnownDateFormats:
    """This class holds all handled date formats.
    Values for each key hold known files under /var/log/ that correspond with the file format"""
    def __init__(self):
        self.yyyymmddhhmmssfff = re.compile('\[\d*-\d*-\d*.\d*:\d*:\d*,\d*\]')
        self.DDDMMMddhhmmssIDTYYYY = re.compile(r'.+\d*:\d*:\d*\sIDT\s\d*')
        self.MMMddhhmmss = re.compile(r'.+\d*:\d*:\d*')
        self.format_matcher = {
                                self.yyyymmddhhmmssfff: '[%Y-%m-%d %H:%M:%S,%f]',  # anaconda
                                self.DDDMMMddhhmmssIDTYYYY: '%a %b %d %H:%M:%S IDT %Y',  # dracut,httpd
                                self.MMMddhhmmss: '%a %b %d %H:%M:%S'  # secure,messages,cron,yum.log,maillog
                            }
