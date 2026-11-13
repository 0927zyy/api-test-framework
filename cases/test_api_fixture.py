def test_api_available(api):
    # 验证api fixture 能正常注入
    assert api is not None
    assert hasattr(api,"post_json")