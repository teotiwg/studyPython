add = lambda x,y: x+y
ret = add(1,3)
print(ret)

funcs = [lambda x: x + '.pptx', lambda x: x+ '.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

names = {'Mary':11000, 'Sam':2111, 'Amy':9888, 'Tom':20243, 'Mike':27115, 'Bob':5888,'Kelly':7888}
ret3 = sorted(names.items(), key = lambda x: x[0])
print(ret3)