# Step 1 & 2: Import Required Libraries

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


# Step 3: Load the Wine Dataset

wine = load_wine()

X = wine.data
y = wine.target


# Step 4: Display Dataset Information

print("Dataset Information")
print("-------------------")
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(np.unique(y)))

print("\nFeature Names:")
print(wine.feature_names)

print("\nTarget Class Names:")
print(wine.target_names)


# Step 5: Split the Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# Step 6: Standardize the Features

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Step 7: Encode the Target Classes

y_train_encoded = to_categorical(y_train, num_classes=3)
y_test_encoded = to_categorical(y_test, num_classes=3)


# Step 8: Create the Feedforward Neural Network

model = Sequential([
    Dense(16, activation='relu', input_shape=(13,)),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')
])


# Display Model Architecture

model.summary()


# Step 9: Compile the Model

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# Step 10: Train the Model

history = model.fit(
    X_train,
    y_train_encoded,
    validation_split=0.20,
    epochs=100,
    batch_size=16,
    verbose=1
)


# Step 11: Evaluate the Model

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test_encoded,
    verbose=0
)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_accuracy)


# Step 12: Make Predictions

y_probability = model.predict(X_test)

y_pred = np.argmax(y_probability, axis=1)

print("\nPredicted Classes:")
print(y_pred)

print("\nActual Classes:")
print(y_test)


# Step 13: Calculate Classification Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nClassification Accuracy:", accuracy)
print("Classification Accuracy (%):", accuracy * 100)


# Step 14: Generate the Classification Report

print("\nClassification Report")
print("---------------------")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=wine.target_names
    )
)


# Step 15: Generate the Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print("----------------")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=wine.target_names
)

disp.plot(cmap='Blues')

plt.title("Confusion Matrix")
plt.show()


# Step 16: Plot Training and Validation Accuracy

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['accuracy'],
    label='Training Accuracy'
)

plt.plot(
    history.history['val_accuracy'],
    label='Validation Accuracy'
)

plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.show()


# Step 17: Plot Training and Validation Loss

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['loss'],
    label='Training Loss'
)

plt.plot(
    history.history['val_loss'],
    label='Validation Loss'
)

plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.show()


# Step 18: Record the Result

print("\nFinal Result")
print("------------")
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)
print("Classification Accuracy:", accuracy)
print("Classification Accuracy (%):", accuracy * 100)
