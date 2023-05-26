list=[]

for i in range(1,10):
    list.append(i)
print(list)

listCom=[i for i in range(1,10)]
print(listCom)

dic={}
for i in range(1,5):
    dic.update({i:i*i})
print(dic)

dicCom={i:i*i for i in range(1,5)}
print(dicCom)

def even_list(n):
    list_even=[]
    for i in range(0,n):
        if i%2==0:
            list_even.append(i)
    return list_even
    
print(even_list(10))

even = lambda n:list(range(0,n,2))
print(even_list(20))
