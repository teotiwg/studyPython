solar= ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
planet = 'mars'
pos = solar.index(planet)
solar[pos] = '화성'
print(solar)