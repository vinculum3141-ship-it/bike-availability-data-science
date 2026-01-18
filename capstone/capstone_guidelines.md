# 🎓 Capstone Project Guidelines

## Overview
The capstone project is your opportunity to demonstrate mastery of the entire data science lifecycle by building an end-to-end bike availability prediction system.

---

## 🛤️ Choose Your Track

**You must select one of two capstone tracks based on your learning path:**

### Track A: Real-Time Commuter Availability (Classification)
**Project Goal:** Build a binary classification system that predicts whether bikes will be available at a station in the next 15 minutes.
- **Audience:** Daily commuters who need immediate answers
- **Prediction Type:** Binary (Available/Not Available) + confidence
- **Time Horizon:** 15 minutes ahead
- **Use Case:** "Should I walk to this station or choose another?"
- **Recommended if you completed:** Module 4 Track A & Module 5 Track A

### Track B: Multi-Day Tourist Forecasting (Regression)
**Project Goal:** Build a time series forecasting system that predicts bike availability 24-72 hours ahead.
- **Audience:** Tourists planning their visit
- **Prediction Type:** Continuous (number of available bikes) + uncertainty intervals
- **Time Horizon:** 24-72 hours ahead
- **Use Case:** "How many bikes will be available Tuesday morning?"
- **Recommended if you completed:** Module 4 Track B & Module 5 Track B

**Note:** You may also attempt **both tracks** if you completed all sub-track modules and want an advanced challenge.

---

## 🎯 Project Objectives

Build a complete ML system that:
1. Acquires data from real-world sources
2. Processes and engineers meaningful features
3. Trains and validates predictive models
4. Visualizes insights through an interactive dashboard
5. Follows production-ready best practices

## 📋 Project Requirements

### 1. Data Acquisition (15%)
**Both tracks:**
- [ ] Fetch data from at least 2 different sources (bike API, weather API)
- [ ] Collect at least 3 months of historical data
- [ ] Handle API rate limits and errors gracefully
- [ ] Save raw data with proper versioning
- [ ] Document all data sources

**Track A additional:** Real-time data integration, train schedule API (optional)
**Track B additional:** Weather forecast API, event calendar API (optional)

### 2. Data Processing & Feature Engineering (20%)
**Both tracks:**
- [ ] Clean and validate raw data
- [ ] Handle missing values appropriately
- [ ] Avoid data leakage
- [ ] Document feature engineering decisions

**Track A (Classification) - Create 10+ features including:**
- [ ] Rush hour indicators (7-9 AM, 5-7 PM)
- [ ] Cyclical time encodings (sin/cos hour, day)
- [ ] Current weather conditions
- [ ] Train arrival proximity (if using train API)
- [ ] Weekend/holiday flags

**Track B (Time Series) - Create 10+ features including:**
- [ ] Lag features (7-day, 14-day historical patterns)
- [ ] Rolling statistics (mean, std over 7-day windows)
- [ ] Seasonal decomposition components
- [ ] Weather forecast features (24-72h ahead)
- [ ] Event calendar indicators (festivals, holidays)

### 3. Exploratory Data Analysis (15%)
- [ ] Generate automated profiling report
- [ ] Create at least 5 insightful visualizations
- [ ] Identify and document key patterns
- [ ] Analyze temporal trends
- [ ] Document data quality issues

### 4. Modeling (25%)
**Track A (Classification):**
- [ ] Create proper train/validation/test splits (time-based)
- [ ] Build baseline model (majority class classifier)
- [ ] Train at least 3 algorithms (e.g., Logistic Regression, Random Forest, XGBoost)
- [ ] Optimize for recall (minimize false negatives)
- [ ] Perform hyperparameter tuning (focus on class imbalance)
- [ ] Document performance: **Precision, Recall, F1, ROC-AUC**
- [ ] Determine optimal classification threshold

**Track B (Time Series):**
- [ ] Create proper train/validation/test splits (time-series aware)
- [ ] Build baseline model (seasonal naive, moving average)
- [ ] Train at least 3 approaches (e.g., Linear Regression, ARIMA/Prophet, XGBoost)
- [ ] Evaluate multi-horizon forecasts (24h, 48h, 72h)
- [ ] Perform hyperparameter tuning (lag orders, seasonality)
- [ ] Document performance: **RMSE, MAE, MAPE by horizon**
- [ ] Quantify prediction uncertainty (confidence intervals)

### 5. Validation & Governance (10%)
**Track A (Classification):**
- [ ] Validate on held-out test data
- [ ] Analyze confusion matrix (focus on false negatives)
- [ ] Perform error analysis by time of day, station type
- [ ] Create model card with precision/recall tradeoffs
- [ ] Define monitoring: track F1 score, false negative rate

**Track B (Time Series):**
- [ ] Validate on held-out test data
- [ ] Analyze residual plots and autocorrelation
- [ ] Perform error analysis by forecast horizon
- [ ] Create model card with multi-horizon accuracy
- [ ] Define monitoring: track RMSE degradation, seasonal drift

### 6. Visualization & Dashboard (10%)
**Track A (Classification Dashboard):**
- [ ] Real-time station availability predictions
- [ ] Confidence scores for each prediction
- [ ] Confusion matrix visualization
- [ ] ROC curve and threshold selector
- [ ] Station map with color-coded predictions
- [ ] Design for commuter decision-making

**Track B (Forecasting Dashboard):**
- [ ] Multi-day forecast calendar (24-72h ahead)
- [ ] Time series plots with uncertainty bands
- [ ] Forecast vs actual comparison
- [ ] Residual analysis plots
- [ ] Station selector with historical trends
- [ ] Design for trip planning

### 7. Automation & Best Practices (5%)
- [ ] Create reproducible pipeline
- [ ] Track experiments with MLflow
- [ ] Write clean, documented code
- [ ] Follow Git best practices
- [ ] Include comprehensive README

## 📅 Suggested Timeline

### Week 1-2: Data & Exploration
- Set up project structure
- Acquire and save data
- Perform EDA
- Document findings

### Week 3-4: Feature Engineering & Modeling
- Engineer features
- Build baseline models
- Train multiple algorithms
- Tune hyperparameters

### Week 5: Validation & Visualization
- Validate final model
- Create model documentation
- Build dashboard
- Perform error analysis

### Week 6: Polish & Documentation
- Clean up code
- Write comprehensive documentation
- Create presentation
- Prepare for review

## 📊 Deliverables

### 1. Code Repository
- Well-organized directory structure
- Clean, documented code
- Reproducible notebooks
- Working pipelines

### 2. Documentation
- Comprehensive README
- Model documentation/card
- Data dictionary
- API documentation

### 3. Dashboard
- Working Streamlit application
- Interactive visualizations
- Clear KPIs and metrics
- User-friendly interface

### 4. Final Report/Presentation
- Problem statement and approach
- Key findings and insights
- Model performance and limitations
- Future improvements
- Lessons learned

## 💡 Tips for Success

### Do:
- ✅ Start early and iterate
- ✅ Document as you go
- ✅ Test your code frequently
- ✅ Ask for feedback early
- ✅ Focus on insights, not just code
- ✅ Think about the end user
- ✅ Be honest about limitations

### Don't:
- ❌ Wait until the last minute
- ❌ Skip data validation
- ❌ Ignore data leakage
- ❌ Overcomplicate visualizations
- ❌ Forget to save your work
- ❌ Neglect documentation
- ❌ Be afraid to ask for help

## 🎯 Success Criteria

Your project should demonstrate:
- **Technical Skills**: Correct implementation of ML pipeline
- **Critical Thinking**: Thoughtful decisions and trade-offs
- **Communication**: Clear documentation and visualizations
- **Best Practices**: Clean code, version control, reproducibility
- **Impact**: Actionable insights for stakeholders

## 📚 Resources

- Review all module notebooks for reference
- Check `docs/` for guidelines and templates
- Refer to `docs/coding_standards.md` for code quality standards
- Use `self_evaluation.md` to assess your work before submission

## 🤔 Evaluation Questions

Your project should answer:
1. What is the business problem we're solving?
2. How good is our model? (metrics, validation)
3. What features matter most?
4. Where does the model fail? Why?
5. What would you do differently with more time?
6. How would you deploy this in production?

## 🚀 Going Beyond

Optional enhancements to stand out:
- Deploy dashboard to cloud (Streamlit Cloud, Heroku)
- Implement real-time predictions
- Add model monitoring
- Create API endpoints
- Build mobile-friendly interface
- Add automated alerts/notifications

## 📝 Submission

Submit the following:
1. GitHub repository link
2. Working dashboard link (if deployed)
3. Final report/presentation (PDF or slides)
4. Self-assessment against rubric

## ⏰ Deadline

Complete all deliverables by: **[Insert Date]**

---

**Remember**: This is your showcase project. Make it something you're proud to share with potential employers! 🌟
