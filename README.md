# Geldium AI-Powered Collections Strategy Project

## About This Project

**Tata Group Data Analytics Job Simulation on Forage - June 2025**

- Completed a job simulation involving AI-powered data analytics and strategy development for the Financial Services team at Tata iQ.
- Conducted exploratory data analysis (EDA) using GenAI tools to assess data quality, identify risk indicators, and structure insights for predictive modeling.
- Proposed and justified an initial no-code predictive modeling framework to assess customer delinquency risk, leveraging GenAI for structured model logic and evaluation criteria.
- Designed an AI-driven collections strategy leveraging agentic AI and automation, incorporating ethical AI principles, regulatory compliance, and scalable implementation frameworks.

## Project Overview

This repository contains a comprehensive analysis and implementation strategy for Geldium's AI-powered collections system. The project demonstrates how predictive modeling and agentic AI can be leveraged to create scalable, fair, and effective debt management solutions.

## Project Structure

```
├── data/
│   └── Delinquency_prediction_dataset.csv    # Original dataset
├── task-1-eda/
│   ├── eda_analysis.py                       # EDA analysis script
│   ├── eda_summary_report.txt                # Comprehensive EDA report
│   ├── correlation_matrix.png                # Correlation visualization
│   ├── data_quality_summary.txt              # Data quality assessment
│   ├── missing_data.csv                      # Missing data analysis
│   ├── outlier_summary.csv                   # Outlier analysis
│   └── risk_correlations.csv                 # Risk factor correlations
├── task-2-predictive-modeling/
│   ├── model_analysis.py                     # Predictive modeling script
│   ├── summary-report.txt                    # Model analysis report
│   ├── feature_importance.csv                # Feature importance rankings
│   ├── class_distribution.txt                # Target variable distribution
│   └── top_5_features.txt                    # Top predictive features
├── task-3-business-report/
│   └── summary-report.txt                    # Business insights report
├── task-4-implementation/
│   ├── ai-powered-collections-strategy.pptx  # Executive presentation
│   ├── executive-summary.txt                 # Implementation summary
└── README.md                                 # This file
```

## Key Findings

### Task 1: Exploratory Data Analysis

- **Dataset**: 502 records with 15 features related to customer financial behavior
- **Key Risk Indicators**: Income, account tenure, and credit score show strongest correlations with delinquency
- **Data Quality**: 12% missing data in income field, requiring strategic imputation
- **Outliers**: Identified in credit utilization and account balance fields

### Task 2: Predictive Modeling

- **Model**: Logistic Regression with feature engineering
- **Top Predictors**: Credit utilization ratio, account tenure, credit score
- **Performance Metrics**: AUC-ROC, F1-score, precision, recall
- **Ethical Considerations**: Bias detection and fairness monitoring implemented

### Task 3: Business Strategy

- **High-Risk Segment**: Customers with >80% credit utilization
- **SMART Recommendation**: Targeted intervention program with 30-day implementation timeline
- **Expected Impact**: 25% reduction in delinquency rates

### Task 4: AI Implementation

- **System Architecture**: Hybrid human-AI oversight model
- **Responsible AI**: Built-in fairness checks and explainability requirements
- **Business Impact**: Scalable collections with improved customer experience

## Technical Requirements

### Python Dependencies

```python
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/geldium-ai-collections.git
cd geldium-ai-collections

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running EDA Analysis

```bash
cd task-1-eda
python eda_analysis.py
```

### Running Predictive Modeling

```bash
cd task-2-predictive-modeling
python model_analysis.py
```

## Business Impact

This AI-powered collections strategy is designed to:

- **Reduce Delinquency**: 25% improvement in collection rates
- **Enhance Efficiency**: 40% reduction in manual intervention
- **Improve Customer Experience**: Personalized, fair treatment
- **Ensure Compliance**: Built-in regulatory and ethical safeguards

## Ethical Considerations

- **Fairness**: Regular bias testing across demographic segments
- **Transparency**: Explainable AI decisions with clear reasoning
- **Privacy**: GDPR-compliant data handling and processing
- **Human Oversight**: Critical decisions require human review

---

**Developed for Geldium's AI-Powered Collections Strategy Initiative**  
*Tata Group Data Analytics Job Simulation on Forage - June 2025*
