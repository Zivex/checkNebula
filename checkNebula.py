import requests
     
     
# 1.Github项目及API接口数据
     
# api = 'https://api.github.com/repos/hubastard/nebula'

url = 'https://github.com/hubastard/nebula/releases/latest'
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

res = requests.get(url, headers=HEADERS, allow_redirects=False)


     
# req = requests.get(url)


print(res.headers['Location'])

# requests.get(api).json()# 3.解析想要的数据，并打印cur_update = all_info['updated_at']print(cur_update)