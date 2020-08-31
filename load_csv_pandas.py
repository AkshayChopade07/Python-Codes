# Load CSV using Pandas

from pandas import read_csv
filename = '/Users/admin/Desktop/new folder/pima-indians-diabetes.data.csv'
columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = read_csv(filename, names=columns)
print(data.shape)
data

