from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요: ' %target_file)
rename(target_file, newname)
print('[%s] -> [%s] 로 파일명이 변경됐습니다.' %(target_file, newname))