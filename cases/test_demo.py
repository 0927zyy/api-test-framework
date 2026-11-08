import requests


def test_post_status():
    """验证状态码是 200"""
    response = requests.post("https://httpbin.org/post", json={"username": "test"})
    assert response.status_code == 200, f"实际状态码 {response.status_code}"


def test_post_echo():
    """验证发送的数据能原样回显"""
    response = requests.post("https://httpbin.org/post", json={"username": "test"})
    body = response.json()
    assert body["json"]["username"] == "test", f"实际回显 {body['json']}"


def test_post_form():
    '''验证data= 传参走的是表单格式'''
    response=requests.post("https://httpbin.org/post", data={"a": "1"})
    body=response.json()
    assert body["form"]["a"]=="1",f"实际回显{body['form']['a']}"
    assert "x-www-form-urlencoded" in body["headers"]["Content-Type"]