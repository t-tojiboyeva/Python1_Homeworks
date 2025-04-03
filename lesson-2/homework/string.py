1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name=input("Enter your name:")
age=int(input("Enter your year of birth:"))
print(f"Dear {name}, you are {2025-age} years old this year ")
2. Extract Car Names
Extract car names from the following text:

txt = 'LMaasleitbtui'
txt="LMaasleitbtui"
print(txt[::2])
print(txt[1::2])

3. Extract Car Names
Extract car names from the following text:

txt = 'MsaatmiazD'
txt = 'MsaatmiazD'
print(txt[::-2])
print(txt[::2])
4. Extract Residence Area
Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt = "I'am John. I am from London"
print(txt.split()[-1])

5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.
word=input("Enter a word:")
print(f" Reverse of the word is {word[::-1]}")
6. Count Vowels
Write a Python program that counts the number of vowels in a given string.
text=input("enter a sentence:")
vowelcount=text.lower().count("a")+text.lower().count("o")+text.lower().count("e")+text.lower().count("i")+text.lower().count("u")
print(vowelcount)
7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))
print(f" Numbers: {numbers}, max num is {max(numbers)}")
8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word=input ("enter a word:")
reverse =word[::-1]
if word  ==reverse :
    print('this word is palindrome')
else:
    print("this word is not palindrome")
9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.
email=input(" Enter your gmail:")
print(f"  {email[email.index('@')+1:]}")
10.Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.
import random 
import string 
word=string.ascii_letters + string.digits + string.punctuation
password="".join(random.choices(word,k=8))
print(password)

