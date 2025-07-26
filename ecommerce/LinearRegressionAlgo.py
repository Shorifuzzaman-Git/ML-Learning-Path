#Salary price prediction based on experience

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1],[2],[3],[4],[5]]) #exparience
y=np.array([30000,35000,40000,45000,50000]) #salary

model=LinearRegression()
model.fit(x,y)

print(model.coef_[0]) #coefficient
print(model.intercept_)#intercept

prediction=model.predict([[6]]) #predict salary
print(prediction[0])

#visualize
plt.scatter(x,y,color='green')
plt.plot(x,model.predict(x),color='red')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title("Salary prediction")
plt.show()



