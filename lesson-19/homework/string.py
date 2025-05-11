import pandas as pd
data = pd.read_csv(r'D:\Downloads\sales_data.csv')  # raw string
category_group = data.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    average_price_per_unit=('Price', 'mean'),
    max_quantity_sold=('Quantity', 'max')
)
data['Date'] = pd.to_datetime(data['Date'])
print(category_group)

product_sales = data.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

top_products = product_sales.sort_values('Quantity', ascending=False).groupby('Category').first().reset_index()

print("Top-selling product in each category:")
print(top_products)

import pandas as pd
data1 = pd.read_csv(r'D:\Downloads\customer_orders.csv') 
data1
Group the data by CustomerID and filter out customers who have made less than 20 orders.
Identify customers who have ordered products with an average price per unit greater than $120.
Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
customer_order_counts=data1.groupby('CustomerID').size()
customer_20_plus=customer_order_counts[customer_order_counts >=20].index
filtered_customers=data1[data1['CustomerID'].isin(customer_20_plus)]
filtered_customers



high_avg_price_customers=data1.groupby('CustomerID')['Price'].mean()
high_avg_price_customers=high_avg_price_customers[high_avg_price_customers > 120].index
customers_high_avg=data1[data1['CustomerID'].isin(high_avg_price_customers)]

high_avg_price_customers


customers_high_avg
product_totals=data.groupby('Product').agg(
    total_quantity=('Quantity','sum'),
    total_price=('Price','sum')
).reset_index()
filtered_products=product_totals[product_totals['total_quantity'] >= 5]
filtered_products=filtered_products.sort_values(by='total_quantity',ascending=False)
filtered_products
print(" Customers with 20+ orders:")
print(filtered_customers['CustomerID'].unique())

print("\n Customers with average price > $120:")
print(customers_high_avg['CustomerID'].unique())

print("\n Products with total quantity >= 5:")
print(filtered_products)

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect(r'task\population.db')

# Read the population table
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# Close the connection (optional after reading)
conn.close()

salary_bands_df = pd.read_excel(r'task\population salary analysis.xlsx')

# Optional: View structure
print(salary_bands_df.head())

# Use pd.cut or custom logic based on salary_bands_df
def assign_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Unknown'  # fallback if not in any range

# Apply to population DataFrame
population_df['Salary Band'] = population_df['Salary'].apply(assign_salary_band)

# Total number of people
total_population = len(population_df)

# Group by Salary Band
band_stats = population_df.groupby('Salary Band').agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
)

# Add percentage
band_stats['percentage_of_population'] = (band_stats['population_count'] / total_population) * 100

print("Salary Band Statistics:")
print(band_stats)

state_band_stats = population_df.groupby(['State', 'Salary Band']).agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

# Calculate percentage within each state
state_totals = population_df.groupby('State')['Salary'].count().reset_index(name='total')
state_band_stats = pd.merge(state_band_stats, state_totals, on='State')
state_band_stats['percentage_of_population'] = (state_band_stats['population_count'] / state_band_stats['total']) * 100
state_band_stats.drop(columns='total', inplace=True)

print("State-wise Salary Band Statistics:")
print(state_band_stats)

with pd.ExcelWriter('salary_analysis_output.xlsx') as writer:
    band_stats.to_excel(writer, sheet_name='Overall Band Stats')
    state_band_stats.to_excel(writer, sheet_name='State Band Stats', index=False)
