
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data_one_hot = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, data_one_hot], axis=1)
print(data.head())