# 📐 Python Coding Standards

A practical guide to writing clean, professional Python code for data science projects.

---

## 🎯 Why Coding Standards Matter

- **Readability**: Others (and future you) can understand your code
- **Maintainability**: Easy to modify and extend
- **Collaboration**: Team members can work together smoothly
- **Professionalism**: Demonstrates good software engineering practices
- **Debugging**: Clean code is easier to debug

---

## 📏 PEP 8 Basics

Python has an official style guide called [PEP 8](https://pep8.org/). Here are the essentials:

### 1. Naming Conventions

```python
# ✅ GOOD: Clear, descriptive names

# Variables and functions: lowercase_with_underscores
bike_count = 10
available_bikes = get_available_bikes()

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_BIKES_PER_STATION = 50
API_BASE_URL = "https://api.example.com"

# Classes: CapitalizedWords
class BikeStation:
    pass

class WeatherDataProcessor:
    pass

# Private variables/methods: _leading_underscore
def _internal_helper_function():
    pass

# ❌ BAD: Unclear or inconsistent
bc = 10  # Too short
BikeCount = 10  # Wrong case for variable
get_AvailableBikes()  # Inconsistent case
MAXBIKES = 50  # Missing underscore
```

### 2. Indentation and Spacing

```python
# ✅ GOOD: 4 spaces for indentation

def calculate_availability(total_bikes, bikes_in_use):
    available = total_bikes - bikes_in_use
    return available

if available_bikes > 0:
    print("Bikes available!")
else:
    print("No bikes available")

# Add spaces around operators
result = (a + b) * c

# Two blank lines between functions/classes
def function_one():
    pass


def function_two():
    pass


# ❌ BAD: Inconsistent spacing
def bad_function( a,b ):  # Extra spaces
    result=a+b  # No spaces around operators
    return result
```

### 3. Line Length

```python
# ✅ GOOD: Keep lines under 79-88 characters

# Break long lines using parentheses
result = (long_variable_name + another_long_name 
          + yet_another_variable)

# Break function calls
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# Break long strings
message = (
    "This is a very long message that would exceed "
    "the line length limit if written on one line"
)

# ❌ BAD: Lines that are too long
result = really_long_variable_name + another_really_long_variable_name + yet_another_very_long_variable_name
```

### 4. Imports

```python
# ✅ GOOD: Organized imports

# Standard library imports
import os
import sys
from datetime import datetime

# Third-party imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Local imports
from src.data_acquisition import fetch_bike_data
from src.preprocessing import clean_data

# ❌ BAD: Disorganized imports
import pandas as pd, numpy as np  # Don't combine
from src.data_acquisition import *  # Don't use wildcard imports
import matplotlib.pyplot as plt
import os  # Should be at top
```

---

## 📝 Docstrings and Comments

### Function Docstrings

```python
# ✅ GOOD: Clear docstring with Google style

def calculate_bike_availability(station_data, current_time):
    """
    Calculate bike availability for a station at a given time.
    
    Args:
        station_data (pd.DataFrame): DataFrame with station information
        current_time (datetime): Time for which to calculate availability
        
    Returns:
        int: Number of available bikes
        
    Raises:
        ValueError: If station_data is empty
        
    Example:
        >>> data = pd.DataFrame({'bikes': [10, 15, 20]})
        >>> availability = calculate_bike_availability(data, datetime.now())
        >>> print(availability)
        15
    """
    if station_data.empty:
        raise ValueError("Station data cannot be empty")
    
    # Implementation here
    available = station_data.loc[current_time, 'bikes_available']
    return available


# ❌ BAD: No docstring or unclear
def calc(d, t):
    # calculate stuff
    return d.loc[t, 'bikes_available']
```

### Comments

```python
# ✅ GOOD: Comments explain WHY, not WHAT

# Use 24-hour lag because bike patterns show daily seasonality
lag_hours = 24
df['bikes_lag_24h'] = df['bikes_available'].shift(lag_hours)

# Remove outliers beyond 99th percentile (sensor errors)
threshold = df['bikes_available'].quantile(0.99)
df = df[df['bikes_available'] <= threshold]


# ❌ BAD: Comments state the obvious

# Create a new column
df['new_column'] = df['old_column'] * 2  # Multiply by 2

# Loop through the data
for i in range(len(df)):  # Comment adds no value
    pass
```

---

## 🔧 Data Science Specific Standards

### 1. Variable Names for DataFrames

```python
# ✅ GOOD: Descriptive names

df_bikes = pd.read_csv('bike_data.csv')
df_weather = pd.read_csv('weather_data.csv')
df_merged = pd.merge(df_bikes, df_weather, on='timestamp')

# For transformations, indicate the state
df_raw = load_raw_data()
df_clean = clean_data(df_raw)
df_features = engineer_features(df_clean)


# ❌ BAD: Generic or confusing names
df1 = pd.read_csv('bike_data.csv')
data = pd.read_csv('weather_data.csv')
final = pd.merge(df1, data)
```

### 2. Magic Numbers

```python
# ✅ GOOD: Use named constants

TRAIN_SIZE = 0.7
VALIDATION_SIZE = 0.15
TEST_SIZE = 0.15
RANDOM_SEED = 42

train_idx = int(len(df) * TRAIN_SIZE)
val_idx = int(len(df) * (TRAIN_SIZE + VALIDATION_SIZE))

model = RandomForestRegressor(random_state=RANDOM_SEED)


# ❌ BAD: Unexplained numbers
train_idx = int(len(df) * 0.7)  # What is 0.7?
model = RandomForestRegressor(random_state=42)  # Why 42?
```

### 3. Pandas Best Practices

```python
# ✅ GOOD: Clear, vectorized operations

# Use vectorized operations
df['is_weekend'] = df['day_of_week'].isin([5, 6])

# Chain operations clearly
df_processed = (
    df
    .dropna()
    .sort_values('timestamp')
    .reset_index(drop=True)
)

# Use loc/iloc explicitly
bikes_in_morning = df.loc[df['hour'] < 12, 'bikes_available']


# ❌ BAD: Inefficient or unclear
# Don't use loops for operations that can be vectorized
for i in range(len(df)):
    if df.iloc[i]['day_of_week'] in [5, 6]:
        df.iloc[i]['is_weekend'] = True

# Don't use chained assignment (SettingWithCopyWarning)
df[df['hour'] < 12]['bikes_available'] = 0
```

### 4. Model Training Code

```python
# ✅ GOOD: Organized, reproducible

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Set random seed for reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Define model parameters clearly
model_params = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'random_state': RANDOM_SEED,
    'n_jobs': -1
}

# Train model
model = RandomForestRegressor(**model_params)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:")
print(f"  MAE: {mae:.2f}")
print(f"  R²: {r2:.3f}")


# ❌ BAD: Hard to reproduce or understand
model = RandomForestRegressor(100, 10, 5, 42)  # What are these numbers?
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # What metric is this?
```

---

## 🎨 Code Organization

### 1. Notebook Structure

```python
# ✅ GOOD: Organized notebook sections

# ═══════════════════════════════════════════════════════════
# 1. SETUP & IMPORTS
# ═══════════════════════════════════════════════════════════

import pandas as pd
import numpy as np

# ═══════════════════════════════════════════════════════════
# 2. CONFIGURATION
# ═══════════════════════════════════════════════════════════

DATA_PATH = 'data/raw/bike_data.csv'
RANDOM_SEED = 42

# ═══════════════════════════════════════════════════════════
# 3. DATA LOADING
# ═══════════════════════════════════════════════════════════

df = pd.read_csv(DATA_PATH)

# ═══════════════════════════════════════════════════════════
# 4. DATA EXPLORATION
# ═══════════════════════════════════════════════════════════

# And so on...
```

### 2. Function Organization

```python
# ✅ GOOD: Single Responsibility Principle

def load_bike_data(filepath):
    """Load bike data from CSV file."""
    return pd.read_csv(filepath)


def clean_bike_data(df):
    """Clean bike data by removing duplicates and handling missing values."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def add_temporal_features(df):
    """Add time-based features like hour, day_of_week, etc."""
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    return df


# Pipeline
df = load_bike_data('data.csv')
df = clean_bike_data(df)
df = add_temporal_features(df)


# ❌ BAD: One function does everything
def process_all_data(filepath):
    df = pd.read_csv(filepath)
    df = df.drop_duplicates()
    df = df.dropna()
    df['hour'] = df['timestamp'].dt.hour
    # ... 50 more lines ...
    return df
```

---

## ✅ Checklist for Clean Code

Before committing your code, check:

### Basic Standards
- [ ] Variables have descriptive names
- [ ] Functions have docstrings
- [ ] Code follows PEP 8 (4 spaces, line length, etc.)
- [ ] Imports are organized (standard, third-party, local)
- [ ] No commented-out code left in final version

### Data Science Specific
- [ ] Random seeds are set for reproducibility
- [ ] Magic numbers are replaced with named constants
- [ ] DataFrames have descriptive names
- [ ] Vectorized operations used instead of loops
- [ ] Model parameters are clearly defined
- [ ] Evaluation metrics are labeled

### Code Quality
- [ ] Functions are small and focused (< 50 lines)
- [ ] Complex logic is commented
- [ ] No duplicate code
- [ ] Error handling for edge cases
- [ ] Code is tested with sample data

---

## 🛠️ Tools to Help

### 1. Linters (Find Issues)

```bash
# Install
pip install pylint flake8

# Run on a file
pylint my_script.py
flake8 my_notebook.ipynb
```

### 2. Formatters (Auto-fix)

```bash
# Install black (automatic code formatter)
pip install black

# Format a file
black my_script.py

# Format all Python files
black .
```

### 3. VS Code Extensions

- **Python** - Official Python extension
- **Pylance** - Fast, feature-rich language support
- **Black Formatter** - Auto-format on save
- **autoDocstring** - Generate docstring templates

---

## 📚 Examples: Before & After

### Example 1: Data Loading

```python
# ❌ BEFORE
def load(f):
    d = pd.read_csv(f)
    d = d.dropna()
    return d

df = load('data.csv')


# ✅ AFTER
def load_and_clean_bike_data(filepath):
    """
    Load bike availability data and remove rows with missing values.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Cleaned bike data
    """
    df = pd.read_csv(filepath)
    df_clean = df.dropna()
    
    print(f"Loaded {len(df)} rows, {len(df_clean)} after cleaning")
    return df_clean

df_bikes = load_and_clean_bike_data('data/raw/bike_data.csv')
```

### Example 2: Feature Engineering

```python
# ❌ BEFORE
df['f1'] = df['timestamp'].dt.hour
df['f2'] = df['timestamp'].dt.dayofweek
df['f3'] = (df['f2'] >= 5).astype(int)


# ✅ AFTER
def create_temporal_features(df):
    """
    Create time-based features from timestamp column.
    
    Features created:
    - hour: Hour of day (0-23)
    - day_of_week: Day of week (0=Monday, 6=Sunday)
    - is_weekend: 1 if weekend, 0 otherwise
    """
    df = df.copy()
    
    # Extract temporal components
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    
    # Create weekend indicator (Saturday=5, Sunday=6)
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
    
    return df

df_with_features = create_temporal_features(df_bikes)
```

---

## 🎓 Learning Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Code Style](https://realpython.com/python-code-quality/)
- [Clean Code in Python](https://github.com/zedr/clean-code-python)

---

**Remember**: Clean code is not about being perfect—it's about being clear, consistent, and considerate of others (including future you)! 🌟
