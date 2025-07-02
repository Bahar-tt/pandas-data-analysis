import pandas as pd

data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'customer_name': ['Anna', 'Ben', 'Anna', 'Lukas', 'Sophie', 'Ben', 'Anna', 'Lukas'],
    'product': ['Laptop', 'Shoes', 'Tablet', 'Laptop', 'T-shirt', 'Tablet', 'Shoes', 'Shoes'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Clothing'],
    'quantity': [1, 2, 1, 1, 3, 2, 1, 2],
    'unit_price': [1200, 90, 600, 1300, 30, 650, 85, 95],
    'order_date': ['2025-01-03', '2025-01-05', '2025-02-10', '2025-02-20', '2025-03-01', '2025-03-05', '2025-03-07', '2025-03-15'],
    'country': ['Germany', 'Germany', 'France', 'Germany', 'France', 'Germany', 'Germany', 'Germany']
}

df = pd.DataFrame(data)
#1
df['order_date'] = pd.to_datetime(
    df['order_date'],
    format='%Y-%m-%d',
    errors='coerce',
    dayfirst=False
)
df['total_price'] = df['quantity'] * df['unit_price']
print(df[['order_id', 'order_date', 'quantity', 'unit_price', 'total_price']])
#2
# 1. مجموع فروش کل فروشگاه
total_sales = df['total_price'].sum()
print("🔹 Total Sales of Store:", total_sales)

# 2. مجموع فروش به تفکیک دسته‌بندی
category_sales = df.groupby('category')['total_price'].sum().sort_values(ascending=False)
print("🔹 Sales by Category:\n", category_sales)

# 3. میانگین فروش در کشور آلمان
germany_mean = df[df['country'] == 'Germany']['total_price'].mean()
print("🔹 Average Sales in Germany:", germany_mean)
