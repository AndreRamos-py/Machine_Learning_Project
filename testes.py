import pandas as pd
import numpy
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns



table = pd.read_csv(r"C:\Users\andre\OneDrive\Documentos\Intensivão Python\advertising.csv")

# To make the correlation
print(table.corr())

# Display the chart

sns.heatmap(table.corr(), cmap='Greens', annot=True)
plt.show()
