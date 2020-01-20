import sys
import pytest
import os

from config import REPORT_PATH, ROOT_DIR, REPORT_DIR


def main():
    # print("sys.path: ", sys.path)
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)

    # 执行用例
    # --reruns:失败重复执行多少次
    # args = ['--html={}'.format(REPORT_PATH), '--self-contained-html']  # 通过pytest-html生成报告
    args = ['--alluredir={}'.format(REPORT_DIR)]  # 通过allure生成json  REPORT_DIR：测试结果数据所在目录
    pytest.main(args)
    # with open('allure-results/environment.properties', 'a', encoding='utf8')as f:
    #     f.write(os.system("pip freez"))
    os.system('pip freeze > allure-results/environment.properties')
    # 生成html allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean
    os.system("allure generate allure-results/ -o allure-reports/ --clean")


if __name__ == '__main__':
    main()
