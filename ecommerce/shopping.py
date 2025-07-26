import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([[1],[2],[3],[4],[5]])#exparience year
y=np.array([30000,35000,40000,45000,50000])#salary

model=LinearRegression()
model.fit(x,y)

print(model.coef_[0])
print(model.intercept_)

prediction=model.predict([[7]])
print(prediction[0])


plt.scatter(x,y,color='red',label='Actual data')
plt.plot(x,model.predict(x),color='green',label='Regression line')
plt.xlabel='experience'
plt.ylabel='salary'
plt.legend()
plt.show()


