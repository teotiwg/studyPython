tuple1 = (1,2,3,4,5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1,2,3,4,5], ['a','b','c'])
tuple1[0] = 6

def myfunc():
    print("Hello")

tuple4 = (1,2, myfunc)
tuple4[2]()