# %% [markdown]
# ---
# title: "Python script file"
# ---

# %%
import datetime
import pandas as pd
import random

# Randomly generate data that acts as 30-day trailing unit sales.
today = datetime.date.today()
data = pd.DataFrame({
    'Date': pd.date_range(
        today - datetime.timedelta(days=30),
        today - datetime.timedelta(days=1),
    ),
    'Sales': [random.randint(75, 100) for _ in range(1, 31)],
})


# Write a CSV for downstream use.
data.to_csv("sales.csv", index=False)

# %% [markdown]
# Download [CSV](sales.csv)