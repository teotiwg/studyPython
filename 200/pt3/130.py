names = {'Mary':11000, 'Sam':2111, 'Amy':9888, 'Tom':20243, 'Mike':27115, 'Bob':5888,'Kelly':7888}
k = input('이름 입력: ')
if k in names:
    print('%s 는 %d 명입니다.' %(k, names[k]))
else:
    print('%s 라는 이름은 없습니다.' %k)