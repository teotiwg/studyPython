solar1 = ['일', '수', '금', '지','화','목','토','천','해']
solar2 = ['sun', 'mer','ven','ear','mar','jup','sar','ura','nep']
solardict={}
for i, k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val

print(solardict)