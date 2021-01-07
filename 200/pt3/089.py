numstr = input('숫자를 입력하세요')
try:
    num = int(numstr)
    print("입력한 수는 정수 %d 입니다." %num)
except:
    try:
        num = float(numstr)
        print('입력한 수는 실수 %f 입니다.' %num)
    except:
        print('+++숫자를 입력하세요+++')