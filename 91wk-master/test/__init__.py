import requests


def test_uploadavator():
    url = 'http://192.168.1.100:9001/upload_avator/'
    data = {
        'token': '123'
    }
    files = {
        'img': ('aaa.jpg', open(r'E:\Pycharm\WKF\aaa.jpg', 'rb'), 'image/jpg'),
    }
    resp = requests.post(url, data=data, files=files)
    resp_data = resp.json()
    print(resp_data)
    assert resp_data.get('code') == 200
    print('ok')


def test_get_img_url(key, type=0):
    resp = requests.get('http://192.168.1.100:9001/img_url/%s?type=%s' % (key, type))
    print(resp.json())


if __name__ == '__main__':
    # test_uploadavator()
    test_get_img_url('1527ae31d7e04280bef1fb3f772d520e')