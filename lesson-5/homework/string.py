def leap_year(n):
    if (n%4==0 and n%100!=0 )or n%400==0:
        return True
    else:
        return False

n=int(input("Enter a year:"))
print(leap_year(n))

n=int(input("enter an integer:"))
if n%2==1:
    print("Weird")
elif n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")

def find_even_numbers_with_if_else(a, b):
    even_numbers = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

a = 3
b = 10
print(find_even_numbers_with_if_else(a, b))  

def find_even_numbers_without_if_else(a, b):
    return [num for num in range(a, b + 1) if num % 2 == 0]


a = 7
b = 23
print(find_even_numbers_without_if_else(a, b))  
 
