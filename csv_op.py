import pandas as pd

data = {
    "Name": ["Anu", "Rahul", "Veena"],
    "Age": [25, 24, 30],
    "City": ["KTM", "EKM", "Alpy"]
}

df = pd.DataFrame(data)


df.to_csv("students.csv", index=False)


df1 = pd.read_csv("students.csv")

print("First Row")
print(df1.head(1))

print("\nLast Row")
print(df1.tail(1))

print("\nComplete Data")
print(df1)