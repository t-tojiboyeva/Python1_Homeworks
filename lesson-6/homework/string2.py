def insert_underscores(txt):
    result = ""
    i = 0
    count = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            if txt[i] in "aeiou" or (i + 1 < len(txt) and txt[i+1] == '_'):
                pass
            elif i + 1 < len(txt):
                result += '_'
                count = 0
        i += 1

    return result


print(insert_underscores("hello"))      # hel_lo
print(insert_underscores("assalom"))    # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

n = int(input("Enter a number: "))
for i in range(n):
    print(i * i)
i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


num = int(input("Enter number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("Sum is:", total)


num = int(input("Enter number: "))
for i in range(1, 11):numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)

    print(num * i)


numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Output:", count)


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


for i in range(-10, 0):
    print(i)


for i in range(5):
    print(i)
print("Done!")



start = 25
end = 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b


num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")


def uncommon_elements(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)

    for item in list2:
        if item not in list1:
            result.append(item)

    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))       # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))       # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]




