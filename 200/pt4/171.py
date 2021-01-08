from urllib.request import urlopen

url = 'https://www.naver.com/'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('naverhome.html', 'w') as h:
        h.writelines(doc)