import pytest
from common.http_client import HttpClient
from apis.httpbin_api import HttpbinApi

@pytest.fixture(scope="session")
def api():
    # 全局api对象，所有用例写参数名，api即可使用
    client=HttpClient("https://httpbin.org")
    return HttpbinApi(client)