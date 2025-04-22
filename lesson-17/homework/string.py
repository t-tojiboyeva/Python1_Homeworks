import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df.columns=df.columns.str.replace(' ','_').str.lower()
print(df)
import pandas as pd
data={
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df=pd.DataFrame(data)
print(df.head(3))

print(df['Age'].mean())

print(df[['First Name','City']])
df['Salary']=[100,200,300,400]
print(df)
print(df.describe(include='all'))
5000	3000
Feb	6000	3500
Mar	7500	4000
Apr	8000	4500
Calculate and display the maximum sales and expenses.
Calculate and display the minimum sales and expenses.
Calculate and display the average sales and expenses.
import pandas as pd
sales_and_expenses={
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500,4000,4500] 
}
df=pd.DataFrame(sales_and_expenses)


print(df[['Sales','Expenses']].max())

print(df[['Sales','Expenses']].min())

print(df[['Sales','Expenses']].mean())



import pandas as pd
expenses = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df=pd.DataFrame(expenses)
df=df.set_index('Category')


max_expense = df.max(axis=1)
min_expense = df.min(axis=1)
average_expense = df.mean(axis=1)

print("Maximum expense for each category:")
print(max_expense)

print("\nMinimum expense for each category:")
print(min_expense)

print("\nAverage expense for each category:")
print(average_expense)
