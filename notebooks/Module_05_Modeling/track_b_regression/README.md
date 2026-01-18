# Track B: Regression & Time Series Models for Multi-Day Prediction

## 🎯 Track Focus
**Goal:** Build regression and time series models to predict the number of bikes available over 24-72 hours

**Problem Type:** Regression + Time Series Forecasting  
**Target Variable:** `bikes_available` (continuous numeric value)  
**Evaluation Metrics:** RMSE, MAE, MAPE, R², Forecast Accuracy

## 📊 Modeling Strategy

### Why Regression + Time Series?
Tourists need **quantitative forecasts**: "How many bikes will be available over my 3-day trip?"
- Numeric predictions (0-20+ bikes)
- Uncertainty quantification important
- Longer horizons require time series techniques
- Seasonal and trend patterns matter

### Model Pipeline

#### 1. **Regression Models** (M5B_01)
Classical regression approaches for numeric prediction:
- **Linear Regression**: Baseline, interpretable
- **Ridge/Lasso Regression**: Regularization for feature selection
- **Random Forest Regressor**: Non-linear patterns, handles interactions
- **Gradient Boosting (XGBoost/LightGBM)**: High performance
- **Purpose**: Predict bikes_available as numeric target

#### 2. **Time Series Models** (M5B_02)
Specialized models for temporal forecasting:
- **ARIMA/SARIMA**: Classical time series (seasonality, trends)
- **Prophet**: Facebook's robust forecasting tool
- **LSTM (optional)**: Deep learning for complex patterns
- **Purpose**: Capture temporal dependencies and forecasting

#### 3. **Uncertainty Quantification** (M5B_03)
- Prediction intervals (confidence bounds)
- Probabilistic forecasting
- Quantile regression
- Ensemble methods for uncertainty
- **Purpose**: Provide "likely range" not just point predictions

### Evaluation Strategy

#### Key Metrics for Tourist Use Case:

1. **RMSE (Root Mean Squared Error)**: Overall prediction accuracy
   - Penalizes large errors heavily
   - Same units as target (number of bikes)

2. **MAE (Mean Absolute Error)**: Average prediction error
   - More interpretable than RMSE
   - Less sensitive to outliers

3. **MAPE (Mean Absolute Percentage Error)**: Relative error
   - Percentage-based, easy to communicate
   - "On average, predictions are ±15% off"

4. **R² (Coefficient of Determination)**: Variance explained
   - How well model captures patterns
   - 0.0-1.0 scale (higher = better)

5. **Forecast Accuracy**: Multi-step ahead performance
   - 24-hour, 48-hour, 72-hour horizons
   - Does accuracy degrade over time?

#### Business Context:
**Tourists need reliable ranges**:
- "Expect 5-15 bikes available" is useful
- Point predictions less important than intervals
- Uncertainty quantification critical

### Time Series Considerations

**Data Leakage Prevention:**
- Use only past data (no future information)
- Rolling window cross-validation
- Respect temporal order in train/test splits

**Feature Engineering Validation:**
- Lag features must use only historical data
- No "future weather actuals" (use forecasts only)
- Validate stationarity for ARIMA models

**Seasonality Handling:**
- Weekly patterns (commuter cycles)
- Monthly patterns (tourist seasons)
- Holiday effects (events, school breaks)

### Features from Module 4
Your Track B features:
- ✅ Extended Temporal: Seasonal patterns, lag features (24h, 7d), rolling means
- ✅ Weather Forecasts: 24-72 hour temperature, precipitation predictions
- ✅ Event Calendars: Festivals, tourist seasons, holidays

## 🔗 What's Next?
After completing modeling:
- **Module 6**: Time series validation, backtesting
- **Module 7**: Forecast visualization, uncertainty plots
- **Capstone**: Build multi-day prediction dashboard

## 📚 Resources
- [Use Case Comparison Guide](../../../docs/guides/use_case_comparison.md)
- [Prophet Documentation](https://facebook.github.io/prophet/)
- [statsmodels Time Series](https://www.statsmodels.org/stable/tsa.html)
- [scikit-learn Regression Guide](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

## 🎓 Prerequisites
- Completion of Module 4 Track B (feature engineering)
- Understanding of regression algorithms
- Familiarity with time series concepts (stationarity, autocorrelation)
- Knowledge of train/test splits for time series
