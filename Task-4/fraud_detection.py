import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, average_precision_score
from imblearn.over_sampling import SMOTE

# 1. Load the Data
# Download 'creditcard.csv' from Kaggle and place it in the same folder
df = pd.read_csv('creditcard.csv')

print("Dataset Shape:", df.shape)
print(df.head())

# 2. Preprocessing
# The 'Time' and 'Amount' columns are not scaled. We need to scale 'Amount'.
# (V1-V28 are already PCA transformed, so we leave them alone)
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df = df.drop(['Time'], axis=1) # Time is usually not a strong indicator for this specific dataset

# 3. Handling Class Imbalance (The most important step)
X = df.drop('Class', axis=1)
y = df['Class']

# Split FIRST to avoid data leakage (training on test data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Apply SMOTE (Synthetic Minority Over-sampling Technique) ONLY to Training data
# This creates "fake" fraud examples to help the model learn better.
print("Applying SMOTE to handle imbalance...")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print(f"Original Fraud Count: {sum(y_train == 1)}")
print(f"Resampled Fraud Count: {sum(y_train_resampled == 1)}")

# 4. Train the Model
print("Training Random Forest Model...")

# n_jobs=-1 tells the computer to use ALL CPU cores.
# max_depth=10 prevents the trees from getting too complex.
rf_model = RandomForestClassifier(
    n_estimators=50, 
    max_depth=10, 
    n_jobs=-1, 
    random_state=42,
    verbose=1  # This will show a progress bar!
)

rf_model.fit(X_train_resampled, y_train_resampled)
print("Training Complete!")
# 5. Evaluation
y_pred = rf_model.predict(X_test)

print("\n--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show() 

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

print("\n--- AUPRC Score ---")
# Area Under the Precision-Recall Curve is the best metric for imbalance
print(f"AUPRC: {average_precision_score(y_test, y_pred):.4f}")
