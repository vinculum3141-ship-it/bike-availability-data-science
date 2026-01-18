# Track A: Classification Models for Commuter Prediction

## 🎯 Track Focus
**Goal:** Build classification models to predict whether bikes will be available in the next 15 minutes

**Problem Type:** Binary Classification  
**Target Variable:** `bike_available` (1 = bikes available, 0 = no bikes available)  
**Evaluation Metrics:** Precision, Recall, F1-Score, ROC-AUC

## 📊 Modeling Strategy

### Why Classification?
Commuters need a **yes/no answer**: "Will bikes be available when I arrive?"
- Simple, actionable prediction
- Clear decision threshold
- Easier to interpret than regression
- Appropriate for short-term (15-minute) horizon

### Model Pipeline

#### 1. **Baseline Model** (M5A_01)
Start with simple baselines to establish performance floor:
- **Majority class**: Always predict "available"
- **Historical average**: Use station-specific availability rates
- **Time-based rules**: Rush hour = less availability
- **Purpose**: Establish minimum acceptable performance

#### 2. **Classification Models** (M5A_02)
Train multiple algorithms and compare:
- **Logistic Regression**: Simple, interpretable, fast
- **Random Forest**: Handles non-linear patterns, feature importance
- **Gradient Boosting (XGBoost/LightGBM)**: High performance, handles interactions
- **Support Vector Machines (optional)**: Good for binary classification

#### 3. **Model Selection & Tuning** (M5A_03)
- Hyperparameter optimization (GridSearch, RandomSearch)
- Cross-validation strategies (time-series aware)
- Feature importance analysis
- Model interpretation (SHAP, feature impacts)
- Final model selection and saving

### Evaluation Strategy

#### Key Metrics for Commuter Use Case:
1. **Recall (Sensitivity)**: Minimize false negatives
   - **Critical**: Don't predict "available" when bikes run out
   - **Impact**: Users arrive at empty stations (bad UX)

2. **Precision**: Minimize false positives
   - **Important**: Don't predict "unavailable" when bikes exist
   - **Impact**: Users avoid stations with bikes (lost usage)

3. **F1-Score**: Balance precision and recall
   - **Goal**: Harmonic mean for overall performance

4. **ROC-AUC**: Model discrimination ability
   - **Use**: Compare models, select probability threshold

#### Business Context:
**False Negative (FN) >> False Positive (FP)**  
→ Prioritize **Recall** over Precision  
→ Threshold tuning: Lower threshold = higher recall

### Class Imbalance Considerations
OV-fiets stations typically have bikes available (imbalanced classes):
- **Majority class**: Bikes available (~70-80%)
- **Minority class**: No bikes available (~20-30%)

**Handling strategies:**
- Class weights in model training
- SMOTE (Synthetic Minority Over-sampling)
- Threshold tuning to favor recall
- Stratified sampling in train/test splits

### Features from Module 4
Your Track A features:
- ✅ Temporal: Rush hour indicators, hour sin/cos, day of week
- ✅ Weather: Current conditions, rain indicators
- ✅ Train: Minutes to next train, train frequency

## 🔗 What's Next?
After completing modeling:
- **Module 6**: Model validation and testing
- **Module 7**: Visualization and dashboards
- **Capstone**: Build end-to-end commuter prediction system

## 📚 Resources
- [Use Case Comparison Guide](../../../docs/guides/use_case_comparison.md)
- [scikit-learn Classification Guide](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)

## 🎓 Prerequisites
- Completion of Module 4 Track A (feature engineering)
- Basic understanding of classification algorithms
- Familiarity with train/test splits and cross-validation
