import allure
import pytest
import yaml
import json


def load_form_cases():
    """从 yaml 数据文件读取表单接口的测试数据"""
    with open("data/httpbin_data.yaml", "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)["post_form_cases"]

    cases = []
    for item in raw:
        cases.append(
            pytest.param(item["form_value"], item["excepted"], id=item["case_name"])
        )
    return cases


@allure.feature("httpbin 接口")
@allure.story("POST /post 接口")
class TestHttpbinPost:
    """POST 接口测试集"""

    @allure.title("验证状态码返回 200")
    def test_post_json(self, api):
        # 验证状态码是200
        with allure.step("构造请求数据"):
            payload={"username":"test"}
            allure.attach(json.dumps(payload,ensure_ascii=False,indent=2),
                          name="请求参数",attachment_type=allure.attachment_type.JSON)
        with allure.step("发送POST请求"):
            res=api.post_json(payload)
            allure.attach(res.text,
                          name="响应内容", attachment_type=allure.attachment_type.JSON)
        with allure.step("断言状态码是200"):
            assert res.status_code==200,f"实际状态码:{res.status_code}"
        # res = api.post_json({"username": "test"})
        # assert res.status_code == 200, f"实际状态码：{res.status_code}"

    @allure.title("验证请求数据能原样回显")
    def test_post_echo(self, api):
        # 验证发送的数据能原样回显
        with allure.step("构造请求数据"):
            payload={"username":"test"}
        with allure.step("发送POST请求"):
            res=api.post_json(payload)
        with allure.step("断言回显"):
            body = res.json()
            assert body["json"]["username"] == "test", f"实际回显：{body['json']}"
        # res = api.post_json({"username": "test"})
        # body = res.json()
        # assert body["json"]["username"] == "test", f"实际回显：{body['json']}"

    @allure.title("验证表单格式传参：{form_value}")
    @pytest.mark.parametrize("form_value,expected", load_form_cases())
    def test_post_form(self, api, form_value, expected):
        # 参数化，传参走的是表单格式
        with allure.step("构造请求参数"):
            payload={"a":form_value}
            allure.attach(json.dumps(payload,ensure_ascii=False,indent=2),
                                      name="请求参数",attachment_type=allure.attachment_type.JSON)
        with allure.step("发送post请求"):
            res=api.post_form(payload)
            allure.attach(res.text,
                                      name="响应内容", attachment_type=allure.attachment_type.JSON)
        with allure.step("断言回显"):
            body = res.json()
            assert body["form"]["a"] == expected, f"实际回显：{body['form']['a']}"
        # res = api.post_form({"a": form_value})
        # body = res.json()
        # assert body["form"]["a"] == expected, f"实际回显：{body['form']['a']}"
        # 上面注释掉的三行是原来的用法，不带调用详情
