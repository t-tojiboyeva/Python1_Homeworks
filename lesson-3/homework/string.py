fruit_list=["apple", "banana", "cherry","berries","lemon"]
print(fruit_list[2])
list1=[12,34,56,67, 2, 9]
list2=[3,5,6,9,12,34]
list1.extend(list2)
print(list1)
num_list=[2,4,6,8,10,12,14,18]
new_list=[num_list[0],num_list[len(num_list)//2],num_list[-1]]
print(new_list)
tom_hanks_movies = [
    "Forrest Gump",
    "Saving Private Ryan",
    "Cast Away",
    "The Green Mile",
    "Apollo 13",
    "Catch Me If You Can",
    "Big",
    "Toy Story",
    "Philadelphia",
    "Captain Phillips",
    "A Beautiful Day in the Neighborhood",
    "Bridge of Spies",
    "Sully",
    "Road to Perdition",
    "The Terminal"
]

tom_hanks_movies_tuple=tuple(tom_hanks_movies)

print(tom_hanks_movies_tuple)

european_capitals = [
    "Paris",  # France
    "Berlin",  # Germany
    "Madrid",  # Spain
    "Rome",  # Italy
    "Vienna",  # Austria
    "Amsterdam",  # Netherlands
    "Lisbon",  # Portugal
    "Oslo",  # Norway
    "Athens",  # Greece
    "Warsaw"  # Poland
]
if "Paris" in european_capitals:
    print("Yes, 'Paris' is in the fruits list")
else:
    print(" it is not included")
numlist=[1,3,5,7,9,11,13]
mylist=numlist.copy()
print(mylist)
numlist=[1,3,5,7,9,11,13]
numlist[0],numlist[-1]=numlist[-1],numlist[0]
print(numlist)
numbers=[1,2.3,4,5,6,7,8,9,10]
print (numbers[3:7])
colors = ["red", "green", "blue", "yellow", "blue", "black", "white", "blue", "purple", "orange"]

count_blue=colors.count("blue")
print (count_blue)

animals = ("lion", "tiger", "elephant", "giraffe", "zebra", "cheetah", "bear", "wolf", "kangaroo", "panda")
x=animals.index("lion")

print(x)

tuple1=(1,3,5,7)
tuple2=(2,4,6,8)
result=tuple1+tuple2
print(result)
list1= ["apple", "banana", "cherry", "orange"]
tuple1=("apple", "banana", "cherry", "orange")
print(len(list1))
print(len(tuple1))
tuple=("apple", "banana", "cherry", "orange")
converted_list=list(tuple)
print(converted_list)
new_numbers=(1,2,3,4,5,6,7,8,9,10)
print(min(new_numbers))
print(max(new_numbers))
words_tuple = ("one", "two", "three", "four")

reversed_elements_tuple = tuple(word[::-1] for word in words_tuple)

print(reversed_elements_tuple)
