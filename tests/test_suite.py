from proj_maths.views import hello

def test(rf):
    request = rf.get('/hello')
    response = hello(request)
    assert 'Hello' in response.content.decode('utf-8')
    assert response.status_code == 200