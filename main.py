import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("sales.csv")

# show data
print("Original Data: ")
print(data)


# remove duplicate rows
cleaned_data = data.drop_duplicates()

# show cleaned data
print("\nCleaned_data: ")
print(cleaned_data)

# Calculations
total_sales = cleaned_data["Sales"].sum()

average_sales = cleaned_data["Sales"].mean()

highest_sales = cleaned_data["Sales"].max()

# Department-wise sales analysis
department_sales = cleaned_data.groupby("Department")["Sales"].sum()

# results
print("\nTotal Sales:", total_sales)

print("Average Sales: ", average_sales)

print("Highest Sales: ", highest_sales)

print("\nDepartment-wise Sales: ")
print(department_sales)

# Export cleaned data into new CSV file
cleaned_data.to_csv("cleaned_sales.csv", index=False)

print("\nCleaned CSV file created successfully!")

department_sales.plot(kind="bar")

# Graph labels
plt.title("Department-wise sales")

plt.xlabel("Department")

plt.ylabel("Sales")

# show graph
plt.show()
