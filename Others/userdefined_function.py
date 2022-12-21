def additio(a,b):   #Function with no return value.
    print(a+b)
additio(10,20)

def addition(a,b): #Function with return value.
    '''First line of function is called as doc string.'''
    add = a+b
    return add
v = addition(45,2)
print(v)
print(addition.__doc__) #Printing doc string.
