import array

a=array.array('i',[4,5,6])
print(a)

a.append(67)
print(a)

a.pop(2)
print(a)

for i in range(0,1):
    a.append(100)
    print(a)