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

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=0.3)

# Import the artificial intelligence
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Create artificial intelligence
linear_regression_model = LinearRegression()
decision_tree_model = RandomForestRegressor()

# Training artificial intelligence

linear_regression_model.fit(x_training, y_training)
decision_tree_model.fit(x_training, y_training)

linear_regression_prediction = linear_regression_model.predict(x_test)
decision_tree_prediction = decision_tree_model.predict(x_test)

from sklearn.metrics import r2_score

print(r2_score(y_test, linear_regression_prediction))
print(r2_score(y_test, decision_tree_prediction))
