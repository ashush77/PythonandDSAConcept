MyDict = {
    "Name":"Ashu Sharma",
     "Job":"IT",
    "City":"Meerut",

    "Hobby":"Play"
}

print(MyDict['Hobby']);

print(MyDict)

MyDict['Edu']="MCA"
print(MyDict)

print(MyDict.get('Edu'));

MyDict.update({"Salary":"20000"})

print(MyDict);

print(MyDict.keys())
print(MyDict.values())
print(MyDict.items())

for key,value in MyDict.items():
    print(key,value)

    for key in MyDict.keys():
        print(key)

        for value in MyDict.values():
            print(value)