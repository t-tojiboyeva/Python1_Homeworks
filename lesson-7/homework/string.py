def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(True)
else:
    print(False)

def digit_sum(k):
    return sum(int(digit) for digit in str(abs(k)))
k=int(input("Son kiriting:"))
print(digit_sum(k))
def ikki_son_daraja(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=' ')
        k += 1
n=int(input("N ni kiriting: "))
ikki_son_daraja(n)
