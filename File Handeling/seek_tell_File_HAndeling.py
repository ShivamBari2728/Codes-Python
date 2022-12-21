f = open ("demo.txt") #accessing file

print(f.tell())  #Tells the location of pointer 
print(f.readline())

print(f.tell()) #Tells the location of pointer 
print(f.readline())

print(f.seek(2)) #Set pointer at 2nd alphabet
print(f.readline())
f.close()