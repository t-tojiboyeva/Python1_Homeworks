try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")
try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
  try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Sum:", x + y)
except ValueError:
    raise TypeError("Error: Inputs must be numerical values.")
try:
    file = open("/root/protectedfile.txt", "r")
    content = file.read()
    print(content)
    file.close()
except PermissionError:
    print("Error: You don't have permission to access this file.")
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index is out of range.")

try:
    num = input("Enter a number (press Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
try:
    x = 10
    y = 0
    result = x / y
except ArithmeticError:
    print("Arithmetic error occurred.")
try:
    with open("sample.txt", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Error: Cannot decode the file with UTF-8.")
try:
    my_list = [1, 2, 3]
    my_list.upper()  # Invalid operation
except AttributeError:
    print("Error: 'list' object has no attribute 'upper'.")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
  n = 3
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")
with open("sample.txt", "a") as file:
    file.write("New line added.\n")

with open("sample.txt", "r") as file:
    print(file.read())
n = 3
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")
      with open("sample.txt", "r") as file:
    lines = file.readlines()
print(lines)
text = ""
with open("sample.txt", "r") as file:
    for line in file:
        text += line
print(text)
array = []
with open("sample.txt", "r") as file:
    for line in file:
        array.append(line.strip())
print(array)
with open("sample.txt", "r") as file:
    words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
with open("sample.txt", "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))
from collections import Counter
with open("sample.txt", "r") as file:
    words = file.read().replace(',', '').split()
counts = Counter(words)
print(counts)
import os
file_size = os.path.getsize("sample.txt")
print("File size:", file_size, "bytes")
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
      
import random
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Random line:", random.choice(lines))
file = open("sample.txt", "r")
print("Is file closed?", file.closed)
file.close()
print("Is file closed now?", file.closed)

with open("sample.txt", "r") as file:
    lines = file.read().splitlines()
print(lines)

with open("sample.txt", "r") as file:
    text = file.read().replace(",", " ")
    words = text.split()
    print("Word count:", len(words))


filenames = ["file1.txt", "file2.txt"]
chars = []
for name in filenames:
    with open(name, "r") as file:
        chars.extend(list(file.read()))
print(chars)


import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")


import string
letters = string.ascii_lowercase
n = 5  
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")







