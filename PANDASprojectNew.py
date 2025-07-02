import pandas as pd

# Sample dataset
data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'order_date': ['2025-01-03', '2025-01-10', '2025-01-25', '2025-02-01', '2025-02-15', '2025-02-28', '2025-03-05', '2025-03-20'],
    'shipping_date': ['2025-01-05', '2025-01-14', '2025-01-28', '2025-02-03', '2025-02-20', '2025-03-03', '2025-03-08', '2025-03-25'],
    'customer_name': ['Anna', 'Ben', 'Anna', 'Ben', 'Clara', 'Ben', 'Anna', 'Clara'],
    'country': ['Germany', 'Germany', 'Germany', 'France', 'Germany', 'France', 'Germany', 'Germany'],
    'category': ['Office Supplies', 'Technology', 'Technology', 'Office Supplies', 'Furniture', 'Technology', 'Furniture', 'Office Supplies'],
    'quantity': [2, 1, 3, 2, 1, 4, 2, 5],
    'unit_price': [100, 300, 250, 150, 400, 280, 350, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert dates
df[['order_date', 'shipping_date']] = df[['order_date', 'shipping_date']].apply(pd.to_datetime)

# Add total price
df['total_price'] = df['quantity'] * df['unit_price']

# Set index to order_date
df.set_index('order_date', inplace=True)

# Add month name
df['month'] = df.index.month_name()

#Sales by Country and Month
country_month_sales = df.groupby([df['country'], df['month']])['total_price'].sum().sort_values(ascending=False)
print("🔸 Sales by Country and Month:\n", country_month_sales)

#Average Unit Price By Category
avg_price_by_category = df.groupby('category')['unit_price'].mean().sort_values(ascending=False)
print("🔸 Average Unit Price by Category:\n", avg_price_by_category)

#SLA compliance 
df['shipping_delay'] = (df['shipping_date'] - df.index).dt.days
print("🔸 Shipping Delay:\n", df[['customer_name', 'shipping_delay']])

#pivot_table, PowerBI/Excel
pivot = df.pivot_table(
    index='month',
    columns='category',
    values='total_price',
    aggfunc='sum',
    fill_value=0
)
print("🔸 Pivot Table:\n", pivot)

#SaveOutPut
#df.to_csv('final_sales_data.csv')
#pivot.to_excel('pivot_sales_report.xlsx')
