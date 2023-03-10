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

# Graphic Visualization of Predictions

auxiliary_table = pd.DataFrame()
auxiliary_table['y_test'] = y_test
auxiliary_table['Decision Tree Prediction'] = decision_tree_prediction
auxiliary_table['Linear Regression Prediction'] = linear_regression_prediction

sns.lineplot(data=auxiliary_table)
plt.show()

# New Predict

new_predict = table = pd.read_csv(r"C:\Users\andre\OneDrive\Documentos\Intensivão Python\novos.csv")
print(new_predict)

predict_n = decision_tree_model.predict(new_predict)
print(predict_n)
