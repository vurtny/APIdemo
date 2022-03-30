import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

CASE_PATH = os.path.join(BASE_PATH, 'case')

DATA_PATH = os.path.join(BASE_PATH, 'data')

REPORT_PATH = os.path.join(BASE_PATH, 'report')

print("用例路径：", CASE_PATH)
