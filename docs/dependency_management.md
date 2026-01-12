# 📦 Dependency Management Guide

This guide explains how to manage project dependencies.

---

## 📋 Requirements Files

### `requirements.txt`
**Purpose**: Core dependencies needed to run the project  
**Use case**: Production, basic usage, Google Colab

```bash
pip install -r requirements.txt
```

---

## 🐍 Python Version

**Recommended**: Python 3.9 or higher  
**Specified in**: `.python-version` file

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

### Using pyenv (Recommended)

```bash
# Install pyenv (macOS/Linux)
curl https://pyenv.run | bash

# Install Python 3.9
pyenv install 3.9

# Set local version
pyenv local 3.9

# Verify
python --version
```

---

## 🔧 Installation Methods

### Method 1: Basic Installation

```bash
# Install core dependencies
pip install -r requirements.txt
```

### Method 2: Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### Method 3: Conda Environment

```bash
# Create conda environment
conda create -n bike-ds python=3.9

# Activate
conda activate bike-ds

# Install dependencies
pip install -r requirements.txt

# Or install with conda when possible
conda install pandas numpy scikit-learn matplotlib seaborn
pip install -r requirements.txt  # For packages not in conda
```

---

## 📦 Package Versions

### Version Specifiers Explained

- `pandas>=2.0.0` - Install version 2.0.0 or higher
- `pandas==2.0.0` - Install exactly version 2.0.0 (more restrictive)
- `pandas~=2.0.0` - Compatible release (>=2.0.0, <3.0.0)

**Our approach**: We use `>=` to allow compatible updates while maintaining minimum required versions.

---

## 🔄 Updating Dependencies

### Update All Packages

```bash
pip install --upgrade -r requirements.txt
```

### Update Specific Package

```bash
pip install --upgrade pandas
```

### Check Outdated Packages

```bash
pip list --outdated
```

### Freeze Current Versions

```bash
# Save exact versions you have installed
pip freeze > requirements-lock.txt
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Package Conflicts

**Problem**: Incompatible package versions

**Solution**:
```bash
# Clear cache and reinstall
pip cache purge
pip install --no-cache-dir -r requirements.txt
```

### Issue 2: Permission Denied

**Problem**: Need admin rights to install

**Solution**:
```bash
# Install for user only
pip install --user -r requirements.txt

# Or use virtual environment (better)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Issue 3: Old pip Version

**Problem**: pip is outdated

**Solution**:
```bash
# Upgrade pip first
pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

### Issue 4: SSL Certificate Error

**Problem**: SSL certificate verification failed

**Solution**:
```bash
# Upgrade certifi
pip install --upgrade certifi

# Or temporarily bypass (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

---

## 🎓 Google Colab

### Install in Colab Notebook

```python
# Quiet installation (less output)
!pip install -q -r requirements.txt

# Or verbose
!pip install -r requirements.txt
```

### Install Specific Packages

```python
# Install only what you need
!pip install -q pandas numpy matplotlib scikit-learn
```

---

## 📝 Key Package Notes

### pandas-profiling → ydata-profiling

**Old name**: `pandas-profiling`  
**New name**: `ydata-profiling`  

If you see import errors, use:
```python
# Old (deprecated)
# import pandas_profiling

# New (current)
from ydata_profiling import ProfileReport
```

### MLflow

For experiment tracking, MLflow may need additional setup:

```bash
# Start MLflow UI
mlflow ui

# Then open browser to: http://localhost:5000
```

### Streamlit

To run the dashboard:

```bash
streamlit run apps/streamlit_dashboard.py
```

---

## 🧪 Testing Installation

### Verify All Packages

```python
# test_imports.py
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import streamlit
import mlflow
import requests

print("✅ All packages imported successfully!")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
```

Run with:
```bash
python test_imports.py
```

---

## 📊 Dependency Tree

```
├── Data Processing
│   ├── pandas (data manipulation)
│   ├── numpy (numerical computing)
│   └── scipy (scientific computing)
│
├── Machine Learning
│   ├── scikit-learn (ML algorithms)
│   ├── xgboost (gradient boosting)
│   └── shap (model interpretation)
│
├── Visualization
│   ├── matplotlib (plotting)
│   ├── seaborn (statistical viz)
│   └── plotly (interactive viz)
│
├── MLOps
│   ├── mlflow (experiment tracking)
│   └── papermill (notebook automation)
│
├── Data Acquisition
│   └── requests (HTTP/API calls)
│
└── Development
    ├── black (code formatting)
    ├── pylint (linting)
    ├── pytest (testing)
    └── jupyter (notebooks)
```

---

## 🔐 Security Best Practices

### Check for Vulnerabilities

```bash
# Install safety
pip install safety

# Check for known security issues
safety check -r requirements.txt
```

### Keep Packages Updated

```bash
# Regular updates for security patches
pip install --upgrade -r requirements.txt
```

---

## 💡 Pro Tips

### Tip 1: Use pip-tools

```bash
# Install pip-tools
pip install pip-tools

# Compile locked requirements
pip-compile requirements.txt

# Creates requirements.txt with exact versions
```

### Tip 2: Speed Up Installation

```bash
# Use pip's caching
pip install -r requirements.txt

# Parallel downloads (faster)
pip install --use-feature=fast-deps -r requirements.txt
```

### Tip 3: Minimal Install for Colab

If working in Colab, many packages are pre-installed. Only install what's missing:

```python
# Check what's already installed
!pip list | grep pandas

# Only install if missing
try:
    import mlflow
except ImportError:
    !pip install -q mlflow
```

---

## 📚 Resources

- [pip Documentation](https://pip.pypa.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Managing Dependencies](https://realpython.com/courses/managing-python-dependencies/)

---