# Python Version and Environment Setup

This document explains the Python version requirements and how to set up your environment.

## 🐍 Python Version Requirements

**Required:** Python 3.9 or higher  
**Tested with:** Python 3.9, 3.10, 3.11, 3.12  
**Recommended:** Python 3.9 for maximum compatibility

### Why Python 3.9?

- ✅ **Stable and mature** - Released October 2020
- ✅ **Wide library support** - All data science packages work well
- ✅ **Google Colab compatible** - Runs in cloud environments
- ✅ **Balance** - Not too old, not bleeding edge

### Version Files

This repository includes:
- **`.python-version`** - Specifies Python 3.9 (for pyenv and similar tools)
- **`pyproject.toml`** - Formally requires `>=3.9,<3.13`

## 🔧 Setting Up Your Environment

### Option 1: Using pyenv (Recommended for Local Development)

```bash
# Install Python 3.9 if not already installed
pyenv install 3.9.18  # or latest 3.9.x

# Set local Python version for this project
pyenv local 3.9.18

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -e .           # Installs project + dependencies
# OR
pip install -r requirements.txt
```

### Option 2: Using System Python

```bash
# Check your Python version
python --version  # Should be 3.9 or higher

# Create virtual environment
python3.9 -m venv .venv  # Specify version explicitly

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -e .
```

### Option 3: Using Conda

```bash
# Create environment with Python 3.9
conda create -n bike-ds python=3.9

# Activate environment
conda activate bike-ds

# Install dependencies
pip install -e .
# OR use conda for some packages
conda install pandas numpy scikit-learn matplotlib seaborn
pip install -r requirements.txt  # For remaining packages
```

### Option 4: Google Colab (No Setup Needed!)

Google Colab comes with Python pre-installed. Just run:

```python
# In a Colab notebook cell
!pip install -r requirements.txt
```

## 📦 Installation Options

### Basic Installation

```bash
pip install -e .
```

This installs all core dependencies listed in `pyproject.toml`.

### Traditional Installation

```bash
pip install -r requirements.txt
```

Uses the traditional requirements file approach.

## 🔍 Verifying Your Setup

After installation, verify everything works:

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Run a quick test
python -c "import pandas, numpy, sklearn; print('✅ All core packages working!')"
```

## ⚙️ Using pyproject.toml

The `pyproject.toml` file provides several benefits for students:

### 1. Dependency Management

All dependencies are declared in one place with version constraints:

```toml
dependencies = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    # ... more
]
```

### 2. Tool Configuration

Settings for code quality tools to help you write better code:
- **Black** - Code formatting
- **Pylint** - Linting
- **MyPy** - Type checking

## 🛠️ Common Issues

### Issue: Wrong Python Version

**Problem:** Virtual environment created with wrong Python version

**Solution:**
```bash
# Delete existing venv
rm -rf .venv

# Create new venv with specific Python version
python3.9 -m venv .venv

# Activate and reinstall
source .venv/bin/activate
pip install -e .
```

### Issue: pyenv not setting correct version

**Problem:** `.python-version` not being respected

**Solution:**
```bash
# Check available Python versions
pyenv versions

# Install Python 3.9 if missing
pyenv install 3.9.18

# Set local version explicitly
pyenv local 3.9.18

# Verify
python --version  # Should show 3.9.x
```

### Issue: Package installation failures

**Problem:** Some packages fail to install

**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip setuptools wheel

# Try installing again
pip install -e .

# If specific package fails, try installing separately
pip install problematic-package
```

## 📚 Additional Resources

- [pyenv documentation](https://github.com/pyenv/pyenv)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/)
- [Course Dependency Management Guide](dependency_management.md)

## 🔄 Keeping Dependencies Updated

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update all packages (use with caution!)
pip install --upgrade -r requirements.txt
```

## ✅ Checklist

Before starting the course, ensure:

- [ ] Python 3.9+ is installed
- [ ] Virtual environment is created and activated
- [ ] All dependencies are installed (`pip install -e .`)
- [ ] Import test passes (pandas, numpy, sklearn work)
- [ ] You can run Jupyter notebooks
