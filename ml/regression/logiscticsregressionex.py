"""
Logistic Regression & Classification Metrics
How logistic regression works
Despite the name, it's a classifier. It applies the sigmoid function to a linear combination of features, 
squashing output to [0, 1] — a probability. Decision boundary: predict class 1 if P(y=1|x) > 0.5.

It's trained by minimising log loss (cross-entropy), not MSE.

Classification metrics — know all four

Metric	            Formula	            Use when…
Accuracy	        correct / total	        classes are balanced
Precision	        TP / (TP+FP)	        false positives are costly (spam filter)
Recall	            TP / (TP+FN)	        false negatives are costly (cancer detection)
F1-Score	        2·P·R/(P+R)	            imbalanced classes — best single metric
AUC-ROC	            area under ROC curve	    ranking quality across all thresholds

"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

clf = LogisticRegression(max_iter=1000, C=1.0)
clf.fit(X_train_s, y_train)

# --- All classification metrics at once ---
y_pred = clf.predict(X_test_s)
print(classification_report(y_test, y_pred,
      target_names=['malignant', 'benign']))

# --- AUC-ROC ---
y_prob = clf.predict_proba(X_test_s)[:, 1]
auc = roc_auc_score(y_test, y_prob)
print(f"AUC-ROC: {auc:.4f}")

# --- ROC Curve plot ---
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}", color='steelblue')
plt.plot([0,1],[0,1], '--', color='gray', label='random')
plt.xlabel("FPR"); plt.ylabel("TPR"); plt.legend()
plt.title("ROC Curve"); plt.tight_layout(); plt.show()

# --- Confusion matrix ---
ConfusionMatrixDisplay.from_predictions(y_test, y_pred,
    display_labels=['malignant', 'benign'])
plt.show()

# --- Tune threshold (important for imbalanced problems) ---
threshold = 0.3   # lower threshold → higher recall, lower precision
y_pred_low = (y_prob > threshold).astype(int)
print("\nWith threshold=0.3:")
print(classification_report(y_test, y_pred_low))
'''
Threshold tuning
Lowering the decision threshold below 0.5 increases recall at the cost of precision. 
In medical diagnosis you'd prefer high recall (don't miss a cancer). 
In spam filters you'd prefer high precision (don't flag real emails). 
Always tune to your business problem.
'''
'''
Given a model with 95% accuracy on a dataset that is 95% class-0 — is this model good? Why or why not?
Explain the precision–recall trade-off with a concrete example from your domain.
What does AUC = 0.5 mean? AUC = 1.0? AUC = 0.5?
'''