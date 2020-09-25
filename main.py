import numpy as np
import pandas as pd

'reads a CSV file into DataFrame'
DataFrame = pd.read_csv('/Users/edmond/PycharmProjects/Wine-Quality/data/winequality-red.csv', engine='python')
DataFrame.head()

'checks for null values including empty strings'
pd.options.mode.use_inf_as_na = True
DataFrame.isna()

'provides info on the data and counts instances of each quality'
DataFrame.info()
print(DataFrame['quality'].value_counts())

'changes target variable "quality" to Good or Bad, lists quantities of each'
DataFrame['quality'] = ['Good' if x>=7 else 'bad' for x in DataFrame['quality']]
print(DataFrame['quality'].value_counts())
