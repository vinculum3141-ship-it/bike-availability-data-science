# 🧪 Experiment Best Practices

This guide covers best practices for running and tracking machine learning experiments.

---

## 🎯 Why Track Experiments?

**Reproducibility**: Recreate results months later
**Comparison**: Compare different approaches systematically  
**Learning**: Understand what works and what doesn't  
**Collaboration**: Share findings with teammates  
**Production**: Transition best models to production smoothly

---

## 📝 What to Track

### Always Track
- **Code version**: Git commit hash
- **Data version**: Dataset version or hash
- **Hyperparameters**: All model parameters
- **Metrics**: Train, validation, and test performance
- **Training time**: Duration and resources used
- **Random seeds**: For reproducibility
- **Environment**: Package versions

### Also Consider
- Feature sets used
- Data preprocessing steps
- Cross-validation folds
- Model artifacts (weights, checkpoints)
- Predictions on validation/test sets
- Feature importance
- Error analysis results

---

## 🛠️ Tools for Experiment Tracking

### MLflow (Recommended)
```python
import mlflow
import mlflow.sklearn

# Start experiment
mlflow.set_experiment("bike_availability_prediction")

with mlflow.start_run(run_name="random_forest_v1"):
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("random_state", 42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Log metrics
    train_score = model.score(X_train, y_train)
    val_score = model.score(X_val, y_val)
    mlflow.log_metric("train_r2", train_score)
    mlflow.log_metric("val_r2", val_score)
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Log artifacts
    mlflow.log_artifact("feature_importance.png")
```

### Weights & Biases (Alternative)
- More advanced visualization
- Team collaboration features
- Cloud-based tracking

### Simple CSV Tracking
For basic needs:
```python
import pandas as pd
from datetime import datetime

results = {
    'timestamp': datetime.now(),
    'model': 'RandomForest',
    'n_estimators': 100,
    'max_depth': 10,
    'train_r2': 0.85,
    'val_r2': 0.78,
    'test_r2': 0.76
}

# Append to CSV
df = pd.DataFrame([results])
df.to_csv('experiments.csv', mode='a', header=False, index=False)
```

---

## 🔄 Experiment Workflow

### 1. Plan
- Define hypothesis: "Adding weather lag features will improve predictions"
- Set success criteria: "Achieve R² > 0.75 on validation set"
- Document approach

### 2. Setup
```python
# Set random seed for reproducibility
import numpy as np
import random

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Log git commit
import subprocess
git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
```

### 3. Experiment
- Start with simple baseline
- Change ONE thing at a time
- Document observations
- Save intermediate results

### 4. Analyze
- Compare to baseline
- Understand why it worked/failed
- Document insights

### 5. Iterate
- Build on successful experiments
- Learn from failures
- Gradually increase complexity

---

## 📊 Naming Conventions

### Experiment Names
Use descriptive, hierarchical names:
```
bike_availability/
├── baseline/
│   ├── mean_predictor
│   └── linear_regression
├── random_forest/
│   ├── default_params
│   ├── tuned_depth
│   └── feature_selection
└── xgboost/
    ├── default_params
    └── optimized
```

### Run Names
Include key information:
```
rf_100trees_depth10_weather_features_v2
xgb_lr0.1_depth5_allfeatures_v1
```

---

## 🎛️ Hyperparameter Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=5,
    scoring='r2',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

# Log all results
for i, params in enumerate(grid_search.cv_results_['params']):
    with mlflow.start_run(run_name=f"grid_search_{i}"):
        for param, value in params.items():
            mlflow.log_param(param, value)
        mlflow.log_metric("mean_cv_score", grid_search.cv_results_['mean_test_score'][i])
```

### Random Search
More efficient for large parameter spaces:
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(5, 20),
    'min_samples_split': randint(2, 20),
    'learning_rate': uniform(0.01, 0.3)  # For gradient boosting
}

random_search = RandomizedSearchCV(
    estimator,
    param_distributions,
    n_iter=50,
    cv=5,
    random_state=42,
    n_jobs=-1
)
```

---

## 📈 Metrics to Track

### Regression Metrics
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def calculate_metrics(y_true, y_pred):
    return {
        'mae': mean_absolute_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'r2': r2_score(y_true, y_pred),
        'mape': np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    }
```

### Business Metrics
- Prediction accuracy at peak hours
- Error rates for stations with high demand
- Computational cost (inference time)
- Model size

---

## ⚠️ Common Pitfalls

### 1. Data Leakage
❌ Using future information in features  
✅ Respect temporal ordering

### 2. Overfitting to Validation Set
❌ Tuning hyperparameters based on test set  
✅ Use separate validation set for tuning

### 3. Not Setting Random Seeds
❌ Non-reproducible results  
✅ Set seeds for Python, NumPy, and ML libraries

### 4. Changing Multiple Things
❌ Can't isolate what caused improvement  
✅ Change one variable at a time

### 5. Not Documenting Failures
❌ Lose valuable learning  
✅ Document what didn't work and why

---

## 📝 Experiment Documentation Template

```markdown
## Experiment: [Name]

**Date**: 2024-01-15  
**Author**: [Your Name]  
**Git Commit**: abc123

### Hypothesis
Adding weather lag features (1hr, 3hr, 6hr) will improve prediction accuracy.

### Approach
- Added 3 new lag features for temperature and precipitation
- Used RandomForest with 100 trees
- 5-fold time-series cross-validation

### Results
- Baseline R²: 0.72
- New Model R²: 0.78 (+0.06 improvement)
- Training time: 45 seconds
- Feature importance: weather_lag_3hr was most important

### Insights
- Weather lags significantly improve predictions
- 3-hour lag more useful than 1-hour or 6-hour
- Model especially improves during weather transitions

### Next Steps
- Try 24-hour weather lags
- Add weather forecast features
- Test with XGBoost

### Files
- Notebook: `notebooks/experiments/exp_005_weather_lags.ipynb`
- Model: `models/rf_weather_lags_v1.pkl`
```

---

## 🎯 Checklist: Before Running an Experiment

- [ ] Clear hypothesis defined
- [ ] Baseline for comparison exists
- [ ] Random seeds are set
- [ ] Git repository is clean (no uncommitted changes)
- [ ] Logging is configured
- [ ] Success criteria are defined
- [ ] Data splits are prepared
- [ ] Environment is documented

---

## 🚀 Advanced Topics

### A/B Testing
For production models:
```python
# Route 10% traffic to new model
if random.random() < 0.1:
    prediction = new_model.predict(features)
    mlflow.log_metric("model_version", "v2")
else:
    prediction = current_model.predict(features)
    mlflow.log_metric("model_version", "v1")
```

### Model Monitoring
Track in production:
- Prediction distribution drift
- Feature distribution drift
- Prediction latency
- Error rates over time

---

## 📚 Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Weights & Biases Tutorials](https://docs.wandb.ai/)
- [Experiment Tracking Best Practices](https://neptune.ai/blog/ml-experiment-tracking)

---

**Remember**: Good experiment tracking is an investment that pays dividends in reproducibility and team collaboration! 🎯
