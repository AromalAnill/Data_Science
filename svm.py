
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Select categories
categories = ["comp.graphics", "rec.sport.baseball", "sci.space"]

print("Loading dataset...", flush=True)

# Load training dataset
train_data = fetch_20newsgroups(
    subset="train",
    categories=categories,
    remove=("headers", "footers", "quotes"),
    random_state=42
)

# Load testing dataset
test_data = fetch_20newsgroups(
    subset="test",
    categories=categories,
    remove=("headers", "footers", "quotes"),
    random_state=42
)

print("Dataset loaded successfully!")

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000
)

X_train_tfidf = vectorizer.fit_transform(train_data.data)
X_test_tfidf = vectorizer.transform(test_data.data)

y_train = train_data.target
y_test = test_data.target

# Create SVM model
svm_model = LinearSVC(random_state=42)

print("Training LinearSVC model...")

# Train model
svm_model.fit(X_train_tfidf, y_train)

# Predict output
y_pred = svm_model.predict(X_test_tfidf)

# Calculate accuracy
acc = accuracy_score(y_test, y_pred)

# Classification report
report = classification_report(
    y_test,
    y_pred,
    target_names=train_data.target_names
)

# Display results
print("\n--- RESULTS ---")
print("Number of training documents:", len(train_data.data))
print("Number of testing documents:", len(test_data.data))
print("Classification Accuracy:", round(acc, 4))

print("\nClassification Report:")
print(report)
