#-*-coding:utf-8-*-
import requests
     
     
# 1.Github项目及API接口数据
     
# api = 'https://api.github.com/repos/hubastard/nebula'




     
# req = requests.get(url)


sckey = ''
if "SCKEY" in os.environ:
    sckey = os.environ["SCKEY"]
    print(sckey)


def sendMessage(title, desp):
    data = {'text': title, 'desp': desp}
    serverJiang = 'http://sc.ftqq.com/' + sckey + '.send'
    response = requests.post(serverJiang, data=data)
    response.encoding = 'utf-8'
    print(response.text)

def init():
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
    location = res.headers['Location']
    # location = 'https: // github.com/hubastard/nebula/releases/tag/v0.7.10'
    locationurls = location.split('/')
    v = locationurls[len(locationurls)-1]
    if v != 'v0.7.10':
        print(v)
        sendMessage('联机mod更新啦', '版本为：'+v)

init()
