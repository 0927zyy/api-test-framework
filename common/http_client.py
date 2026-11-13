import requests
class HttpClient:
    # 统一请求封装，项目里所有请求都通过这个类发出
    def __init__(self,base_url,timeout=10):
        self.base_url=base_url
        self.timeout=timeout
        self.session=requests.Session()
    def post_json(self,path,payload):
        # 发POST请求体为json格式
        url=self.base_url+path
        return self.session.post(url,json=payload,timeout=self.timeout) 
    def post_form(self,path,payload):
        # 发送POST请求体为表单格式
        url=self.base_url+path
        return self.session.post(url,data=payload,timeout=self.timeout) 
    def get(self,path,params=None):
        # 发GET
        url=self.base_url+path
        return self.session.get(url,params=params,timeout=self.timeout)
    