# Module 05: Modeling

## 📌 Module Overview
Build, train, and compare machine learning models to predict bike availability.

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
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/modeling.py` for model training functions
- Check [code snippets](../../docs/code_snippets.md) for model training examples
- Always evaluate on held-out test data
- Use cross-validation for robust estimates
- Track hyperparameters for reproducibility
- Follow [coding standards](../../docs/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `scikit-learn` - ML algorithms
- `xgboost` - Gradient boosting
- `numpy` / `pandas` - Data handling

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📚 [Code Snippets](../../docs/code_snippets.md) - Model training examples
- 📐 [Coding Standards](../../docs/coding_standards.md) - Best practices
- 🧪 [Experiment Best Practices](../../docs/experiment_best_practices.md) - MLflow tracking
- 📋 [Model Documentation](../../docs/model_documentation_guidelines.md) - Document models

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
