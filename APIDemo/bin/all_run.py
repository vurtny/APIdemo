import unittest
import time
from BeautifulReport import BeautifulReport


# 匹配用例
discover = unittest.defaultTestLoader.discover(start_dir='../case',
                                              pattern='test*.py',
                                              top_level_dir=None)

#生成报告
day = time.strftime("%Y%m%d%H%M%S")
filename = "report_%s.html" % day
runner = BeautifulReport(discover)
runner.report(filename=filename,
             description="接口自动化",
             report_dir="../report")