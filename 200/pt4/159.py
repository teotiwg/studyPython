from time import localtime

weekdays = ['월', '화', '수', '목', '금', '토', '일']

t = localtime()
today = '%d-%d-%d' %(t.tm_year, t.tm_mon,t.tm_mday)
week = weekdays[t.tm_wday]

print('%s 오늘은 %s 입니다' %(today, week))