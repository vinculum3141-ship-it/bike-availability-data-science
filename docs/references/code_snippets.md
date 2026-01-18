# 📚 Code Snippets Reference

Quick reference guide for common data science tasks. Copy and adapt these snippets for your projects.

---

## 📥 Data Loading

### Load CSV File

```python
import pandas as pd

# Basic loading
df = pd.read_csv('data/raw/bike_data.csv')

# With specific options
df = pd.read_csv(
    'data/raw/bike_data.csv',
    parse_dates=['timestamp'],  # Parse date columns
    index_col='timestamp',       # Set index
    na_values=['NA', 'missing'], # Custom missing values
    dtype={'station_id': str}    # Specify data types
)
```

### Load Multiple CSV Files

```python
import pandas as pd
from glob import glob

# Load all CSV files in a directory
csv_files = glob('data/raw/*.csv')
df_list = [pd.read_csv(f) for f in csv_files]
df = pd.concat(df_list, ignore_index=True)

print(f"Loaded {len(csv_files)} files, {len(df)} total rows")
```

### Load from API

```python
import requests
import pandas as pd

def fetch_bike_data(station_id, api_key):
    """Fetch bike availability data from API."""
    url = f"https://api.example.com/bikes/{station_id}"
    headers = {'Authorization': f'Bearer {api_key}'}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error for bad status
    
    data = response.json()
    df = pd.DataFrame(data['results'])
    return df

# Usage
df = fetch_bike_data('STATION_001', api_key='your_key_here')
```

---

## 🧹 Data Cleaning

### Handle Missing Values

```python
# Check missing values
print(df.isnull().sum())
print(df.isnull().sum() / len(df) * 100)  # Percentage

# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows where specific column is missing
df_clean = df.dropna(subset=['bikes_available'])

# Fill missing values
df['temperature'].fillna(df['temperature'].mean(), inplace=True)  # Mean
df['temperature'].fillna(method='ffill', inplace=True)  # Forward fill
df['temperature'].fillna(method='bfill', inplace=True)  # Backward fill

# Interpolate missing values (for time series)
df['temperature'] = df['temperature'].interpolate(method='linear')
```

### Remove Duplicates

```python
# Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# Remove duplicates
df_clean = df.drop_duplicates()

# Remove duplicates based on specific columns
df_clean = df.drop_duplicates(subset=['timestamp', 'station_id'], keep='first')
```

### Handle Outliers

```python
import numpy as np

# Method 1: Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(df['bikes_available']))
df_no_outliers = df[z_scores < 3]

# Method 2: IQR (Interquartile Range)
Q1 = df['bikes_available'].quantile(0.25)
Q3 = df['bikes_available'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_no_outliers = df[
    (df['bikes_available'] >= lower_bound) & 
    (df['bikes_available'] <= upper_bound)
]

# Method 3: Percentile-based
lower = df['bikes_available'].quantile(0.01)
upper = df['bikes_available'].quantile(0.99)
df_no_outliers = df[
    (df['bikes_available'] >= lower) & 
    (df['bikes_available'] <= upper)
]
```

---

## 🔧 Feature Engineering

### Temporal Features

```python
# Extract datetime components
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute
df['day_of_week'] = df['timestamp'].dt.dayofweek  # Monday=0, Sunday=6
df['day_name'] = df['timestamp'].dt.day_name()
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Create cyclical features (for hour, day, month)
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)

# Time-based flags
df['is_morning_peak'] = df['hour'].isin([7, 8, 9]).astype(int)
df['is_evening_peak'] = df['hour'].isin([17, 18, 19]).astype(int)
df['is_business_hours'] = df['hour'].between(9, 17).astype(int)
```

### Lag Features

```python
# Create lag features (previous values)
df['bikes_lag_1h'] = df.groupby('station_id')['bikes_available'].shift(1)
df['bikes_lag_3h'] = df.groupby('station_id')['bikes_available'].shift(3)
df['bikes_lag_24h'] = df.groupby('station_id')['bikes_available'].shift(24)

# Difference features
df['bikes_diff_1h'] = df.groupby('station_id')['bikes_available'].diff(1)
```

### Rolling Features

```python
# Rolling mean (moving average)
df['bikes_rolling_mean_3h'] = (
    df.groupby('station_id')['bikes_available']
    .rolling(window=3, min_periods=1)
    .mean()
    .reset_index(0, drop=True)
)

# Rolling standard deviation
df['bikes_rolling_std_24h'] = (
    df.groupby('station_id')['bikes_available']
    .rolling(window=24, min_periods=1)
    .std()
    .reset_index(0, drop=True)
)

# Rolling min/max
df['bikes_rolling_min_6h'] = (
    df.groupby('station_id')['bikes_available']
    .rolling(window=6, min_periods=1)
    .min()
    .reset_index(0, drop=True)
)
```

### Categorical Encoding

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding (for ordinal data)
le = LabelEncoder()
df['weather_encoded'] = le.fit_transform(df['weather_condition'])

# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['station_id', 'weather_condition'])

# Or using sklearn
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False, drop='first')
encoded = encoder.fit_transform(df[['station_id']])
encoded_df = pd.DataFrame(
    encoded, 
    columns=encoder.get_feature_names_out(['station_id'])
)
```

### Feature Scaling

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standardization (mean=0, std=1)
scaler = StandardScaler()
df[['temperature', 'humidity']] = scaler.fit_transform(
    df[['temperature', 'humidity']]
)

# Min-Max Scaling (scale to 0-1)
scaler = MinMaxScaler()
df[['temperature', 'humidity']] = scaler.fit_transform(
    df[['temperature', 'humidity']]
)

# Important: Save scaler for test data
import pickle
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
```

---

## 📊 Data Exploration

### Summary Statistics

```python
# Basic statistics
print(df.describe())

# Statistics for specific columns
print(df[['bikes_available', 'temperature']].describe())

# Statistics by group
print(df.groupby('station_id')['bikes_available'].describe())

# Custom aggregations
summary = df.groupby('station_id').agg({
    'bikes_available': ['mean', 'std', 'min', 'max'],
    'temperature': ['mean', 'std']
})
print(summary)
```

### Value Counts

```python
# Count unique values
print(df['station_id'].value_counts())

# With percentages
print(df['station_id'].value_counts(normalize=True) * 100)

# Top N values
print(df['station_id'].value_counts().head(10))
```

### Correlation Analysis

```python
# Correlation matrix
correlation = df[['bikes_available', 'temperature', 'humidity']].corr()
print(correlation)

# Find highly correlated features
threshold = 0.7
high_corr = correlation[correlation.abs() > threshold]
print(high_corr)
```

---

## 📈 Visualization

### Line Plot

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['bikes_available'])
plt.xlabel('Time')
plt.ylabel('Bikes Available')
plt.title('Bike Availability Over Time')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Histogram

```python
plt.figure(figsize=(10, 6))
plt.hist(df['bikes_available'], bins=30, edgecolor='black', alpha=0.7)
plt.axvline(df['bikes_available'].mean(), color='red', linestyle='--', 
            label=f'Mean: {df["bikes_available"].mean():.1f}')
plt.xlabel('Bikes Available')
plt.ylabel('Frequency')
plt.title('Distribution of Bike Availability')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Box Plot

```python
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='station_id', y='bikes_available')
plt.xticks(rotation=45)
plt.title('Bike Availability by Station')
plt.tight_layout()
plt.show()
```

### Heatmap

```python
import seaborn as sns

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation = df[['bikes_available', 'temperature', 'humidity', 'hour']].corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True)
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.show()
```

### Scatter Plot

```python
plt.figure(figsize=(10, 6))
plt.scatter(df['temperature'], df['bikes_available'], alpha=0.5)
plt.xlabel('Temperature (°C)')
plt.ylabel('Bikes Available')
plt.title('Bike Availability vs Temperature')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 🤖 Machine Learning

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

# Simple split
X = df[['temperature', 'hour', 'day_of_week']]
y = df['bikes_available']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Time series split (chronological)
train_size = int(len(df) * 0.8)
df_train = df[:train_size]
df_test = df[train_size:]
```

### Train Model

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Initialize and train
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.3f}")
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(
    model, X_train, y_train, 
    cv=5, 
    scoring='neg_mean_absolute_error'
)

print(f"CV MAE: {-scores.mean():.2f} (+/- {scores.std():.2f})")
```

### Feature Importance

```python
# Get feature importance
importances = model.feature_importances_
feature_names = X_train.columns

# Create DataFrame
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

print(importance_df)

# Plot
plt.figure(figsize=(10, 6))
plt.barh(importance_df['feature'], importance_df['importance'])
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
```

### Save and Load Model

```python
import pickle

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load model
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Use loaded model
predictions = loaded_model.predict(X_test)
```

---

## 💾 Data Export

### Save to CSV

```python
# Save DataFrame
df.to_csv('data/processed/bike_data_processed.csv', index=False)

# Save specific columns
df[['timestamp', 'bikes_available']].to_csv('output.csv', index=False)

# Save with custom options
df.to_csv(
    'output.csv',
    index=False,
    sep=';',              # Custom separator
    encoding='utf-8',     # Encoding
    float_format='%.2f'   # Float precision
)
```

### Save to Parquet (Recommended for large files)

```python
# Save (smaller file size, faster loading)
df.to_parquet('data/processed/bike_data.parquet', index=False)

# Load
df = pd.read_parquet('data/processed/bike_data.parquet')
```

---

## 🔍 Useful Pandas Operations

### Filter Data

```python
# Simple filter
df_filtered = df[df['bikes_available'] > 10]

# Multiple conditions
df_filtered = df[
    (df['bikes_available'] > 10) & 
    (df['temperature'] > 15)
]

# Filter by list
stations = ['STATION_001', 'STATION_002']
df_filtered = df[df['station_id'].isin(stations)]

# Filter by date range
df_filtered = df[
    (df['timestamp'] >= '2024-01-01') & 
    (df['timestamp'] <= '2024-01-31')
]
```

### Group By Operations

```python
# Group by single column
grouped = df.groupby('station_id')['bikes_available'].mean()

# Group by multiple columns
grouped = df.groupby(['station_id', 'hour'])['bikes_available'].mean()

# Multiple aggregations
summary = df.groupby('station_id').agg({
    'bikes_available': ['mean', 'std', 'min', 'max'],
    'temperature': 'mean'
})

# Custom aggregation function
def range_func(x):
    return x.max() - x.min()

df.groupby('station_id')['bikes_available'].agg(range_func)
```

### Merge DataFrames

```python
# Inner join (default)
df_merged = pd.merge(df_bikes, df_weather, on='timestamp', how='inner')

# Left join
df_merged = pd.merge(df_bikes, df_weather, on='timestamp', how='left')

# Merge on multiple columns
df_merged = pd.merge(
    df_bikes, df_weather, 
    on=['timestamp', 'station_id'],
    how='inner'
)

# Merge with different column names
df_merged = pd.merge(
    df_bikes, df_weather,
    left_on='time', right_on='timestamp',
    how='inner'
)
```

---

## 🎯 Quick Tips

### Set Display Options

```python
import pandas as pd

# Show all columns
pd.set_option('display.max_columns', None)

# Show more rows
pd.set_option('display.max_rows', 100)

# Show full column content
pd.set_option('display.max_colwidth', None)

# Precision for floats
pd.set_option('display.precision', 2)
```

### Progress Bar for Loops

```python
from tqdm import tqdm

# For loops
for i in tqdm(range(100)):
    # Your code here
    pass

# For pandas apply
tqdm.pandas()
df['new_column'] = df['old_column'].progress_apply(some_function)
```

### Memory Optimization

```python
# Check memory usage
print(df.memory_usage(deep=True))

# Optimize dtypes
df['station_id'] = df['station_id'].astype('category')
df['bikes_available'] = df['bikes_available'].astype('int8')  # if values < 128

# Read CSV with optimized dtypes
df = pd.read_csv(
    'data.csv',
    dtype={'station_id': 'category', 'bikes_available': 'int8'}
)
```

---

## 📚 Resources

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Scikit-learn Cheat Sheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

---

**Pro Tip**: Bookmark this page and use Ctrl+F to quickly find the snippet you need! 🔖
