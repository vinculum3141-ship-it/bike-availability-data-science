# Processed Data Directory

This directory stores **cleaned, transformed, and feature-engineered data** ready for modeling.

---

## 📌 Purpose

Processed data is derived from raw data through:
- Data cleaning
- Feature engineering
- Transformations
- Aggregations
- Merging multiple sources

This separates raw data from analysis-ready data.

---

## 📤 What Goes Here

### Cleaned Data
- Files: `bike_data_cleaned.csv`
- Description: Raw data after cleaning (missing values handled, outliers removed)
- Traceability: Document cleaning steps in notebooks

### Merged Data
- Files: `bike_weather_merged.csv`
- Description: Combined bike and weather data
- Key: Timestamp and station_id

### Feature-Engineered Data
- Files: `features_train.csv`, `features_val.csv`, `features_test.csv`
- Description: Data with engineered features ready for modeling
- Splits: Separate files for train/validation/test

### Model-Ready Data
- Files: `X_train.csv`, `y_train.csv`, `X_test.csv`, `y_test.csv`
- Description: Final preprocessed features and target variable
- Format: Ready to load directly into models

---

## 📝 Naming Convention

Use descriptive names that indicate processing stage:

```
{data_type}_{processing_stage}_{split}.{extension}

Examples:
- bike_data_cleaned.csv
- bike_weather_merged.csv
- features_engineered.csv
- features_train.csv
- features_test.csv
- X_train_scaled.pkl
- y_train.csv
```

---

## 🔄 Processing Pipeline

```
RAW DATA (data/raw/)
    ↓
[Cleaning & Validation]
    ↓
CLEANED DATA (bike_data_cleaned.csv)
    ↓
[Merging Multiple Sources]
    ↓
MERGED DATA (bike_weather_merged.csv)
    ↓
[Feature Engineering]
    ↓
FEATURE DATA (features_engineered.csv)
    ↓
[Train/Val/Test Split]
    ↓
SPLIT DATA (features_train.csv, features_val.csv, features_test.csv)
    ↓
[Scaling & Encoding]
    ↓
MODEL-READY DATA (X_train_scaled.pkl, y_train.csv)
```

---

## 📋 Processing Documentation

For each processed file, document:

### Example Documentation

```markdown
## File: features_engineered.csv

**Created**: 2024-02-15  
**Source**: bike_weather_merged.csv  
**Processing Script**: notebooks/Module_04_Feature_Engineering/M4_04_final_features.ipynb  

**Transformations Applied**:
1. Created temporal features (hour, day_of_week, is_weekend)
2. Created lag features (bikes_lag_1h, bikes_lag_3h)
3. Created rolling features (rolling_mean_24h)
4. Binned temperature into categories
5. Encoded categorical variables

**Shape**: 438,000 rows × 25 columns  
**Features**: [list of feature names]  
**Target**: bikes_available  

**Data Splits**:
- Train: 70% (Jan-Aug 2024)
- Validation: 15% (Sep-Oct 2024)
- Test: 15% (Nov-Dec 2024)

**Quality Checks**:
- No missing values
- No duplicate rows
- All features scaled to [0, 1] range
- No data leakage verified
```

---

## 💾 File Formats

### CSV (Recommended for tabular data)
```python
import pandas as pd

# Save
df.to_csv('data/processed/features_train.csv', index=False)

# Load
df = pd.read_csv('data/processed/features_train.csv')
```

### Parquet (For larger files)
```python
# Advantages: Smaller size, faster loading, preserves dtypes
df.to_parquet('data/processed/features_train.parquet')
df = pd.read_parquet('data/processed/features_train.parquet')
```

### Pickle (For Python objects)
```python
import pickle

# Save (e.g., scaler objects, complex transformations)
with open('data/processed/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Load
with open('data/processed/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
```

---

## 🔐 Reproducibility

### Save Processing Scripts

Create reproducible processing pipelines:

```python
# Example: processing_pipeline.py

import pandas as pd
from src.preprocessing import clean_data
from src.feature_engineering import create_features

def process_data(raw_path, output_path):
    """
    End-to-end data processing pipeline.
    
    Args:
        raw_path: Path to raw data
        output_path: Path to save processed data
    """
    # Load raw data
    df = pd.read_csv(raw_path)
    
    # Clean
    df_clean = clean_data(df)
    
    # Engineer features
    df_features = create_features(df_clean)
    
    # Save
    df_features.to_csv(output_path, index=False)
    
    print(f"✅ Processed data saved to {output_path}")
    return df_features

if __name__ == "__main__":
    process_data(
        'data/raw/bike_data.csv',
        'data/processed/features_engineered.csv'
    )
```

### Save Processing Metadata

```python
import json
from datetime import datetime

metadata = {
    'processing_date': datetime.now().isoformat(),
    'source_files': ['bike_data.csv', 'weather_data.csv'],
    'processing_steps': [
        'Remove duplicates',
        'Handle missing values',
        'Create lag features',
        'Scale features'
    ],
    'shape': df.shape,
    'columns': df.columns.tolist()
}

with open('data/processed/features_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

---

## ⚠️ Important Considerations

### Data Leakage Prevention
```python
# ❌ WRONG: Fit scaler on all data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# ✅ CORRECT: Fit on train, transform on train/val/test
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)  # Note: transform, not fit_transform
X_test_scaled = scaler.transform(X_test)
```

### Temporal Ordering
```python
# For time series: respect temporal order
df = df.sort_values('timestamp')

# Split chronologically
train = df[df['timestamp'] < '2024-09-01']
val = df[(df['timestamp'] >= '2024-09-01') & (df['timestamp'] < '2024-11-01')]
test = df[df['timestamp'] >= '2024-11-01']
```

---

## 📊 Data Quality Checks

Before saving processed data:

```python
def validate_processed_data(df):
    """Validate processed data quality."""
    
    checks = {
        'No missing values': df.isnull().sum().sum() == 0,
        'No duplicates': df.duplicated().sum() == 0,
        'Correct shape': len(df) > 0,
        'Required columns': all(col in df.columns for col in ['timestamp', 'target']),
        'Valid date range': df['timestamp'].is_monotonic_increasing,
        'No infinite values': ~df.select_dtypes(include='number').isin([np.inf, -np.inf]).any().any()
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}")
    
    return all(checks.values())

# Use it
if validate_processed_data(df_processed):
    df_processed.to_csv('data/processed/features_engineered.csv', index=False)
    print("✅ Data validation passed. File saved.")
else:
    print("❌ Data validation failed. Please fix issues.")
```

---

## 🗂️ Example Directory Structure

```
data/processed/
├── README.md (this file)
├── .gitkeep
├── bike_data_cleaned.csv
├── bike_weather_merged.csv
├── features_engineered.csv
├── features_train.csv
├── features_val.csv
├── features_test.csv
├── X_train_scaled.pkl
├── X_val_scaled.pkl
├── X_test_scaled.pkl
├── y_train.csv
├── y_val.csv
├── y_test.csv
├── scaler.pkl
├── feature_names.json
└── processing_metadata.json
```

---

## ✅ Checklist: Saving Processed Data

Before saving:

- [ ] Data is cleaned and validated
- [ ] Transformations are documented
- [ ] No data leakage (features don't use future info)
- [ ] Train/val/test splits are separate files
- [ ] Scalers/encoders are saved (for reproducibility)
- [ ] Processing script or notebook is committed
- [ ] Metadata file created
- [ ] File naming follows convention
- [ ] Quality checks passed

---

## 🔗 Related Resources

- [Feature Engineering Module](../../notebooks/Module_04_Feature_Engineering/)
- [Preprocessing Module](../../src/preprocessing.py)
- [Feature Engineering Module](../../src/feature_engineering.py)
- [Raw Data Directory](../raw/README.md)

---

**Remember**: Processed data should be reproducible. Always save the code that created it! 🔄
