import re
from singleton_decorator import singleton


@singleton
class KnownDateFormats:
    """This class holds all handled date formats.
    Values for each key hold known files under /var/log/ that correspond with the file format"""
    def __init__(self):
        self.yyyymmddhhmmssfff = re.compile('\[\d+-\d+-\d+.\d+:\d+:\d+,\d+\]')
        self.DDDMMMddhhmmssIDTYYYY = re.compile(r'.+\d+:\d+:\d+\sIDT\s\d+')
        self.DDDMMMddhhmmss = re.compile(r'\w{3,3}\s\w{3,3}\s\d+:\d+:\d+')
        self.MMMddhhmmss = re.compile(r'\w{3,3}\s\d+\s:\d+:\d+')
        self.DDMMMYYYYHHMMSS = re.compile('\[\d+/\w+/\d+:\d+:\d+:\d+\]')
        self.format_matcher = {
                                self.yyyymmddhhmmssfff: '[%Y-%m-%d %H:%M:%S,%f]',  # anaconda
                                self.DDMMMYYYYHHMMSS: '[%d/%b/%Y:%H:%M:%S]',
                                self.DDDMMMddhhmmssIDTYYYY: '%a %b %d %H:%M:%S IDT %Y',  # dracut,httpd
                                self.MMMddhhmmss: '%b %d %H:%M:%S',  # secure,messages,cron,yum.log,maillog
                                self.DDDMMMddhhmmss: '%a %b %d %H:%M:%S'  # secure,messages,cron,yum.log,maillog
                            }
