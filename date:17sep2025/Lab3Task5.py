import matplotlib.pyplot as plt

# Sales data for 12 months (in thousands)
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

# Calculate total sales
total_sales = 0
for sale in sales_data:
    total_sales += sale

# Calculate average sales
average_sales = total_sales / len(sales_data)

# Find month with highest sales
highest_sales = sales_data[0]
highest_month = 0
for i in range(1, len(sales_data)):
    if sales_data[i] > highest_sales:
        highest_sales = sales_data[i]
        highest_month = i

# Print results
print("Total Sales (in thousands):", total_sales)
print("Average Sales (in thousands):", average_sales)
print("Month with Highest Sales:", highest_month + 1, "with", highest_sales, "thousands")

# Plot sales data
months = list(range(1, 13))
plt.plot(months, sales_data, marker='o', label="Monthly Sales")

# Highlight the highest sales month
plt.scatter(highest_month + 1, highest_sales, color='red', s=100, zorder=5, label="Highest Sales")

plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.xticks(months)
plt.legend()
plt.grid(True)
plt.show()
