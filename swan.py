import pandas as pd

data = {
    "Name": ["Black Swan", "White Swan", "Grey Swan"],
    "Age": [3, 4, 5],
    "City": ["Lake1", "Lake2", "Lake3"]
}

df = pd.DataFrame(data)

print(df)
