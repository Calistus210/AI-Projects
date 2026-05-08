import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


digits = load_digits()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = SGDClassifier(random_state=42)

print("Training model...")
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")

fig, axes = plt.subplots(2, 5, figsize=(10, 5))

for i, ax in enumerate(axes.flat):

    image = X_test[i].reshape(8, 8)

    ax.imshow(image, cmap='gray')

    ax.set_title(
        f"Pred: {y_pred[i]}\nTrue: {y_test[i]}"
    )

    ax.axis('off')

plt.tight_layout()

plt.savefig("digit_predictions.png")

print("\nImage saved as digit_predictions.png")

plt.show()