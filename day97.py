#Self-Training
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_classification(
    n_samples=200,
    n_features=5,
    random_state=42
)

X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

X_labeled, X_unlabeled, y_labeled, _ = train_test_split(
    X_train_full, y_train_full, test_size=0.7, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_labeled, y_labeled)

for _ in range(5):
    probs = model.predict_proba(X_unlabeled)
    confidence = np.max(probs, axis=1)

    high_conf_idx = np.where(confidence > 0.9)[0]

    if len(high_conf_idx) == 0:
        break

    X_labeled = np.vstack((X_labeled, X_unlabeled[high_conf_idx]))
    y_labeled = np.hstack((
        y_labeled,
        model.predict(X_unlabeled[high_conf_idx])
    ))

    X_unlabeled = np.delete(X_unlabeled, high_conf_idx, axis=0)
    model.fit(X_labeled, y_labeled)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Final Accuracy:", accuracy)
