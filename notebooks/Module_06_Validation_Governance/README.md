# Module 06: Validation & Governance

## 📌 Module Overview
Validate model performance, ensure fairness, and establish governance practices for production deployment.

---

## 🎯 Track-Aware Validation

**Both tracks converge in Modules 6-10, but validation approaches differ by model type.**

### Validation Differences by Track

| Aspect | Track A (Classification) | Track B (Regression/Time Series) |
|--------|-------------------------|----------------------------------|
| **Primary Metrics** | Confusion matrix, precision, recall, F1 | RMSE, MAE, residual plots |
| **Cross-Validation** | Stratified K-fold (class balance) | Time-series CV (rolling window) |
| **Error Analysis** | False positives/negatives analysis | Residual analysis, forecast errors |
| **Threshold Tuning** | ROC curve, precision-recall tradeoff | N/A (continuous predictions) |
| **Key Risks** | Class imbalance bias | Overfitting to trends, data leakage |
| **Business Validation** | "How often do we mislead commuters?" | "How accurate are our forecasts?" |

### Common Validation Tasks (Both Tracks)
- Test set evaluation (final performance)
- Feature importance validation
- Model assumptions checking
- Edge case analysis
- Documentation and model cards
- Governance framework

---

## ⚠️ Critical Domain Insight for Course Developers

**OV-fiets System Characteristics:**
- **No docking system**: `docks_available` field is always 0
- **Same-station returns**: Bikes must return to origin station
- **After-hours flexibility**: Bikes can be left outside without docking

**Impact on Module 6 Validation & Governance:**
- ✅ **Validation checks to include**:
  - Verify no dock-related features used in model
  - Confirm predictions respect: `0 ≤ bikes_available ≤ station_capacity`
  - Validate same-station return constraint assumptions
  - Check model doesn't predict cross-station transfers

- ✅ **Business rule validation**:
  - `bikes_available` must be integer values
  - Station capacity constraints must hold
  - After-hours patterns should be documented
  - System limitations (no docking) must be in model cards

- ✅ **Documentation requirements**:
  - Explicitly state: "Model designed for OV-fiets (no-dock system)"
  - Document why dock-based approaches don't apply
  - Note transferability limitations to dock-based systems (Citi Bike, Vélib, etc.)
  - Include system-specific assumptions in model governance docs

- ✅ **Error analysis considerations**:
  - Errors during after-hours periods (unique behavior)
  - Station-specific capacity mismatches
  - Misaligned with dock-based benchmark models (expected!)

**Reference:** See M2_01 SOLUTIONS notebook, Task 8.1 for full explanation.

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 6 teaches **validation and governance** - critical for production ML.

**Scaffolding Strategy:**
- **Initial**: 70% complete - Learn validation frameworks
- **Progressive**: 70% → 30% emphasizing critical thinking
- **Goal**: Design validation strategies, document thoroughly, ensure reproducibility
- **Approach**: Standards → Apply → Design custom validation → Document

**Progressive Difficulty (Each Notebook):**
- Part 1: Validation Concepts (85% complete)
- Part 2: Implement Validation (60%)
- Part 3: Edge Cases (40%)
- Part 4: Documentation (30%)
- Part 5: Governance Framework (20% + organizational design)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` with industry standards
- Multiple documentation templates
- Validation strategy examples

**Optional Challenges:**
- Automated validation pipelines
- Custom monitoring dashboards
- Production deployment checklists

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Validate models on test data using appropriate metrics for your problem type
- Perform error analysis (confusion matrices for classification, residual plots for regression)
- Check model assumptions and identify violations
- Document model limitations and system constraints
- Establish model governance practices for production

## ✅ Your Tasks

**Complete these notebooks - examples provided for both tracks:**

### M6_01_test_evaluation.ipynb
**Track A examples:**
- Evaluate classification model on test set
- Generate confusion matrix and classification report
- Analyze false positives and false negatives
- Calculate precision, recall, F1-score, ROC-AUC
- Threshold tuning for business requirements

**Track B examples:**
- Evaluate regression/time series models on test set
- Calculate RMSE, MAE, MAPE for different horizons
- Plot actual vs predicted values
- Analyze residuals (patterns, heteroscedasticity)
- Multi-step forecast evaluation (24h, 48h, 72h)

### M6_02_error_analysis.ipynb
**Track A examples:**
- Identify misclassification patterns (which stations? which times?)
- Analyze false negative cases (predicted available but empty)
- Analyze false positive cases (predicted unavailable but bikes present)
- Rush hour performance vs off-peak
- Weather impact on prediction errors

**Track B examples:**
- Identify large forecast errors (which stations? which periods?)
- Analyze systematic biases (over/under-prediction)
- Seasonal error patterns
- Event-driven anomalies
- Uncertainty calibration (are prediction intervals accurate?)

### M6_03_model_assumptions.ipynb
**Track A examples:**
- Check class balance assumptions
- Validate feature independence (multicollinearity)
- Examine prediction calibration (predicted probabilities vs actual rates)
- Test model on different time periods

**Track B examples:**
- Check stationarity assumptions (for ARIMA)
- Validate residual normality
- Test for autocorrelation in residuals
- Check homoscedasticity
- Validate on different seasons/periods

### M6_04_documentation.ipynb
**Both tracks:**
- Create model card (purpose, limitations, metrics)
- Document OV-fiets system constraints
- List assumptions and edge cases
- Specify monitoring requirements
- Define retraining triggers

**Track A specific:**
- Decision threshold justification
- Class imbalance handling strategy
- False negative risk mitigation

**Track B specific:**
- Forecast horizon limitations
- Uncertainty quantification methodology
- Seasonality handling approach

### M6_05_governance.ipynb
**Both tracks:**
- Establish model update policy
- Define performance degradation thresholds
- Create incident response plan
- Document data quality requirements
- Set up model versioning strategy

## 📝 Naming Convention

### M6_01_model_validation.ipynb
- Evaluate on held-out test data
- Calculate confidence intervals
- Test model stability across time periods
- Validate assumptions

### M6_02_error_analysis.ipynb
- Identify where model performs poorly
- Analyze error patterns by time, location, weather
- Investigate large errors
- Document failure modes

### M6_03_model_interpretability.ipynb
- Analyze feature importance
- Create SHAP or LIME explanations
- Understand model decisions
- Document key drivers

### M6_04_model_documentation.ipynb
- Document model card (purpose, data, metrics)
- List model limitations
- Define monitoring metrics
- Create deployment checklist

## 📝 Naming Convention
Follow this pattern: `M6_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/evaluation.py` for evaluation functions
- Check [model documentation guidelines](../../docs/best_practices/model_documentation_guidelines.md) for templates
- Reference [code snippets](../../docs/references/code_snippets.md) for evaluation examples
- Be honest about model limitations
- Think about production monitoring
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `scikit-learn` - Evaluation metrics
- `shap` - Model explanations
- `matplotlib` / `seaborn` - Visualizations

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📋 [Model Documentation Guidelines](../../docs/best_practices/model_documentation_guidelines.md) - Document models
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - Evaluation examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices

## 📋 Model Card Checklist
- [ ] Model purpose and use case
- [ ] Training data description
- [ ] Performance metrics
- [ ] Known limitations
- [ ] Ethical considerations
- [ ] Maintenance plan

## ✨ Checkpoint
Before moving to Module 07, ensure:

**Track A (Classification):**
- [ ] Test set evaluation complete (confusion matrix, classification report)
- [ ] False positive/negative patterns analyzed
- [ ] Threshold tuning justified for business needs
- [ ] Prediction calibration validated
- [ ] Model card created with classification-specific details

**Track B (Regression/Time Series):**
- [ ] Test set evaluation complete for all horizons (24h, 48h, 72h)
- [ ] Residual analysis performed (patterns, normality, autocorrelation)
- [ ] Forecast accuracy assessed across seasons
- [ ] Uncertainty quantification validated
- [ ] Model card created with forecasting-specific details

**Both Tracks:**
- [ ] OV-fiets system constraints documented
- [ ] Error patterns analyzed and understood
- [ ] Model limitations clearly stated
- [ ] Governance framework established

---
**Next Module:** Module 07 - Visualization  
- **Track A:** Classification dashboards, confusion matrix heatmaps
- **Track B:** Forecast plots with uncertainty bands, residual analysis
