import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Priya"],
    "Age": [22, 21, 23],
    "Salary": [17000, 20000, 25000]
}

df = pd.DataFrame(data)

print(df)