import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set output directory
OUTPUT_DIR = 'task-1-eda'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv('../data/Delinquency_prediction_dataset.csv')

# 1. Dataset Overview
summary = {}
summary['num_records'] = len(df)
summary['columns'] = list(df.columns)
summary['dtypes'] = df.dtypes.astype(str).to_dict()

# Save dataset overview
overview_path = os.path.join(OUTPUT_DIR, 'dataset_overview.txt')
with open(overview_path, 'w') as f:
    f.write(f"Number of records: {summary['num_records']}\n")
    f.write(f"Columns: {summary['columns']}\n")
    f.write(f"Data types: {summary['dtypes']}\n")

# 2. Missing Data Analysis
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100
missing_df = pd.DataFrame({'MissingCount': missing, 'MissingPercent': missing_percent})
missing_path = os.path.join(OUTPUT_DIR, 'missing_data.csv')
missing_df.to_csv(missing_path)

# 3. Outlier & Anomaly Detection (basic)
outlier_cols = ['Age', 'Income', 'Credit_Score', 'Credit_Utilization', 'Missed_Payments', 'Loan_Balance', 'Debt_to_Income_Ratio', 'Account_Tenure']
outlier_summary = {}
for col in outlier_cols:
    if col in df.columns:
        desc = df[col].describe()
        outlier_summary[col] = desc.to_dict()
outlier_path = os.path.join(OUTPUT_DIR, 'outlier_summary.csv')
pd.DataFrame(outlier_summary).to_csv(outlier_path)

# 4. Early Risk Indicators (correlation with Delinquent_Account)
corrs = {}
for col in outlier_cols:
    if col in df.columns and df[col].dtype != 'O':
        corrs[col] = df[[col, 'Delinquent_Account']].corr().iloc[0,1]
corrs_path = os.path.join(OUTPUT_DIR, 'risk_correlations.csv')
pd.DataFrame.from_dict(corrs, orient='index', columns=['CorrelationWithDelinquency']).to_csv(corrs_path)

# 5. Top 3 Predictors (by absolute correlation)
top_predictors = sorted(corrs.items(), key=lambda x: abs(x[1]), reverse=True)[:3]
top_predictors_path = os.path.join(OUTPUT_DIR, 'top_predictors.txt')
with open(top_predictors_path, 'w') as f:
    for col, corr in top_predictors:
        f.write(f"{col}: {corr:.3f}\n")

# 6. Save a summary for the report
data_quality_summary = os.path.join(OUTPUT_DIR, 'data_quality_summary.txt')
with open(data_quality_summary, 'w') as f:
    f.write("Notable missing or inconsistent data:\n")
    f.write(missing_df[missing_df['MissingCount'] > 0].to_string())
    f.write("\n\nKey anomalies (see outlier_summary.csv for details)\n")
    f.write("\nEarly indicators of delinquency risk (see risk_correlations.csv and top_predictors.txt)\n")

# 7. Visualizations (optional, for report)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'correlation_matrix.png'))
plt.close()

print('EDA complete. Outputs saved in task-1 directory.') 