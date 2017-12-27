from urllib.request import urlopen

url  = "https://s.taobao.com/search?q=computer&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
response = urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)