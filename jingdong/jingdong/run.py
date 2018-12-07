"""
__author__ = 'lss'
"""
from scrapy import cmdline
name = 'phone1'
cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())
