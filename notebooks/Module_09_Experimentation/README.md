# Module 09: Experimentation & Tracking

## 📌 Module Overview
Learn to track experiments, compare models systematically, and manage ML lifecycle.

---

## 🎯 Track-Aware Experiment Tracking

**Metrics and experiment design differ by model type.**

### Experiment Tracking Differences

| Aspect | Track A (Classification) | Track B (Time Series) |
|--------|-------------------------|----------------------|
| **MLflow Metrics** | Precision, recall, F1, ROC-AUC | RMSE, MAE, MAPE, R² |
| **Key Parameters** | Class weights, threshold, C/max_depth | Lag order, seasonality, alpha |
| **Artifacts** | Model pickle, confusion matrix | Model pickle, forecast plots |
| **Comparison Focus** | Recall optimization | Multi-horizon accuracy |
| **A/B Testing** | Prediction accuracy vs baseline | Forecast RMSE improvement |
| **Retraining Triggers** | F1 drop below threshold | RMSE increase >10% |

### Common Experiment Tasks (Both Tracks)
- MLflow tracking setup
- Hyperparameter optimization
- Model versioning
- Experiment comparison
- Best model selection

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 9 teaches **experiment tracking and MLOps** - professional ML workflows.

**Scaffolding Strategy:**
- **Initial**: 65% complete - Learn MLflow and experiment tracking
- **Progressive**: 65% → 25% for strategic thinking
- **Goal**: Design experiments, track systematically, make data-driven decisions
- **Approach**: Tools → Tracking → Comparison → Experiment design

**Progressive Difficulty (Each Notebook):**
- Part 1: MLflow Basics (75% complete)
- Part 2: Experiment Tracking (55%)
- Part 3: Model Registry (40%)
- Part 4: A/B Testing (30%)
- Part 5: Experiment Strategy (20% + design challenges)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` with tracking patterns
- Multiple experiment designs
- Statistical testing examples

**Optional Challenges:**
- Multi-armed bandits
- Bayesian optimization
- Advanced experiment designs

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Track experiments with MLflow
- Compare model versions
- Manage hyperparameters
- Implement A/B testing concepts
- Follow experiment best practices

## ✅ Your Tasks

**Complete these notebooks - examples provided for both tracks:**

### M9_01_mlflow_setup.ipynb
**Track A: Log classification experiments**
- Track precision, recall, F1, ROC-AUC
- Log class weights and threshold
- Save confusion matrices
- Track false negative rate

**Track B: Log forecasting experiments**
- Track RMSE, MAE, MAPE by horizon
- Log ARIMA orders, Prophet parameters
- Save forecast plots with uncertainty
- Track seasonal decomposition

**Both tracks:**
- MLflow server setup
- Experiment organization
- Model artifact management

### M9_02_hyperparameter_tuning.ipynb
**Track A: Tune classification models**
- XGBoost: max_depth, learning_rate, scale_pos_weight
- Random Forest: n_estimators, max_features
- Optimize for recall (minimize false negatives)

**Track B: Tune forecasting models**
- ARIMA: (p,d,q) orders, seasonal parameters
- Prophet: changepoint_prior_scale, seasonality_prior_scale
- XGBoost: lag features, window sizes
- Optimize for multi-horizon RMSE

**Both tracks:**
- Grid/Random search with MLflow
- Cross-validation strategies
- Best model selection

### M9_03_model_versioning.ipynb
- Version control models
- Compare model versions
- Track model lineage
- Manage model registry

### M9_04_experiment_comparison.ipynb
- Compare multiple experiments
- Visualize experiment results
- Analyze trade-offs
- Document best practices

## 📝 Naming Convention
Follow this pattern: `M9_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Check [experiment best practices](../../docs/best_practices/experiment_best_practices.md) for MLflow guidelines
- Reference [code snippets](../../docs/references/code_snippets.md) for MLflow examples
- Track everything: code, data, parameters, metrics
- Use meaningful experiment names
- Document experiment rationale
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `mlflow` - Experiment tracking
- `scikit-learn` - Hyperparameter tuning
- `optuna` (optional) - Advanced optimization

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 🧪 [Experiment Best Practices](../../docs/best_practices/experiment_best_practices.md) - MLflow guide
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - MLflow examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices
- 📋 [Model Documentation](../../docs/best_practices/model_documentation_guidelines.md) - Document experiments

## 🧪 Experiment Tracking Checklist
- [ ] Parameters logged
- [ ] Metrics tracked
- [ ] Model artifacts saved
- [ ] Data version recorded
- [ ] Code version tagged
- [ ] Results documented

## ✨ Checkpoint
Before moving to Module 10, ensure:
- [ ] MLflow is set up and working
- [ ] Experiments are tracked systematically
- [ ] Hyperparameters are optimized
- [ ] Model versions are managed
- [ ] Best practices are documented

---
**Next Module:** Module 10 - Collaboration
