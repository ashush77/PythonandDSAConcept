ListOfNames = ["ashu","rahul","akash"];
print(ListOfNames);

ListOfCity = []
ListOfCity.append("Meerut");
ListOfCity.append("Delhi");
ListOfCity.append("Gurugram");
ListOfCity.append("Kanpur");

print(ListOfCity[3]);

print(ListOfCity[0:2]);

for city in ListOfCity:
 print(city);

print("For loop with logic");


for i in range(0,len(ListOfCity)):
 print(ListOfCity[i])