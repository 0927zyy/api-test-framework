
class HttpbinApi:
    # httpbin项目的接口集合
    def __init__(self,client):
        self.client=client
        
    def post_json(self,payload):
        # post/post，json格式请求体
        return self.client.post_json("/post",payload)
    
    def post_form(self,payload):
        # post/post，表单格式请求体
        return self.client.post_form("/post",payload)
    
    def get_status(self, code):
        """GET /status/{code}，用于测异常状态码"""
        return self.client.get(f"/status/{code}")