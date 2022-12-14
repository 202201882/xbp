#ライブラリのインポート
from unicodedata import name
import requests
from bs4 import BeautifulSoup


#tenki.jpの目的の地域のページのURL（今回は東京都調布市）
url = 'https://tenki.jp/forecast/3/17/4610/14100/'

#HTTPリクエスト
r = requests.get(url)

#プロキシ環境下の場合は以下を記述
"""
proxies = {
    "http":"http://proxy.xxx.xxx.xxx:8080",
    "https":"http://proxy.xxx.xxx.xxx:8080"
}
r = requests.get(url, proxies=proxies)
"""

#HTMLの解析
bsObj = BeautifulSoup(r.content, "html.parser")

#今日の天気を取得
today = bsObj.find(class_="today-weather")
weather = today.p.string

#気温情報のまとまり
temp=today.div.find(class_="date-value-wrap")

#気温の取得
temp=temp.find_all("dd")
temp_max = temp[0].span.string #最高気温
temp_max_diff=temp[1].string #最高気温の前日比
temp_min = temp[2].span.string #最低気温
temp_min_diff=temp[3].string #最低気温の前日比

#結果の出力
print("天気:{}".format(weather))
print("最高気温:{} {}".format(temp_max,temp_max_diff))
print("最低気温:{} {}".format(temp_min,temp_min_diff))

#ここから私

最低気温=1
if 最低気温> 10: 
    print("はんそで")
else:
    print("ながそで")

    
#30　半袖
#25　半袖シャツ
#20　カーディガン
#15　セーター
#10 トレンチコート
#5　厚手のコート
#0　ダウンコート

