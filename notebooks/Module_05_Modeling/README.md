# Module 05: Modeling

## 📌 Module Overview
Build, train, and compare machine learning models to predict bike availability.

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Split data into train/validation/test sets
- Build baseline models
- Train multiple ML algorithms
- Compare model performance
- Select the best model

## ✅ Your Tasks
Create the following notebooks in this folder:

### M5_01_train_test_split.ipynb
- Create train/validation/test splits
- Handle temporal ordering (no future data leakage)
- Ensure representative splits
- Document split strategy

### M5_02_baseline_models.ipynb
- Create naive baseline (mean, median)
- Build simple linear regression
- Establish performance benchmarks
- Document baseline results

### M5_03_tree_models.ipynb
- Train Decision Tree
- Train Random Forest
- Train Gradient Boosting (XGBoost)
- Compare tree-based models

### M5_04_model_comparison.ipynb
- Compare all models
- Analyze performance metrics (MAE, RMSE, R²)
- Plot predictions vs actual
- Select best performing model

## 📝 Naming Convention
Follow this pattern: `M5_{number}_{description}.ipynb`

## 💡 Tips
- Use `src/modeling.py` for model training functions
- Always evaluate on held-out test data
- Use cross-validation for robust estimates
- Track hyperparameters for reproducibility

## 📚 Key Libraries
- `scikit-learn` - ML algorithms
- `xgboost` - Gradient boosting
- `numpy` / `pandas` - Data handling

## ⚠️ Important
- Respect temporal ordering in time series data
- Never train on test data (data leakage!)
- Use same preprocessing for all datasets
- Document all modeling decisions

## 📊 Evaluation Metrics
For regression tasks, consider:
- MAE (Mean Absolute Error) - easy to interpret
- RMSE (Root Mean Squared Error) - penalizes large errors
- R² (R-squared) - proportion of variance explained
- MAPE (Mean Absolute Percentage Error) - relative error

## ✨ Checkpoint
Before moving to Module 06, ensure:
- [ ] You have train/validation/test splits
- [ ] Baseline model is established
- [ ] Multiple ML models are trained
- [ ] Model performances are compared
- [ ] Best model is selected and saved

---
**Next Module:** Module 06 - Validation & Governance
