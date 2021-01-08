from time import localtime

t = localtime()
startDay = '%d-01-01' %t.tm_year
elapsedDay = t.tm_yday

print('오늘은 %s 이후 %d일째 되는 날이다.' %(startDay, elapsedDay))