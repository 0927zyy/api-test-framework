# import pytest
import requests

# @pytest.fixture
# def post_response():
#     # 准备：发送一次POST请求，把响应对象交给用例使用
#     print("\n>>>fixture被执行了")
#     return requests.post("https://httpbin.org/post", json={"username": "test"})

# @pytest.fixture
# def post_response_status(post_response):
#     assert post_response.status_code == 200, f"实际状态码：{post_response.status_code}"
    
    
    
def test_post_status(post_response):
    """验证状态码是 200"""
    # response = requests.post("https://httpbin.org/post", json={"username": "test"})
    print(f"\nstatus 用例里的对象: {id(post_response)}")
    assert post_response.status_code == 200, f"实际状态码 {post_response.status_code}"


def test_post_echo(post_response):
    """验证发送的数据能原样回显"""
    # response = requests.post("https://httpbin.org/post", json={"username": "test"})
    print(f"echo 用例里的对象: {id(post_response)}")
    body = post_response.json()
    assert body["json"]["username"] == "test", f"实际回显 {body['json']}"


def test_post_form():
    '''验证data= 传参走的是表单格式'''
    response=requests.post("https://httpbin.org/post", data={"a": "1"})
    body=response.json()
    assert body["form"]["a"]=="1",f"实际回显{body['form']['a']}"
    assert "x-www-form-urlencoded" in body["headers"]["Content-Type"]