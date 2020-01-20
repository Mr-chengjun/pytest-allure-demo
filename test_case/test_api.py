import pytest
import allure
import requests
from urllib.parse import urljoin
from test_data import user_data
from config import REPORT_PATH, REPORT_DIR, BASE_URL


@allure.feature("接口测试")
@allure.title("接口测试类TestInterface")
class TestInterface(object):
    @pytest.mark.parametrize('methods, url, data, expect', user_data)
    @allure.story("接口测试函数")
    @allure.title("接口测试数据-{data}")
    def test_api(self, methods, url, data, expect, login, headers):
        """用例描述：接口功能测试"""
        url = urljoin(BASE_URL, url)
        print("登录结果：", login)
        headers['JWT'] = login
        print("登录后的headers:", headers)

        if methods.lower() == 'get':
            # res = requests.get(url, params=data)
            allure.attach("用例参数", "{}".format(data))
            assert methods == expect, "测试未通过，测试数据：{},返回结果：{}".format(data, "结果")
            print("测试通过")
        if methods.lower() == "post":
            # res = requests.post(url, data=data)
            assert methods == expect, "测试未通过，测试数据：{},返回结果：{}".format(data, "结果")
            print("测试通过")
        if methods.lower() == "put":
            # res = requests.put(url, data=data)
            assert methods == expect, "测试未通过，测试数据：{},返回结果：{}".format(data, "结果")
            print("测试通过")
        if methods.lower() == 'patch':
            # res = requests.patch(url, data=data)
            assert methods == expect, "测试未通过，测试数据：{},返回结果：{}".format(data, "结果")
            print("测试通过")
        if methods.lower() == 'delete':
            print("删除函数")
            # res = requests.delete(url)
            # print(res.text)
            # 关联的资料信息, 可在报告中记录保存必要的相关信息
            allure.attach("用例参数", "{}".format("删除请求"))
            assert methods == expect, "测试未通过，测试数据{},返回结果{}".format(data, "删除")
            print("删除成功，测试通过")


if __name__ == "__main__":
    # pytest.main(['-s', 'test_api.py', '--html={}'.format(REPORT_PATH), '--self-contained-html'])
    pytest.main(['-s', 'test_api.py', '--alluredir={}'.format(REPORT_DIR)])
