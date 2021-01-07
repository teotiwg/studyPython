solar = ['sun', 'mer', 'ven', 'ear', 'mar','jup','sat','ura','nep']
ret = list(enumerate(solar))
print(ret)

for i, body in enumerate(solar):
    print('%d번째 천체: %s' %(i,body))