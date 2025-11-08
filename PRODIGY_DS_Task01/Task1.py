import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load CSV file
df =pd.read_csv("age.csv")  # Make sure CSV is in the same folder

# ✅ Bar Chart – Gender Count
gender_count = df["Gender"].value_counts()
plt.figure(figsize=(6,4))
gender_count.plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ✅ Histogram – Age Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=8)   # bins = grouping size
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
