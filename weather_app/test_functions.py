import json
import pandas as pd


data = {
  "company": {
    "departments": [
      {
        "name": "Engineering",
        "employees": [
          {"name": "Alice", "age": 30},
          {"name": "Bob", "age": 25}
        ]
      },
      {
        "name": "HR",
        "employees": [
          {"name": "Eve", "age": 28},
          {"name": "Frank", "age": 40}
        ]
      }
    ]
  }
}


df = pd.json_normalize(
    data,
    record_path=["company", "departments", "employees"],
    meta=[["company", "departments", "name"]]
    )
print(df)

