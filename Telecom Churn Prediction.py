# Question: Based on a customer's contract length and monthly charges, will they leave (Churn) or stay?

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# 1. Data
X = np.array([[0, 25], [1, 50], [0, 100], [2, 40], [0, 110], [1, 20], [2, 105], [0, 95]])
y = np.array([0, 0, 1, 0, 1, 0, 0, 1]) # 0=Stay, 1=Leave

# 2. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Logistic Regression
logr = LogisticRegression()
logr.fit(X_train, y_train)

# 4. Decision Tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# 5. Confusion Matrix
predictions = dtree.predict(X_test)
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:\n", cm)