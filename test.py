i = 0

def func_complique(x):
    print(x * 2)

def hey(n:int,x:int):
    """test
    n: test1
    x: test2"""
    global i
    for i in range(n):
        x(i)

hey(3, lambda x : func_complique(x))

pout(test)
