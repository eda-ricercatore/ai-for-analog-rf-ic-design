#!/opt/anaconda3/bin/python
#   #!/opt/homebrew/bin/python3
#   #!/opt/anaconda3/bin/python



"""
   Source code obtained from a Google search for: gantt chart python 
   https://matplotlib.org/
"""


import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare data with dates converted to pandas datetime objects
data = [
    {"Task": "Task A", "Start": "2026-06-01", "End": "2026-06-05"},
    {"Task": "Task B", "Start": "2026-06-04", "End": "2026-06-10"},
    {"Task": "Task C", "Start": "2026-06-09", "End": "2026-06-18"}
]
df = pd.DataFrame(data)
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# 2. Calculate task duration
df["Duration"] = df["End"] - df["Start"]

# 3. Plotting
fig, ax = plt.subplots(figsize=(10, 5))

# Use barh (horizontal bar) where left argument acts as the start date
ax.barh(df["Task"], df["Duration"].dt.days, left=df["Start"], color="skyblue", edgecolor="black")

# 4. Formatting the timeline axes
ax.invert_yaxis()  # Put the first task at the top
plt.xlabel("Timeline")
plt.title("Project Gantt Chart")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.show()
