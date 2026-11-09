import pandas as pd

data = {
    "Name": ["Anu", "Rahul", "Meena", "John"],
    "Age": [20, None, 21, 22],
    "Marks": [85, 90, None, 78]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Customers with marks greater than 80
print("\nMarks > 80")
print(df[df["Marks"] > 80])

# Missing values
print("\nMissing Values")
print(df.isnull())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Filling Missing Values")
print(df)

# Sort by Marks
df = df.sort_values(by="Marks", ascending=False)

print("\nSorted Data")
print(df)