val = input('문자 코드값을 입력하세요')
val = int(val)

try:
    ch = chr(val)
    print('코드값: %d[%s], 문자: %s' %(val, hex(val), ch))
except ValueError:
    print('입력한 %d라는 문자는 존재 않습니다.' %val)