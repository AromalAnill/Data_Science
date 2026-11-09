# Decision Tree Classification using Iris Dataset

# Step 1: Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Step 2: Load the Iris dataset
iris = load_iris()

# Step 3: Separate input features (X) and target classes (y)
X = iris.data
y = iris.target

# Display dataset information
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Feature names:", iris.feature_names)
print("Class names:", iris.target_names)

# ---------------------------------------------------------
# 80% Training and 20% Testing
# ---------------------------------------------------------

print("\n========== 80% Training / 20% Testing ==========")

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Step 5: Create Decision Tree Classifier using Gini criterion
model = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Predict classes of test data
y_pred = model.predict(X_test)

# Step 8 & 9: Compare predictions and calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nActual classes:   ", y_test)
print("Predicted classes:", y_pred)

print("\nAccuracy:", accuracy)
print("Accuracy percentage: {:.2f}%".format(accuracy * 100))

# Step 10: Display confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Step 11: Display classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

# Step 12 & 13: Visualize the trained Decision Tree
plt.figure(figsize=(15, 10))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree - Iris Dataset")
plt.show()


# ---------------------------------------------------------
# 70% Training and 30% Testing
# ---------------------------------------------------------

print("\n========== 70% Training / 30% Testing ==========")

# Step 4: Split dataset with 70% training and 30% testing
X_train_70, X_test_70, y_train_70, y_test_70 = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Create and train Decision Tree
model_70 = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)

model_70.fit(X_train_70, y_train_70)

# Predict
y_pred_70 = model_70.predict(X_test_70)
    
# Calculate accuracy
accuracy_70 = accuracy_score(y_test_70, y_pred_70)

print("Training samples:", len(X_train_70))
print("Testing samples:", len(X_test_70))

print("\nAccuracy:", accuracy_70)
print("Accuracy percentage: {:.2f}%".format(accuracy_70 * 100))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test_70, y_pred_70))

# Classification Report
print("\nClassification Report:")
print(classification_report(
    y_test_70,
    y_pred_70,
    target_names=iris.target_names
))
