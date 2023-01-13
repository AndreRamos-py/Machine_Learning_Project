import pandas as pd
import numpy
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns



# Import the database
table = pd.read_csv(r"C:\Users\andre\OneDrive\Documentos\Intensivão Python\advertising.csv")

# Create the chart
sns.heatmap(table.corr(), cmap='Greens', annot=True)
plt.show()

# Data division
y = table['Vendas']
x = table [['TV', 'Radio', 'Jornal']]

from sklearn.model_selection import train_test_split

x_training, x_test, y_training, x_test = train_test_split(x, y)
