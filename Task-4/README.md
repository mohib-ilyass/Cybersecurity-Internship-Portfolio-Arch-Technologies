# Credit Card Fraud Detection System 🛡️

**Domain:** Cybersecurity / Financial Forensics  
**Technique:** Machine Learning (Random Forest + SMOTE)  
**Status:** Completed  

---

## 1. Project Overview
This project focuses on detecting fraudulent credit card transactions using machine learning. The dataset involves transactions made by European cardholders in September 2013. 

**The Challenge:** The dataset is highly unbalanced. Out of 284,807 transactions, only **492** are frauds (0.172%). A standard model would simply guess "Legitimate" every time and achieve 99.8% accuracy while missing every single crime.

**Objective:** Build a model that maximizes **Recall** (catching the fraud) while maintaining high **Precision** (avoiding false card blocks).

---

## 2. Methodology

### A. Data Preprocessing
* **Scaling:** The `Amount` feature was normalized using `StandardScaler`.
* **Anonymity:** Features `V1-V28` are PCA-transformed to protect user privacy.

### B. Handling Imbalance (SMOTE)
I used **SMOTE (Synthetic Minority Over-sampling Technique)** with a sampling strategy of `0.1`.
* Instead of training on a 99:1 ratio, I synthesized new fraud examples to create a **10:1 ratio**.
* This allowed the model to learn the patterns of fraud without being overwhelmed by the majority class.

### C. Model Architecture
* **Algorithm:** Random Forest Classifier
* **Settings:** `n_estimators=50`, `max_depth=10`, `n_jobs=-1` (Optimized for speed/performance balance).

---

## 3. Results & Analysis
The model was evaluated on a test set of roughly 57,000 transactions.

### Confusion Matrix
![Confusion Matrix](screenshots/confusion_matrix.png)

### Key Metrics:
* **Detection Rate (Recall): ~86%**
    * The model successfully detected **84 out of 98** fraudulent transactions in the test set.
* **False Alarm Rate: < 0.2%**
    * Only **103** legitimate transactions were flagged incorrectly out of 56,000+.
* **Accuracy:** 99.8% (Though this metric is misleading in fraud detection, the Recall score confirms the model's effectiveness).

---

## 4. Conclusion
No model is 100% perfect. There is always a trade-off between catching every criminal (Recall) and not bothering innocent users (Precision). 

This model achieves a strong balance: it stops the vast majority of attacks while keeping the "False Positive" annoyance rate extremely low for legitimate customers.

---

## 5. How to Run
1. Install dependencies: `pip install pandas scikit-learn imbalanced-learn seaborn`
2. Download the dataset from Kaggle (`creditcard.csv`).
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
3. Run the script: `python fraud_detection.py`