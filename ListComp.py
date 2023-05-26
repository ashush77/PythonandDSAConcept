ListOfNum = [];

ListOfNum.append(10);
ListOfNum.append(12);
ListOfNum.append(4);
ListOfNum.append(5);

for i in range(0,4):
    print(ListOfNum[i])

    for num in ListOfNum:
        print(num);

# List comprehension

ListOfArray = []

for i in range(10,21):
    ListOfArray.append(i)
        
print(ListOfArray);

ListOfInt = [i for i in range(10,21)]

print(ListOfInt)