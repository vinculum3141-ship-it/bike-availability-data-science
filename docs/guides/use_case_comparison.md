# 🔀 Use Case Comparison: Commuter vs Tourist Prediction

**Document Purpose:** Help learners choose between Track A (Classification) and Track B (Regression/Time Series) by comparing the two prediction problems.

**Last Updated:** January 18, 2026

---

## 🎯 Two Distinct Prediction Problems

The OV-fiets system serves two primary user populations with different needs:

| Aspect | **Commuter Use Case** | **Tourist Use Case** |
|--------|----------------------|---------------------|
| **User Type** | Daily/weekly riders | Occasional/weekend riders |
| **Rental Duration** | 1-4 hours | 12-72 hours |
| **Prediction Horizon** | 2-4 hours ahead | 1-3 days ahead |
| **Question** | "Will a bike be available?" | "How many bikes will be available?" |
| **ML Problem Type** | **Binary Classification** | **Regression / Time Series** |
| **Track** | **Track A** | **Track B** |

---

## 🚴 Use Case 1: Commuter Prediction (Track A)

### Problem Statement
> **"I need to know if there will be a bike available when I arrive at Amsterdam Centraal tomorrow morning at 8:30 AM."**

### User Story
- Alice commutes daily from Amsterdam Centraal to her office
- She takes the train at 8:00 AM, arrives at 8:25 AM
- She needs a bike to reach her office 15 minutes away
- If no bikes are available, she'll need a backup plan (bus, walking, taxi)

### Prediction Goal
- **Binary outcome:** Bike available (yes/no)
- **Prediction window:** 2-4 hours ahead
- **Actionable:** Alice can adjust departure time or choose alternative transport

### Data Science Approach (Track A)
- **Problem type:** Binary classification
- **Target variable:** `bike_available` (1 if count > 0, else 0)
- **Features:** Peak hours, train schedules, weather (current), day of week
- **Models:** Logistic Regression, Random Forest Classifier, XGBoost Classifier
- **Metrics:** Accuracy, Precision, Recall, F1-score
- **Success criteria:** 85%+ accuracy, high recall (minimize false negatives)

### Why Classification?
- Commuters care about **availability**, not exact count
- Binary decision: "Go as planned" or "Find alternative"
- Imbalanced data: Bikes often available (class imbalance challenge)

---

## 🗺️ Use Case 2: Tourist Prediction (Track B)

### Problem Statement
> **"How many bikes will be available at Museumplein this Saturday afternoon? I'm planning a 2-day trip and need to know if I should reserve in advance."**

### User Story
- Bob is visiting Amsterdam next weekend with 3 friends
- They want to rent bikes on Saturday at 2 PM for a 2-day city tour
- They need **4 bikes** to be available simultaneously
- They want to forecast availability 3 days in advance to plan their itinerary

### Prediction Goal
- **Continuous outcome:** Number of bikes available (0-100+)
- **Prediction window:** 1-3 days ahead
- **Actionable:** Bob can choose a different station, different time, or reserve in advance

### Data Science Approach (Track B)
- **Problem type:** Regression or Time series forecasting
- **Target variable:** `bikes_available` (continuous count)
- **Features:** Holidays, events, weather forecasts (3-day), tourist seasons, lag features
- **Models:** Linear/Ridge Regression, Random Forest Regressor, XGBoost, ARIMA, Prophet, LSTM
- **Metrics:** MAE, RMSE, R², MAPE
- **Success criteria:** RMSE < 5 bikes, R² > 0.75, uncertainty quantification

### Why Regression/Time Series?
- Tourists care about **capacity**, not just binary availability
- Need count estimates: "Are 4 bikes available?"
- Long-term forecasts: Multi-day planning
- Seasonal patterns: Holidays, summer vs winter

---

## 🧭 Decision Tree: Which Track Should You Choose?

```
START: Do you have Python basics?
    ├─ NO → Go to Python fundamentals course first
    └─ YES → Continue
        │
        ├─ Are you new to machine learning?
        │   ├─ YES → **Track A** (Classification)
        │   └─ NO → Continue
        │       │
        │       ├─ Do you want to learn regression and time series?
        │       │   ├─ YES → **Track B** (Both tracks)
        │       │   └─ NO → **Track A** (Classification only)
        │       │
        │       └─ Do you have 30-45 hours available?
        │           ├─ YES → **Track B** (Both tracks)
        │           └─ NO → **Track A** (20-30 hours)
```

---

## ✅ Prerequisites Checklist

### Track A (Classification) — Beginner-Friendly
**Required:**
- ✅ Python basics (variables, loops, functions)
- ✅ Pandas fundamentals (DataFrames, filtering, grouping)
- ✅ Basic statistics (mean, median, correlation)

**Recommended (not required):**
- 📚 Matplotlib/Seaborn (can learn during course)
- 📚 Scikit-learn basics (taught from scratch)

**Time Commitment:** 20-30 hours

---

### Track B (Regression + Time Series) — Advanced
**Required:**
- ✅ **All Track A prerequisites**
- ✅ Machine learning fundamentals (supervised learning, train/test split, overfitting)
- ✅ Regression concepts (linear models, feature scaling)
- ✅ Evaluation metrics (MAE, RMSE, R²)

**Recommended:**
- 📚 Time series concepts (autocorrelation, stationarity)
- 📚 Statistical models (ARIMA, exponential smoothing)
- 📚 Deep learning basics (for optional LSTM extension)

**Time Commitment:** 30-45 hours (includes Track A content)

---

## 📊 Feature Engineering Comparison

| Feature Category | Track A (Classification) | Track B (Regression/TS) |
|-----------------|-------------------------|------------------------|
| **Temporal** | Hour, day_of_week, is_peak | + Holidays, school_vacation, long_weekends |
| **Weather** | Current conditions | + 3-day forecasts, accumulated rainfall |
| **Calendar** | Basic (weekday/weekend) | + Event calendars, tourist seasons |
| **Lag Features** | Simple (1-hour lag) | + Multi-period lags (24h, 48h, 168h) |
| **Domain** | Train schedules | + Tourist attractions proximity, hotel occupancy |
| **Complexity** | 5-10 features | 15-25 features |

---

## 🎓 Learning Outcomes Comparison

### What You'll Learn in Track A
- Binary classification for real-world problems
- Handling imbalanced datasets
- Logistic Regression, Random Forest, XGBoost
- Classification metrics (precision, recall, F1)
- Short-term prediction strategies

### Additional Outcomes in Track B
- Regression modeling for continuous targets
- Time series forecasting (ARIMA, Prophet)
- Multi-step ahead predictions
- Uncertainty quantification (confidence intervals)
- Long-term forecasting strategies
- Compare classification vs regression trade-offs

---

## 🏆 Capstone Project Comparison

### Track A Capstone
**Deliverables:**
- Classification model predicting bike availability 2-4 hours ahead
- Dashboard with binary predictions and confidence scores
- Report for commuter-focused use case

**Complexity:** Standard

---

### Track B Capstone
**Deliverables:**
- Regression model predicting bike counts 1-3 days ahead
- Time series forecasts with uncertainty intervals
- Dashboard with multi-day forecasts
- Report for tourist-focused use case

**Complexity:** Advanced

---

### Both Tracks Capstone (Ambitious!)
**Deliverables:**
- Both classification and regression models
- Comparative dashboard showing both approaches
- Recommendation engine: "When to use which model?"
- Comprehensive report analyzing trade-offs

**Complexity:** Comprehensive

---

## 🚦 When to Choose Each Track

### Choose Track A if you:
- ✅ Are new to machine learning
- ✅ Want to focus on classification problems
- ✅ Have 20-30 hours available
- ✅ Prefer shorter prediction horizons (2-4 hours)
- ✅ Want to complete the course faster

### Choose Track B (Both Tracks) if you:
- ✅ Have ML fundamentals already
- ✅ Want to learn regression AND classification
- ✅ Have 30-45 hours available
- ✅ Interested in time series forecasting
- ✅ Want comprehensive data science experience
- ✅ Building a portfolio project

### Still Unsure?
- 📖 Complete **Modules 1-3** first (foundation, shared by both tracks)
- 🧪 Explore the data in Module 3 and analyze patterns
- 🎯 Make your decision at the **end of Module 3** (decision point)
- 🔄 You can always come back and do the other track later!

---

## 🔗 Related Documents

- **[OV-fiets System Overview](ov_fiets_system_overview.md)** — Understand the domain and operational constraints
- **[Learning Pathways](learning_pathways.md)** — See complete learning journeys for each track
- **[Course Structure](course_structure_dual_track.md)** — Full module-by-module breakdown

---

## 💡 Quick Comparison Table

| Criteria | Track A | Track B |
|----------|---------|---------|
| **ML Problem** | Classification | Regression + Time Series |
| **Difficulty** | Beginner | Advanced |
| **Prerequisites** | Python basics | Python + ML fundamentals |
| **Duration** | 20-30 hrs | 30-45 hrs |
| **Prediction Horizon** | 2-4 hours | 1-3 days |
| **Models** | 3 classifiers | 6+ models (regression + TS) |
| **Use Case** | Commuter | Tourist + Capacity Planning |
| **Target Variable** | Binary (yes/no) | Continuous (count) |
| **Metrics** | Accuracy, F1 | MAE, RMSE, R² |
| **Capstone Complexity** | Standard | Advanced |

---

**Decision Point:** End of Module 3  
**Can Change Later:** Yes! Modules are designed to be revisited.

**Questions?** Review [Module 3 README](../notebooks/Module_03_Exploration_Profiling/README.md) for pattern analysis guidance.

---

**Document Maintainer:** Course Development Team  
**Last Updated:** January 18, 2026
