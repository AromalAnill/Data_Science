
import pandas as pd


data = {
    "Department": ["MCA", "CSE", "MCA", "CSE", "ECA"],
    "EmpName": ["ABC", "XYZ", "PQR", "TUV", "DEF"],
    "Salary": [45000, 50000, 42000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Employee Data")
print(df)

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary of Each Department")
print(avg_salary)