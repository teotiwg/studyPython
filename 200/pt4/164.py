url = 'https://play.google.com/movies?hl=ko'

tmp = url.split('?')
query = tmp[1].split('&')
for q in query:
    print(q)