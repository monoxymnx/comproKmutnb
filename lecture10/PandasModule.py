import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]}

df = pd.DataFrame(data)
print(df)

average_age = df["Age"].mean()
print("Average Age:", average_age)

filtered_df = df[df["Age"] > 28]
print("Filtered DataFrame (Age > 28):")

df['Salary'] = [70000, 80000, 90000]
print(df)
