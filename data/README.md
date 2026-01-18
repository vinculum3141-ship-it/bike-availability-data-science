# 📊 Data Directory

This directory contains all data used in the bike availability prediction project.

---

## 📁 Directory Structure

```
data/
├── raw/           # Original, immutable data
└── processed/     # Cleaned and transformed data
```

---

## 🗂️ Data Organization

### `raw/` - Raw Data

**Purpose**: Store original, unmodified datasets exactly as downloaded

**Guidelines**:
- ✅ Keep data in original format (CSV, JSON, etc.)
- ✅ Never modify files in this folder
- ✅ Include data source documentation
- ✅ Add date stamps to filenames

**Naming Convention**:
```
{source}_{description}_{YYYY-MM-DD}.{ext}

Examples:
├── amsterdam_bike_api_2024-01-15.json
├── knmi_weather_2024-01-15.csv
├── openchargemap_stations_2024-01-15.json
└── README.md (describe each file)
```

**See**: [raw/README.md](raw/README.md) for detailed organization

---

### `processed/` - Processed Data

**Purpose**: Store cleaned, merged, and feature-engineered datasets

**Guidelines**:
- ✅ Document all transformations
- ✅ Include version numbers
- ✅ Save in efficient formats (parquet, feather)
- ✅ Keep processing scripts traceable

**Naming Convention**:
```
{stage}_{description}_v{version}.{ext}

Examples:
├── cleaned_bike_weather_v1.parquet
├── featured_bike_availability_v2.parquet
└── README.md (describe transformations)
```

**See**: [processed/README.md](processed/README.md) for detailed organization

---

## 🌐 Data Sources

For this project, you'll work with open data from:

| Source | Data Type | Module |
|--------|-----------|--------|
| Amsterdam Open Data | Bike availability | Module 02 |
| KNMI | Weather data | Module 02 |
| OpenChargeMap | Charging stations | Module 02 |
| Custom APIs | Time-series data | Module 02 |

**Complete list**: See [docs/open_data_sources.md](../docs/references/open_data_sources.md)

---

## 🔒 Data Security & Privacy

### Do NOT Commit

- ❌ Large datasets (> 100MB)
- ❌ Personal/sensitive data
- ❌ API keys or credentials
- ❌ Raw data downloads (unless small samples)

### What to Use Instead

- ✅ `.gitignore` entries for data files
- ✅ Sample datasets (< 10MB)
- ✅ Data acquisition scripts
- ✅ Documentation of data sources

---

## 📥 Getting Data

### Option 1: Download from Sources

```python
# See Module 02 notebooks for API examples
import requests

# Example: Amsterdam Bike API
url = "https://api.amsterdam.nl/bikes"
response = requests.get(url)
data = response.json()
```

### Option 2: Generate Sample Data

```python
# For testing pipelines without real data
import pandas as pd
import numpy as np

# Generate sample bike availability data
dates = pd.date_range('2024-01-01', periods=1000, freq='H')
sample_data = pd.DataFrame({
    'timestamp': dates,
    'station_id': np.random.choice(['S001', 'S002', 'S003'], 1000),
    'bikes_available': np.random.randint(0, 20, 1000),
    'temperature': np.random.uniform(0, 25, 1000)
})
```

---

## 🛠️ Data Pipeline Flow

```
1. ACQUIRE (Module 02)
   ├── APIs, downloads, web scraping
   ├── Save to raw/
   └── Document sources

2. EXPLORE (Module 03)
   ├── Load from raw/
   ├── Profiling and EDA
   └── Identify quality issues

3. CLEAN (Module 04)
   ├── Handle missing values
   ├── Remove duplicates
   ├── Fix data types
   └── Save to processed/cleaned_*.parquet

4. ENGINEER (Module 04)
   ├── Create features
   ├── Encode categories
   ├── Scale/normalize
   └── Save to processed/featured_*.parquet

5. MODEL (Module 05)
   ├── Train/test splits
   ├── Model training
   └── Save predictions to processed/
```

---

## 📚 Code Snippets for Data Operations

### Loading Data

```python
import pandas as pd

# Load raw CSV
df = pd.read_csv('data/raw/amsterdam_bike_api_2024-01-15.csv')

# Load processed parquet (faster)
df = pd.read_parquet('data/processed/cleaned_bike_weather_v1.parquet')

# Load JSON
df = pd.read_json('data/raw/openchargemap_stations_2024-01-15.json')
```

### Saving Data

```python
# Save to parquet (recommended for processed data)
df.to_parquet('data/processed/cleaned_bike_weather_v1.parquet', index=False)

# Save to CSV (for raw data)
df.to_csv('data/raw/amsterdam_bike_api_2024-01-15.csv', index=False)
```

**More examples**: [docs/code_snippets.md](../docs/references/code_snippets.md)

---

## 🧪 Data Validation

Before using data in models, always validate:

```python
# Check for issues
print(f"Shape: {df.shape}")
print(f"Missing: {df.isnull().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
print(f"Data types:\n{df.dtypes}")
```

**Tools**:
- `pandas-profiling` (now `ydata-profiling`) - Automated reports
- `great_expectations` - Data validation pipelines

---

## 📦 Dependencies for Data Work

Make sure you have these installed:

```bash
pip install pandas numpy scipy ydata-profiling
```

**See**: [docs/dependency_management.md](../docs/setup/dependency_management.md) for complete setup

---

## 📖 Additional Resources

### Documentation
- 📐 [Coding Standards](../docs/standards/coding_standards.md) - Data handling best practices
- 📚 [Code Snippets](../docs/references/code_snippets.md) - Quick data operations
- 🌐 [Open Data Sources](../docs/references/open_data_sources.md) - Where to get data

### Module Guides
- 📓 [Module 02: Data Acquisition](../notebooks/Module_02_Data_Acquisition/) - API usage
- 📓 [Module 03: Exploration](../notebooks/Module_03_Exploration_Profiling/) - EDA techniques
- 📓 [Module 04: Feature Engineering](../notebooks/Module_04_Feature_Engineering/) - Transformations

---

## ✅ Data Quality Checklist

Before moving data to processed/:

- [ ] Source documented (where did it come from?)
- [ ] Date stamp included
- [ ] No personal/sensitive information
- [ ] Reasonable file size (< 100MB or compressed)
- [ ] Missing values handled
- [ ] Data types correct
- [ ] Duplicates removed
- [ ] Transformations documented

---

## 🆘 Common Issues

### Issue: File too large for Git
**Solution**: Add to `.gitignore` and document how to obtain it

### Issue: Missing data files
**Solution**: Run data acquisition notebooks in Module 02

### Issue: Import errors
**Solution**: Check [dependency_management.md](../docs/setup/dependency_management.md)

### Issue: Can't find data files
**Solution**: Use relative paths from project root:
```python
import os
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
```

---

**Next steps**: Start with [Module 02](../notebooks/Module_02_Data_Acquisition/) to acquire your first dataset! 🚀
