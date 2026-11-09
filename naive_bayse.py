from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

y = np.where(y >= np.median(y), 1, 0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

nb = GaussianNB()

nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Actual Labels:\n", y_test)
print("\nPredicted Labels:\n", y_pred)

print("\nAccuracy of Naive Bayes Classifier: {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
