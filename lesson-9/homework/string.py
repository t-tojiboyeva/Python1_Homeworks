import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
      
        return math.pi * self.radius ** 2

    def get_perimeter(self):
       
        return 2 * math.pi * self.radius


circle1 = Circle(5)
print("Area of the circle:", circle1.get_area())
print("Perimeter of the circle:", circle1.get_perimeter())


from datetime import datetime

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
       
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


person1 = Person("Alice", "Uzbekistan", "2000-04-08")
print("Name:", person1.name)
print("Country:", person1.country)
print("Age:", person1.get_age())


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


calc = Calculator()
print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 4))
print("Multiply:", calc.multiply(6, 2))
print("Divide:", calc.divide(8, 2))


import math

class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        # Heron's formula
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


circle = Circle(4)
square = Square(5)
triangle = Triangle(3, 4, 5)

print("Circle area:", circle.get_area())
print("Square perimeter:", square.get_perimeter())
print("Triangle area:", triangle.get_area())




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(current, value):
            if current is None:
                return Node(value)
            if value < current.value:
                current.left = _insert(current.left, value)
            else:
                current.right = _insert(current.right, value)
            return current

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(current, value):
            if current is None:
                return False
            if current.value == value:
                return True
            elif value < current.value:
                return _search(current.left, value)
            else:
                return _search(current.right, value)

        return _search(self.root, value)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)

print("Search 5:", bst.search(5))
print("Search 12:", bst.search(12))


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()


class ShoppingCart:
    def __init__(self):
        self.items = {}  # key = item name, value = price

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"{item} not found in the cart.")

    def get_total(self):
        return sum(self.items.values())

    def show_items(self):
        for item, price in self.items.items():
            print(f"{item}: ${price}")
        print("Total:", self.get_total())


cart = ShoppingCart()
cart.add_item("Apple", 1.2)
cart.add_item("Bread", 2.5)
cart.show_items()

cart.remove_item("Apple")
cart.show_items()



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def display(self):
        if not self.is_empty():
            print("Stack contents:", self.items)
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(5)
stack.push(10)
stack.display()

stack.pop()
stack.display()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if not self.is_empty():
            print("Queue contents:", self.items)
        else:
            print("Queue is empty")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()

queue.dequeue()
queue.display()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


account = BankAccount("Tozagul", 100)
account.deposit(50)
account.withdraw(30)
print("Final Balance:", account.get_balance())

