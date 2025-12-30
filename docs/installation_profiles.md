# Installation Options Comparison

> **⚡ Quick Decision Tree**: [Jump to "Which Should You Use?"](#-which-should-you-use)

This document explains the different ways to install dependencies and what each includes.

---

## 🧭 Quick Start: Choose Your Path

```
START: What are you doing?
│
└─ 📚 Taking the course / Learning data science
   └─ ✅ Choose your installation method:
      │
      ├─ No installation? → Use Google Colab (easiest!)
      ├─ Want automation? → Run ./setup.sh
      └─ Manual control? → pip install -e .
```

**� All installation methods give you everything needed for the course!**

---

## 📦 What You'll Get

### Core Installation (For Course)

**What you get:**
- ✅ All core data science packages
- ✅ Everything needed for notebooks
- ✅ Basic code quality tools (black, pylint, flake8)
- ✅ Dashboard tools (streamlit)

**Install:**
```bash
pip install -e .
```

**Use case:** You're taking the course, working through notebooks, learning data science.

---

## 📊 Package Overview

Your installation includes approximately **18 core packages** for data science learning.

---

## 🎯 Installation Methods Comparison

### Method 1: Using pyproject.toml (Modern - Recommended)

```bash
pip install -e .
```

**Pros:**
- ✅ Clean, standardized
- ✅ Tool configs included

**Cons:**
- Requires understanding of package installation syntax

---

### Method 2: Using requirements files (Traditional)

```bash
pip install -r requirements.txt
```

**Pros:**
- ✅ Familiar to most users
- ✅ Simple syntax
- ✅ Works everywhere

**Cons:**
- ❌ No tool configuration
- ❌ No entry points

---

### Method 3: Using setup.sh (Automated)

```bash
./setup.sh
```

**Pros:**
- ✅ Most beginner-friendly
- ✅ Checks Python version
- ✅ Creates venv automatically
- ✅ Verifies installation

**Cons:**
- Only for bash/Linux/macOS (Windows users need WSL or manual setup)

---

## 🤔 Which Should You Use?

### 🎓 For Students/Learners (Recommended)

**👉 You're taking this course and want to learn data science**

**Best options (pick ONE):**

1. **🌐 Google Colab** (No installation at all!)
   - Open notebooks directly in browser
   - See [Google Colab Setup Guide](setup_google_colab.md)
   - ✅ Fastest way to start learning

2. **🚀 Automated Script** (Easiest local setup)
   ```bash
   ./setup.sh
   ```
   - Handles everything automatically
   - See [Setup Script Guide](setup_script_guide.md)

3. **🎯 Modern Install** (Manual but clean)
   ```bash
   pip install -e .
   ```
   - Uses modern Python standards

4. **📜 Traditional Install** (If preferred)
   ```bash
   pip install -r requirements.txt
   ```
   - Classic requirements file approach

**What you get:** All core packages for data science learning

---

## 📝 What's in the Installation?

### Core Packages Include:
```
pandas, numpy, scipy
scikit-learn, xgboost, shap
matplotlib, seaborn, plotly
requests
ydata-profiling
mlflow
papermill, ipywidgets
streamlit
black, pylint, flake8, mypy
python-dotenv, python-dateutil, tqdm
```

---

## ✅ Verification

After installation, verify what you have:

```bash
# Check installed packages
pip list

# Test that core packages work
python -c "import pandas, numpy, sklearn; print('✅ All core packages working!')"
```

---

## 🆘 Troubleshooting

### "Too many packages, slow installation"
Be patient! All packages are needed for the course activities.

### "I want JupyterLab"
```bash
pip install -e .
pip install jupyterlab
```

---

## 📚 Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [pyproject.toml specification](https://peps.python.org/pep-0621/)
- [Dependency Management Guide](dependency_management.md)
- [Python Version Setup](python_version_setup.md)

---

**Bottom line:** All installation methods provide everything you need for the course. Choose the one that works best for you! 🎯
