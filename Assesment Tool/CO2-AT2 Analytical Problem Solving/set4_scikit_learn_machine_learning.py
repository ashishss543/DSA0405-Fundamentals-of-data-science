import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

print("==================================================")
print("       MACHINE LEARNING WITH SCIKIT-LEARN         ")
print("==================================================")

# 1. Supervised Learning: Logistic Regression
print("\n1. Supervised Learning - Logistic Regression Algorithm:")
iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 2. Unsupervised Learning: KMeans Clustering
print("\n2. Unsupervised Learning - KMeans Clustering Algorithm:")
iris_data = load_iris()
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(iris_data.data)
cluster_labels = kmeans.labels_

print("Cluster Labels:")
print(cluster_labels)
