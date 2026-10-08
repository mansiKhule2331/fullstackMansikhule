import pandas as pd
# a) Read the CSV file
df = pd.read_csv("sales.csv")
# b) Display all products
print("All Products:")
print(df)
# c & d) Create Total_Sales column
# Total_Sales = Price × Quantity
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("\nProducts with Total Sales:")
print(df)
# e) Find the product with the highest total sales
highest_sales = df.loc[df["Total_Sales"].idxmax()]
print("\nProduct with Highest Total Sales:")
print(highest_sales)
# f) Find total sales of all products
total_sales = df["Total_Sales"].sum()
print("\nTotal Sales of All Products:", total_sales)
# g) Find average product price
average_price = df["Price"].mean()
print("Average Product Price:", average_price)
# h) Display products where quantity is greater than 10
print("\nProducts with Quantity Greater Than 10:")
print(df[df["Quantity"] > 10])
# i) Find total sales category-wise using groupby()
category_sales = df.groupby("Category")["Total_Sales"].sum()
print("\nCategory-wise Total Sales:")
print(category_sales)
# j) Sort products according to Total_Sales in descending order
sorted_df = df.sort_values(by="Total_Sales", ascending=False)
print("\nProducts Sorted by Total Sales:")
print(sorted_df)
# Save updated DataFrame
sorted_df.to_csv("sales_analysis.csv", index=False)
print("\nResult saved successfully as sales_analysis.csv")