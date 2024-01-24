import csv
import pandas as pd
data = pd.read_csv("data.csv")
print(data.head(2))
print("\n")
print(data.tail(3))

