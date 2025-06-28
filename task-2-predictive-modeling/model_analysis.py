import pandas as pd
import numpy as np
import os

# Set output directory
OUTPUT_DIR = 'task-2-predictive-modeling'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv('../data/Delinquency_prediction_dataset.csv')

print("=== FEATURE ANALYSIS FOR PREDICTIVE MODELING ===")

# Handle missing values for analysis
df_clean = df.copy()
df_clean['Income'].fillna(df_clean['Income'].median(), inplace=True)
df_clean['Credit_Score'].fillna(df_clean['Credit_Score'].mean(), inplace=True)
df_clean['Loan_Balance'].fillna(df_clean['Loan_Balance'].median(), inplace=True)

# 1. Feature Importance Analysis using Correlation
numerical_features = ['Age', 'Income', 'Credit_Score', 'Credit_Utilization', 
                     'Missed_Payments', 'Loan_Balance', 'Debt_to_Income_Ratio', 'Account_Tenure']

# Calculate correlation with target variable
correlations = {}
for col in numerical_features:
    correlations[col] = abs(df_clean[[col, 'Delinquent_Account']].corr().iloc[0,1])

# Sort features by correlation strength
feature_importance = pd.DataFrame({
    'Feature': list(correlations.keys()),
    'Correlation_with_Target': list(correlations.values())
})
feature_importance = feature_importance.sort_values('Correlation_with_Target', ascending=False)

print("\nFeature Importance (Correlation with Delinquency):")
print(feature_importance.to_string(index=False))

# Save feature importance results
feature_importance_path = os.path.join(OUTPUT_DIR, 'feature_importance.csv')
feature_importance.to_csv(feature_importance_path, index=False)

# 2. Top 5 Features Analysis
top_5_features = feature_importance.head(5)
print(f"\nTop 5 Features for Predictive Modeling:")
print(top_5_features.to_string(index=False))

# Save top features
top_features_path = os.path.join(OUTPUT_DIR, 'top_5_features.txt')
with open(top_features_path, 'w') as f:
    f.write("Top 5 Features for Delinquency Prediction:\n")
    for idx, row in top_5_features.iterrows():
        f.write(f"{row['Feature']}: Correlation = {row['Correlation_with_Target']:.3f}\n")

# 3. Class Distribution Analysis
class_dist = df_clean['Delinquent_Account'].value_counts()
print(f"\nClass Distribution:")
print(f"Non-delinquent: {class_dist[0]} ({class_dist[0]/len(df_clean)*100:.1f}%)")
print(f"Delinquent: {class_dist[1]} ({class_dist[1]/len(df_clean)*100:.1f}%)")

# Save class distribution
class_dist_path = os.path.join(OUTPUT_DIR, 'class_distribution.txt')
with open(class_dist_path, 'w') as f:
    f.write(f"Class Distribution:\n")
    f.write(f"Non-delinquent: {class_dist[0]} ({class_dist[0]/len(df_clean)*100:.1f}%)\n")
    f.write(f"Delinquent: {class_dist[1]} ({class_dist[1]/len(df_clean)*100:.1f}%)\n")

# 4. Risk Factor Analysis
print("\n=== RISK FACTOR ANALYSIS ===")

# Analyze high-risk groups
high_utilization = df_clean[df_clean['Credit_Utilization'] > 0.5]
high_missed_payments = df_clean[df_clean['Missed_Payments'] >= 3]
low_credit_score = df_clean[df_clean['Credit_Score'] < 500]
low_income = df_clean[df_clean['Income'] < df_clean['Income'].quantile(0.25)]
high_debt_ratio = df_clean[df_clean['Debt_to_Income_Ratio'] > 0.4]

risk_analysis = {
    'High Credit Utilization (>50%)': {
        'count': len(high_utilization),
        'delinquency_rate': high_utilization['Delinquent_Account'].mean() * 100
    },
    'High Missed Payments (≥3)': {
        'count': len(high_missed_payments),
        'delinquency_rate': high_missed_payments['Delinquent_Account'].mean() * 100
    },
    'Low Credit Score (<500)': {
        'count': len(low_credit_score),
        'delinquency_rate': low_credit_score['Delinquent_Account'].mean() * 100
    },
    'Low Income (Bottom 25%)': {
        'count': len(low_income),
        'delinquency_rate': low_income['Delinquent_Account'].mean() * 100
    },
    'High Debt-to-Income (>40%)': {
        'count': len(high_debt_ratio),
        'delinquency_rate': high_debt_ratio['Delinquent_Account'].mean() * 100
    }
}

print("\nRisk Factor Analysis:")
for factor, stats in risk_analysis.items():
    print(f"{factor}: {stats['count']} customers, {stats['delinquency_rate']:.1f}% delinquency rate")

# Save risk analysis
risk_analysis_path = os.path.join(OUTPUT_DIR, 'risk_factor_analysis.txt')
with open(risk_analysis_path, 'w') as f:
    f.write("Risk Factor Analysis:\n")
    for factor, stats in risk_analysis.items():
        f.write(f"{factor}: {stats['count']} customers, {stats['delinquency_rate']:.1f}% delinquency rate\n")

# 5. Model Selection Insights
print("\n=== MODEL SELECTION INSIGHTS ===")

# Check for non-linear relationships by binning
non_linear_analysis = {}
for col in ['Credit_Utilization', 'Missed_Payments', 'Income', 'Credit_Score']:
    # Create bins for non-linear analysis
    df_clean[f'{col}_binned'] = pd.qcut(df_clean[col], q=5, duplicates='drop')
    grouped = df_clean.groupby(f'{col}_binned')['Delinquent_Account'].mean()
    non_linear_analysis[col] = grouped.std()  # Higher std indicates non-linear relationship

print("\nNon-linear Relationship Analysis (Standard Deviation of Delinquency Rate by Bins):")
for col, std_val in non_linear_analysis.items():
    print(f"{col}: {std_val:.3f}")

# 6. Categorical Variable Analysis
print("\n=== CATEGORICAL VARIABLE ANALYSIS ===")

categorical_features = ['Employment_Status', 'Credit_Card_Type', 'Location']
categorical_analysis = {}

for col in categorical_features:
    grouped = df_clean.groupby(col)['Delinquent_Account'].agg(['count', 'mean'])
    grouped['delinquency_rate'] = grouped['mean'] * 100
    categorical_analysis[col] = grouped
    print(f"\n{col} Analysis:")
    print(grouped[['count', 'delinquency_rate']].round(2))

# Save categorical analysis
cat_analysis_path = os.path.join(OUTPUT_DIR, 'categorical_analysis.txt')
with open(cat_analysis_path, 'w') as f:
    f.write("Categorical Variable Analysis:\n")
    for col, grouped in categorical_analysis.items():
        f.write(f"\n{col}:\n")
        f.write(grouped[['count', 'delinquency_rate']].round(2).to_string())
        f.write("\n")

# 7. Model Recommendations
print("\n=== MODEL RECOMMENDATIONS ===")

# Determine if data shows linear or non-linear patterns
linear_features = [k for k, v in non_linear_analysis.items() if v < 0.05]
non_linear_features = [k for k, v in non_linear_analysis.items() if v >= 0.05]

print(f"Linear relationships detected in: {linear_features}")
print(f"Non-linear relationships detected in: {non_linear_features}")

# Save model insights
model_insights_path = os.path.join(OUTPUT_DIR, 'model_selection_insights.txt')
with open(model_insights_path, 'w') as f:
    f.write("Model Selection Insights:\n")
    f.write(f"Dataset size: {len(df_clean)} records\n")
    f.write(f"Class imbalance: {class_dist[1]/len(df_clean)*100:.1f}% delinquent customers\n")
    f.write(f"Top features: {', '.join(top_5_features['Feature'].tolist())}\n")
    f.write(f"Linear relationships: {', '.join(linear_features)}\n")
    f.write(f"Non-linear relationships: {', '.join(non_linear_features)}\n")
    f.write(f"High-risk factors: {', '.join([k for k, v in risk_analysis.items() if v['delinquency_rate'] > 15])}\n")

print("\nAnalysis complete. Outputs saved in task-2 directory.") 