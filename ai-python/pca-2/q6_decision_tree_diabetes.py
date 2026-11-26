"""
Question 6: Decision Tree Classification on the Diabetes Dataset.
Matches lab style using diabetes.csv (Pima Indians Diabetes dataset) with an offline
fallback to sklearn.datasets.load_diabetes() if diabetes.csv is not present.
"""

import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

if os.path.exists("diabetes.csv"):
    col_names = ["pregnant", "glucose", "bp", "skin", "insulin", "bmi", "pedigree", "age", "label"]
    pima = pd.read_csv("diabetes.csv", header=None, names=col_names)
    feature_cols = ["pregnant", "insulin", "bmi", "age", "glucose", "bp", "pedigree"]
    X = pima[feature_cols]
    y = pima.label
else:
    diabetes = load_diabetes()
    X = diabetes.data
    y = (diabetes.target >= np.median(diabetes.target)).astype(int)

# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create and train Decision Tree classifier object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
