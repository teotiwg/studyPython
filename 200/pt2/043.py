import time
import mylib

print('5초간 프로그램을 정지합니다.')
time.sleep(5)
print('5초가 지났습니다.')

ret1 = mylib.add_txt('Korea', 'The Best')
ret2 = mylib.reverse(1, 2, 3)
print(ret1)
print(ret2)
