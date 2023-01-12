import pandas as pd
import numpy
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns



tabela = pd.read_csv(r"C:\Users\andre\OneDrive\Documentos\Intensivão Python\advertising.csv")

# To make the correlation
print(tabela.corr())

# Display the chart

sns.heatmap(tabela.corr())
plt.show()
