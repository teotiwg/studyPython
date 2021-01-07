names = {'Mary':10999, 'Sam':2111, 'Amy':9778, 'Tom':20245, 'Mike':27115, 'Bob':5887, 'Kelly':7855}
ks = names.keys()
print(ks)

for k in ks:
    print("Key: %s Value: %d" %(k, names[k]))
