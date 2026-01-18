# Module 05: Modeling

## 📌 Module Overview
Build, train, and compare machine learning models to predict bike availability.

---

## 🎯 Track Selection: Choose Your Path

**This module continues the track divergence from Module 4. Choose the track you started.**

### Track A: Classification Models (Commuter Prediction)
📁 **Folder:** `track_a_classification/`  
**Goal:** Binary classification - predict bike availability in next 15 minutes  
**Models:** Logistic Regression, Random Forest, XGBoost  
**Metrics:** Precision, Recall, F1-Score, ROC-AUC  
**Notebooks:**
- M5A_01: Baseline models & train/test splits
- M5A_02: Classification algorithms
- M5A_03: Model selection & hyperparameter tuning

→ [Go to Track A README](./track_a_classification/README.md)

### Track B: Regression & Time Series (Multi-Day Prediction)
📁 **Folder:** `track_b_regression/`  
**Goal:** Regression + forecasting - predict number of bikes over 24-72 hours  
**Models:** Linear/Ridge, Random Forest, ARIMA, Prophet  
**Metrics:** RMSE, MAE, MAPE, R², Forecast Accuracy  
**Notebooks:**
- M5B_01: Regression models
- M5B_02: Time series models (ARIMA, Prophet)
- M5B_03: Uncertainty quantification

→ [Go to Track B README](./track_b_regression/README.md)

### Track Comparison

| Aspect | Track A (Classification) | Track B (Regression/Time Series) |
|--------|--------------------------|----------------------------------|
| **Problem Type** | Binary Classification | Regression + Forecasting |
| **Target** | Available/Not Available | Number of bikes (0-20+) |
| **Algorithms** | Logistic, RF, XGBoost | Linear, RF, ARIMA, Prophet |
| **Evaluation** | Precision, Recall, F1 | RMSE, MAE, MAPE |
| **Complexity** | Moderate | High |
| **Time Commitment** | 4-5 hours | 6-7 hours |
| **Prerequisites** | Module 4 Track A | Module 4 Track B |
| **Key Challenge** | Class imbalance | Time series validation |

### Still Deciding?
You should have chosen your track in Module 3. If you're switching tracks:
- Review [Use Case Comparison Guide](../../docs/guides/use_case_comparison.md)
- Check [Learning Pathways Guide](../../docs/guides/learning_pathways.md)
- Complete corresponding Module 4 track first

---

## ⚠️ Critical Domain Insight for Course Developers

**OV-fiets System Characteristics:**
- **No docking system**: `docks_available` field is always 0
- **Same-station returns**: Bikes must return to origin station
- **After-hours flexibility**: Bikes can be left outside without docking

**Impact on Module 5 Modeling:**
- ❌ **INVALID target variables**:
  - Cannot predict "dock availability"
  - Cannot model dock-to-bike ratios
  - Cannot predict rebalancing needs between stations

- ✅ **VALID target variables**:
  - `bikes_available` at specific stations (primary target)
  - `bikes_available` at future time points (time-series)
  - `station_empty_probability` (binary classification)

- ✅ **Key modeling constraints**:
  - Predictions must respect: `0 ≤ bikes_available ≤ station_capacity`
  - Consider same-station return flow (bikes don't transfer between stations)
  - Model station-specific patterns (each station is independent)
  - Account for after-hours behavior (bikes outside without docking)

- ✅ **Feature selection validation**:
  - Ensure no dock-related features in final model
  - Validate that model doesn't assume dock-based operations

**Reference:** See M2_01 SOLUTIONS notebook, Task 8.1 for full explanation.

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 5 introduces **machine learning modeling** with careful scaffolding for new ML practitioners.

**Scaffolding Strategy:**
- **Initial**: 65% complete - Learn model training workflows
- **Progressive**: 65% → 25% as confidence builds
- **Goal**: Train models independently, compare effectively, select best approach
- **Approach**: Baseline → Simple models → Complex models → Model selection

**Progressive Difficulty (Each Notebook):**
- Part 1: Model Setup (85% complete)
- Part 2: Basic Training (60%)
- Part 3: Hyperparameter Tuning (45%)
- Part 4: Model Comparison (30%)
- Part 5: Advanced Techniques (15% + optional)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` with multiple approaches
- Different hyperparameter strategies shown
- Model interpretation examples

**Optional Challenges:**
- Ensemble methods
- Custom model architectures
- Advanced cross-validation strategies

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Split data into train/validation/test sets (time-series aware)
- Build and evaluate baseline models
- Train multiple ML algorithms appropriate for your use case
- Compare model performance using relevant metrics
- Select and save the best model for deployment

## ✅ Your Tasks

**Choose your track and complete the notebooks in that folder:**

### Track A: Classification (`track_a_classification/`)
1. **M5A_01_baseline_models.ipynb**
   - Create time-series aware train/val/test splits
   - Build baseline models (majority class, historical rates)
   - Define evaluation metrics (precision, recall, F1, ROC-AUC)
   - Establish performance benchmarks

2. **M5A_02_classification_models.ipynb**
   - Train Logistic Regression (baseline ML model)
   - Train Random Forest Classifier (non-linear patterns)
   - Train XGBoost Classifier (gradient boosting)
   - Handle class imbalance (class weights, SMOTE)
   - Compare models on validation set

3. **M5A_03_model_selection.ipynb**
   - Hyperparameter optimization (GridSearchCV)
   - Cross-validation strategies (time-series aware)
   - Feature importance analysis
   - Model interpretation with SHAP
   - Select final model and evaluate on test set
   - Save model with joblib

### Track B: Regression & Time Series (`track_b_regression/`)
1. **M5B_01_regression_models.ipynb**
   - Create time-series aware train/val/test splits
   - Train Linear/Ridge/Lasso Regression
   - Train Random Forest Regressor
   - Train XGBoost Regressor
   - Compare RMSE, MAE, MAPE, R²
   - Feature importance analysis

2. **M5B_02_time_series_models.ipynb**
   - Build ARIMA/SARIMA models (univariate forecasting)
   - Train Prophet with holidays and events
   - Multi-step ahead predictions (24h, 48h, 72h)
   - Seasonality and trend decomposition
   - Forecast accuracy evaluation

3. **M5B_03_uncertainty_quantification.ipynb**
   - Build prediction intervals (95% confidence)
   - Quantile regression (10th, 50th, 90th percentiles)
   - Ensemble methods for uncertainty
   - Probabilistic forecasting with Prophet
   - Visualize uncertainty bands
   - Communicate forecast ranges

## 📝 Naming Convention
- **Track A**: `M5A_{number}_{description}.ipynb` (classification notebooks)
- **Track B**: `M5B_{number}_{description}.ipynb` (regression/time series notebooks)

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/modeling.py` for model training functions
- Check [code snippets](../../docs/references/code_snippets.md) for model training examples
- Always evaluate on held-out test data
- Use cross-validation for robust estimates
- Track hyperparameters for reproducibility
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `scikit-learn` - ML algorithms
- `xgboost` - Gradient boosting
- `numpy` / `pandas` - Data handling

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - Model training examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices
- 🧪 [Experiment Best Practices](../../docs/best_practices/experiment_best_practices.md) - MLflow tracking
- 📋 [Model Documentation](../../docs/best_practices/model_documentation_guidelines.md) - Document models

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

**Track A Checklist:**
- [ ] Time-series aware train/val/test splits created
- [ ] Baseline models established (majority class, historical rates)
- [ ] Classification models trained (Logistic, RF, XGBoost)
- [ ] Class imbalance handled appropriately
- [ ] Models compared on precision, recall, F1-score
- [ ] Hyperparameters tuned with cross-validation
- [ ] Final model selected and saved

**Track B Checklist:**
- [ ] Time-series aware train/val/test splits created
- [ ] Regression models trained (Linear, RF, XGBoost)
- [ ] Time series models built (ARIMA, Prophet)
- [ ] Multi-horizon forecasts evaluated (24h, 48h, 72h)
- [ ] Uncertainty quantification implemented
- [ ] Models compared on RMSE, MAE, MAPE
- [ ] Final model(s) selected and saved with uncertainty bounds

---
**Next Module:** Module 06 - Validation & Governance  
- **Track A:** Classification model validation, confusion matrices
- **Track B:** Time series validation, backtesting, forecast evaluation
