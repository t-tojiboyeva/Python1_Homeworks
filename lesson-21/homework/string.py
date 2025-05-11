import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1
df1['Average']=df1[['Math','English','Science']].mean(axis=1)
print(df1)
top_student=df1.loc[df1['Average'].idxmax()]
print(top_student)
df1['Total']=df1[['Math','English','Science']].sum(axis=1)
print(df1)
import matplotlib.pyplot as plt

subject_avarege=df1[['Math','English','Science']].mean(axis=1)
subject_avarege.plot(kind='bar',title='Avarage Grades ',color=['skyblue','lightgreen','salmon'])
plt.ylabel=('Average grade')
plt.xlabel=('Subject')
plt.tight_layout()
plt.show()

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
# Calculate total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales for each product:")
print(total_sales)
# Calculate total sales per day and find the date with the maximum
total_sales_per_day = df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_date = total_sales_per_day.idxmax()
print("\nDate with the highest total sales:", max_date)
# Compute percentage change and format the result
pct_changes = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
pct_changes = pct_changes.round(2)  # Round to two decimal places
result_df = df2[['Date']].join(pct_changes.add_suffix('_%Change'))
print("\nPercentage change in sales for each product:")
print(result_df)
import matplotlib.pyplot as plt

# Plotting the sales trends using pandas built-in plot
df2.plot(x='Date', y=['Product_A', 'Product_B', 'Product_C'], kind='line', figsize=(10, 6))
plt.title('Sales Trends Over Time')
plt.ylabel('Sales')
plt.xlabel('Date')
plt.grid(True)
plt.show()
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
import matplotlib.pyplot as plt

# Exercise 1: Average salary per department
avg_salary = df3.groupby('Department')['Salary'].mean().round(2)
print("Average salary per department:")
print(avg_salary)

# Exercise 2: Employee with most experience
most_exp_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with most experience:")
print(most_exp_employee[['Name', 'Department', 'Experience (Years)']])

# Exercise 3: Salary Increase percentage from minimum salary
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print("\nDataFrame with Salary Increase:")
print(df3[['Name', 'Department', 'Salary', 'Salary Increase (%)']])

# Exercise 4: Employee distribution bar chart
plt.figure(figsize=(8, 5))
df3['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()
#DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
import matplotlib.pyplot as plt

# Exercise 1: Total Revenue
total_revenue = df4['Total_Price'].sum()
print(f"Total Revenue: ${total_revenue}")

# Exercise 2: Most Ordered Product
product_quantity = df4.groupby('Product')['Quantity'].sum()
most_ordered_product = product_quantity.idxmax()
print(f"\nMost Ordered Product: {most_ordered_product}")

# Exercise 3: Average Quantity per Order
average_quantity = df4['Quantity'].mean().round(2)
print(f"\nAverage Quantity per Order: {average_quantity}")

# Exercise 4: Sales Distribution Pie Chart
product_sales = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(8, 8))
product_sales.plot.pie(
    autopct='%1.1f%%',
    labels=product_sales.index,
    startangle=90,
    colors=['lightcoral', 'lightgreen', 'lightskyblue']
)
plt.title('Sales Distribution by Product')
plt.ylabel('')  # Remove default y-label
plt.show()
