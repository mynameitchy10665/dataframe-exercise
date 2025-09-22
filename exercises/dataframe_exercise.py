import pandas as pd
# Sample sales dataset (20 rows)
data = {
"OrderID": range(1001, 1021),
"Product": [
"Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
"Headphones", "Mouse", "Chair", "Desk", "Laptop",
"Printer", "Keyboard", "Monitor", "Mouse", "Laptop",
"Headphones", "Desk", "Monitor", "Printer", "Chair"
],
"Category": [
"Electronics", "Accessories", "Accessories", "Electronics", "Electronics",
"Accessories", "Accessories", "Furniture", "Furniture", "Electronics",
"Electronics", "Accessories", "Electronics", "Accessories", "Electronics",
"Accessories", "Furniture", "Electronics", "Electronics", "Furniture"
],
"Quantity": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],
"Price": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],
"Customer": [
"Alice", "Bob", "Charlie", "Diana", "Ethan",
"Fiona", "George", "Hannah", "Ian", "Jane",
"Kyle", "Laura", "Mike", "Nina", "Oscar",
"Paul", "Queen", "Robert", "Sarah", "Tom"
],
"Region": [
"North", "South", "East", "West", "North",
"South", "East", "West", "North", "South",
"East", "West", "North", "South", "East",
"West", "North", "South", "East", "West"
]
}
# Create DataFrame
df = pd.DataFrame(data)
# Compute Total column
df["Total"] = df["Quantity"] * df["Price"]
print(df.head())

print("Rows: ", df.shape[0])
print("Columns: ", df.shape[1])

print("Columns:", df.columns)

new_row = {
    "OrderID": 1021,
    "Product": "Tablet",
    "Category": "Electronics",
    "Quantity": 2,
    "Price": 450,
    "Customer": "Victor",
    "Region": "East"
}
new_row_df = pd.DataFrame([new_row])
df = pd.concat([df, new_row_df], ignore_index=True)


df["Total"] = df["Quantity"] * df["Price"]

print(df.tail(3))
