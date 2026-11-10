def test_second_file(post_response):
    # 证明:不import、不定义、直接就能用confest.py里的fixture
    assert post_response.status_code==200,f"实际状态码｛post_response.status_code｝"