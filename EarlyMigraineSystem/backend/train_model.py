import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

df = pd.read_csv("../data/migraine_data.csv")

print("Columns:", df.columns)

# Rename columns
df.rename(columns={
    'Photophobia': 'photophobia',
    'Phonophobia': 'phonophobia',
    'Type': 'label'
}, inplace=True)

# Select important features
df = df[['photophobia', 'phonophobia', 'Nausea', 'Vomit', 'Intensity', 'Frequency', 'label']]

def convert_binary(val):
    val = str(val).strip().lower()
    return 1 if val in ['yes', 'y', '1', 'true'] else 0

df['photophobia'] = df['photophobia'].apply(convert_binary)
df['phonophobia'] = df['phonophobia'].apply(convert_binary)
df['Nausea'] = df['Nausea'].apply(convert_binary)
df['Vomit'] = df['Vomit'].apply(convert_binary)

# Convert numeric features
df['Intensity'] = pd.to_numeric(df['Intensity'], errors='coerce')
df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce')

df['label'] = df['label'].astype(str).str.lower()
df['label'] = df['label'].apply(lambda x: 1 if 'migraine' in x else 0)

print("\nBefore cleaning:", len(df))
print(df['label'].value_counts())

# Drop missing values
df = df.dropna()

print("\nAfter cleaning:", len(df))

df_majority = df[df.label == 0]
df_minority = df[df.label == 1]

print("\nMajority:", len(df_majority))
print("Minority:", len(df_minority))

df_majority = df_majority.sample(len(df_minority), replace=True)
df = pd.concat([df_majority, df_minority])

print("\nAfter balancing:")
print(df['label'].value_counts())

ks = pd.read_csv("../data/DSL-StrongPasswordData.csv")

print("\nKeystroke Columns:", ks.columns)

# Select numeric columns
numeric_cols = ks.select_dtypes(include=['float64', 'int64']).columns

# Compute typing speed
ks['typing_speed'] = ks[numeric_cols].mean(axis=1)

# Normalize typing speed
ks['typing_speed'] = (
    (ks['typing_speed'] - ks['typing_speed'].min()) /
    (ks['typing_speed'].max() - ks['typing_speed'].min())
)

n = min(len(df), len(ks))

df = df.sample(n)
ks = ks.sample(n)

df['typing_speed'] = ks['typing_speed'].values

# Final dataset
final_df = df[['photophobia', 'phonophobia', 'Nausea', 'Vomit', 'Intensity', 'Frequency', 'typing_speed', 'label']]

print("\nFinal dataset size:", len(final_df))
print(final_df.head())

# Save dataset
final_df.to_csv("../data/final_dataset.csv", index=False)

X = final_df[['photophobia', 'phonophobia', 'Nausea', 'Vomit', 'Intensity', 'Frequency', 'typing_speed']]
y = final_df['label']

# Scale numeric features
scaler = StandardScaler()
X[['Intensity', 'Frequency', 'typing_speed']] = scaler.fit_transform(
    X[['Intensity', 'Frequency', 'typing_speed']]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Improved model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)
print("\nConfusion Matrix:\n", cm)

report = classification_report(y_test, pred)
print("\nClassification Report:\n", report)

print("\nAccuracy:", accuracy_score(y_test, pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Get prediction probabilities
y_prob = model.predict_proba(X_test)[:, 1]

# Compute ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

print("\nAUC Score:", roc_auc)