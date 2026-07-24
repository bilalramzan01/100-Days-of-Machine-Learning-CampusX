import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load the data
iris = sns.load_dataset("iris")
print(iris)  # This will print the raw data to your console

# 2. Generate the plot (No print function needed here)
sns.pairplot(iris)

# 3. Correctly display the window (Leave the parentheses completely empty)
plt.show()
