from random import shuffle

male=['superman', 'batman', 'ironman', 'captain', 'thor']
female = ['wonderwoman', 'catwoman', 'blackwidow', 'agentcarter', 'thorgirl']

shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
    print('커플 %d: %s - %s' %(i+1,couple[0],couple[1]))