from datetime import datetime
import os

# 请求的url
BASE_URL = 'http://192.168.0.185:7012'
# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'allure-results')

# 测试数据所在目录
TEST_DATA_PATH = os.path.join(ROOT_DIR, 'test_data', 'testdata.xlsx')

# 当前时间
CURRENT_TIME = datetime.now().strftime('%Y%m%d%H%M%S')

# 报告名称
REPORT_NAME = '{}.html'.format(CURRENT_TIME)

# 报告的绝对路径
REPORT_PATH = os.path.join(REPORT_DIR, REPORT_NAME)

