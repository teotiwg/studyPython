solarsys = ['sun', 'mercury', 'venus', 'earth','mars', 'jupiter', 'saturn', 'uranus', 'neptune','earth']
planet = 'earth'

pos = solarsys.index(planet)
print('%s는 %d번째 위치'%(planet, pos))
pos = solarsys.index(planet , 5)
print('%s는 %d번째 위치'%(planet, pos))