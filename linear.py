from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

X_bmi = X[:, 2].reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X_bmi, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

print("Linear Regression using BMI")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_linear))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred_linear))
print("R2 Score:", r2_score(y_test, y_pred_linear))

X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X, y, test_size=0.2, random_state=42
)

multiple_model = LinearRegression()

multiple_model.fit(X_train_multi, y_train_multi)

y_pred_multiple = multiple_model.predict(X_test_multi)

print("\nMultiple Linear Regression using all features")
print("Mean Squared Error:", mean_squared_error(y_test_multi, y_pred_multiple))
print("Mean Absolute Error:", mean_absolute_error(y_test_multi, y_pred_multiple))
print("R2 Score:", r2_score(y_test_multi, y_pred_multiple))

print("\nComparison")
print("Linear Regression R2 Score:", r2_score(y_test, y_pred_linear))
print("Multiple Linear Regression R2 Score:", r2_score(y_test_multi, y_pred_multiple))

plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, y_pred_linear, color="red", label="Regression Line")

plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression using BMI")
plt.legend()
plt.show()
