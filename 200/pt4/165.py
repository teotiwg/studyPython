mystack = []

def putdata(data):
    global mystack
    mystack.append(data)

def popdata():
    global mystack
    if len(mystack) ==0:
        return 0
    return mystack.pop()

putdata('Data1')
putdata([3,4,5,6])
putdata(12345)

print('<스택상태>: ', end='')
print(mystack)

ret = popdata()
while ret != None:
    print('스택에서 데이터 추출 ->:', end='')
    print(ret)
    print('<스택상태>', end='')
    print(mystack)
    ret = popdata()