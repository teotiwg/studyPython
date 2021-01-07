utxt = 'I love Python'
btxt = utxt.encode()

print(utxt)
print(btxt)

ret1 = 'I'==utxt[0]
ret2 = 'I'==btxt[0]
print(ret1)
print(ret2)