# Track B: Multi-Day Tourist Prediction (Regression/Time Series)

## 🎯 Track Focus
**Goal:** Predict the **number of bikes available** over next **24-72 hours** (regression + time series)

**Why This Track?**
- Focus on longer-term availability trends
- Perfect for tourists planning multi-day trips
- More complex problem: regression + time series forecasting
- Longer feature horizon: forecasts and trends matter

## 📊 Feature Engineering Strategy

### Time Horizon: **24-72 Hours**
All features in this track focus on **medium-term patterns**:
- Extended temporal patterns (day-of-week trends, seasonal effects)
- Weather **forecasts** (not just current conditions)
- Event calendars (festivals, conferences, holidays)
- Lag features over longer windows (1-7 days)
- Rolling statistics (24hr, 48hr, weekly averages)

### Key Feature Categories

#### 1. **Extended Temporal Features** (M4B_01)
- Day of week with weekend patterns
- Month and season indicators
- Holiday calendars (multi-day holidays affect demand)
- Cyclical encodings (hour, day, month)
- **Interaction features**: Weekend × Season, Holiday × Weather
- **Focus**: Identify multi-day demand patterns

#### 2. **Weather Forecast Features** (M4B_02)
- 24-72 hour temperature forecasts
- Multi-day precipitation predictions
- Weather trend indicators (improving/worsening)
- Aggregate forecasts (3-day average temperature)
- **Focus**: Future weather affecting trip planning decisions

#### 3. **Event Calendar Features** (M4B_03)
- Major events in Amsterdam (festivals, conferences)
- Concert/sports event indicators
- Tourist season indicators (high/low)
- School holiday periods
- **Focus**: Special events driving tourist demand

#### 4. **Long-Term Lag Features**
- Bikes available 24 hours ago
- Bikes available 7 days ago (weekly pattern)
- Rolling means (24hr, 48hr, 7-day windows)
- Trend indicators (increasing/decreasing availability)
- **Focus**: Capture multi-day availability patterns

#### 5. **Demand Trend Features**
- Daily demand growth rate
- Week-over-week changes
- Seasonal baseline adjustments
- **Focus**: Long-term trends for time series modeling

### Success Criteria
Your features should help answer:
- "What's the availability trend over next 3 days?"
- "Is a major event affecting demand?"
- "What's the weather forecast for tourists' trip?"
- "Is this a peak tourist season?"

## 🔗 What's Next?
After completing feature engineering, you'll move to:
- **Module 5 Track B**: Regression + Time Series models (Linear Regression, Random Forest, ARIMA, Prophet)
- **Evaluation**: RMSE, MAE, MAPE, forecast accuracy
- **Goal**: Minimize forecast error for multi-day predictions

## 📚 Resources
- [Use Case Comparison Guide](../../../docs/guides/use_case_comparison.md)
- [OV-fiets System Overview](../../../docs/guides/ov_fiets_system_overview.md)
- [Learning Pathways Guide](../../../docs/guides/learning_pathways.md)

## 🎓 Prerequisites
This track assumes:
- Completion of Track A **OR** solid understanding of:
  - Basic feature engineering (temporal, weather)
  - ML fundamentals (regression, evaluation metrics)
- Familiarity with time series concepts (lags, rolling windows)
