import matplotlib.pyplot as plt
import numpy as np
# 通过sklearn.linemodel加载岭回归方法
from sklearn.linear_model import Ridge
# 通过sklearn.preprocessing加载PolynomialFeatures用于创建多项式特征，如ab, a^2, b^2
from sklearn.preprocessing import PolynomialFeatures

data_train = np.loadtxt('zhengqi_train.txt', delimiter='\t', skiprows=1)
x_train = data_train[:, 0:-1]
y_train = data_train[:, -1]
data_test = np.loadtxt('zhengqi_test.txt', delimiter='\t', skiprows=1)
x_test = data_test[:, 0:-1]
y_test = data_test[:, -1]
# print(x_data)
# print(x_data.shape)
# print(type(x_data))
poly = PolynomialFeatures(6)
# X_train = poly.fit_transform(x_train)
# X_test = poly.fit_transform(x_test)

# clf = Ridge(alpha = 1.0, fit_intercept=True)
# clf.fit(X_train, y_train)
# clf.score(X_test, y_test)

print(data_train.corr())
