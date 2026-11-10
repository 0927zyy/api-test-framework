import pytest
import requests

@pytest.fixture
def post_response():
    # 公共fixture：发送一次POST请求给需要它的用例
    print("\n>>>fixture被执行了")
    return requests.post("https://httpbin.org/post", json={"username": "test"})