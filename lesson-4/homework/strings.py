Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
student_scores={
    'Alex':88,
    'Ben': 75,
    'Cyrus': 93,
    'Denver': 85,
    'John': 84,
    'Mike': 33,
    'Anna': 61,
    'Sam': 45
}
sorted_by_values_asc=dict(sorted(student_scores.items(),key=lambda item:item[1],reverse=False))
sorted_by_values_desc=dict(sorted(student_scores.items(),key=lambda item:item[1],reverse=True))


print(sorted_by_values_asc)
print(sorted_by_values_desc)
2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.
thisdict={
    "a":10,
    "b":20,
}
thisdict["c"]=30
print(thisdict)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
resul1=dic1|dic2|dic3
print(resul1)
n=int(input("enter a number"))
squares={}
for x in range(1,n+1):
    squares[x]=x*x
print(squares)
n=15
sqrt={}
for x in range(1,n+1):
    sqrt[x]=x*x
print(sqrt)
fruit_set={"apple", "banana", "cherry", "apple"}
print(fruit_set)
fruit_set={"apple", "banana", "cherry", "apple"}
for fruit in fruit_set:
    print(fruit)
fruit_set={"apple", "banana", "cherry", "apple"}
fruit_set.add("orange")
print(fruit_set)
fruit_set={"apple", "banana", "cherry", "apple"}
fruit_set.discard("apple")
print(fruit_set)
fruit_set={"apple", "banana", "cherry", "apple"}
fruit_set.remove("apple")
print(fruit_set)
