import os
from os.path import exists

dirName = input('새로 생성할 디렉터리 이름을 입력하세요')
if not exists(dirName):
    os.mkdir(dirName)
    print(' %s 디렉터리를 생성했습니다.' %dirName)
else:
    print('%s 은(는) 이미 존재합니다.' %dirName)