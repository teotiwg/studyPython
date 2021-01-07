ch = input('문자 1개를 입력하세요')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자: %s \t 코드값: %d[%s]' %(ch, chv, hex(chv)))