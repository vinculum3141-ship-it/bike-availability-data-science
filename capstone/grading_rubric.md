# 📊 Capstone Project Grading Rubric

## Total Points: 100

---

## 🛤️ Track Selection

**You will be graded according to the track you selected:**
- **Track A:** Real-Time Commuter Availability (Classification)
- **Track B:** Multi-Day Tourist Forecasting (Regression/Time Series)
- **Both Tracks:** Advanced challenge (graded on both criteria)

**Track-specific differences:**
- **Feature Engineering:** Track A focuses on real-time features; Track B on historical patterns
- **Modeling:** Track A uses classification algorithms; Track B uses regression/time series
- **Metrics:** Track A uses precision/recall/F1; Track B uses RMSE/MAE/MAPE
- **Validation:** Track A analyzes confusion matrices; Track B analyzes residuals and forecast horizons
- **Dashboard:** Track A shows classification alerts; Track B shows forecast calendars

---

## 1. Data Acquisition (15 points)

### Excellent (13-15 points)
- Successfully fetches data from multiple sources (bike + weather APIs)
- Implements robust error handling and retry logic
- Properly manages API keys and credentials
- Data is well-organized and versioned
- All data sources are thoroughly documented

### Good (10-12 points)
- Fetches data from required sources with minor issues
- Basic error handling implemented
- Data is organized adequately
- Sources are documented

### Satisfactory (7-9 points)
- Fetches data but with significant manual intervention
- Limited error handling
- Basic organization
- Minimal documentation

### Needs Improvement (0-6 points)
- Cannot reliably fetch data
- Poor error handling
- Disorganized data storage
- Lacks documentation

---

## 2. Data Processing & Feature Engineering (20 points)

### Excellent (17-20 points)
- Comprehensive data cleaning and validation
- Creative and meaningful feature engineering (10+ features)
- **Track A:** Rush hour indicators, cyclical encodings, current weather, train proximity
- **Track B:** Lag features (7-14 day), rolling statistics, seasonal components, weather forecasts
- No data leakage (critical for time series!)
- Proper handling of missing values and outliers
- Well-documented feature definitions and rationale

### Good (14-16 points)
- Solid data cleaning process
- Good set of features (7-9 features)
- **Track A:** Basic temporal and weather features
- **Track B:** Some lag features and rolling statistics
- Minimal data leakage risk
- Adequate handling of missing data
- Features are documented

### Satisfactory (10-13 points)
- Basic cleaning performed
- Limited features (4-6 features)
- **Track A:** Only basic hour/day features
- **Track B:** Only simple lag features without rolling statistics
- Some potential data leakage
- Simple missing data handling
- Minimal documentation

### Needs Improvement (0-9 points)
- Insufficient data cleaning
- Very few or poor features (<4)
- Clear data leakage issues (especially problematic for Track B)
- Poor handling of data quality issues

---

## 4. Modeling (25 points)

### Excellent (22-25 points)
**Track A (Classification):**
- Implements 3+ algorithms (Logistic Regression, Random Forest, XGBoost, etc.)
- Properly handles class imbalance (SMOTE, class weights)
- Optimizes for recall to minimize false negatives
- Achieves F1 > 0.75 and Recall > 0.80
- Determines optimal classification threshold
- Thorough hyperparameter tuning

**Track B (Time Series):**
- Implements 3+ approaches (Linear/Ridge, ARIMA/Prophet, XGBoost)
- Proper time-series cross-validation
- Multi-horizon evaluation (24h, 48h, 72h)
- Achieves MAPE < 15% for 24h forecast
- Quantifies uncertainty (confidence intervals)
- Thorough hyperparameter tuning

**Both tracks:** Well-justified model selection, excellent documentation

### Good (18-21 points)
**Track A:** 3 algorithms, basic class imbalance handling, F1 > 0.65, some tuning
**Track B:** 3 approaches, time-series aware splits, MAPE < 20%, basic uncertainty quantification
**Both:** Adequate model comparison and documentation

### Satisfactory (13-17 points)
**Track A:** 2 algorithms, minimal imbalance handling, F1 > 0.50, limited tuning
**Track B:** 2 approaches, simple splits, MAPE < 30%, no uncertainty quantification
**Both:** Basic model selection, limited documentation

### Needs Improvement (0-12 points)
**Track A:** Single algorithm, ignores class imbalance, F1 < 0.50
**Track B:** Single approach, data leakage in splits, MAPE > 30%
**Both:** Poor model performance, insufficient documentation

---

## 3. Exploratory Data Analysis (15 points)

### Excellent (13-15 points)
- Comprehensive automated profiling
- Insightful visualizations (5+ high-quality plots)
- Clear identification of patterns and anomalies
- Thorough temporal analysis
- Well-documented insights and findings

### Good (10-12 points)
- Good profiling and analysis
- Adequate visualizations (3-4 plots)
- Identifies main patterns
- Basic temporal analysis
- Key findings documented

### Satisfactory (7-9 points)
- Basic EDA performed
- Limited visualizations (1-2 plots)
- Surface-level insights
- Minimal documentation

### Needs Improvement (0-6 points)
- Minimal or no EDA
- Poor or no visualizations
- No meaningful insights
- Lacks documentation

---

## 4. Modeling (25 points)

### Excellent (22-25 points)
- Proper temporal train/validation/test splits
- Strong baseline model for comparison
- Multiple algorithms tested (3+)
- Systematic hyperparameter tuning
- Rigorous model comparison with clear metrics
- Well-justified model selection
- Excellent performance (e.g., R² > 0.75)

### Good (18-21 points)
- Appropriate data splits
- Baseline model included
- 2-3 algorithms tested
- Basic hyperparameter tuning
- Model comparison performed
- Good performance (e.g., R² 0.60-0.75)

### Satisfactory (13-17 points)
- Basic data splits
- Limited baseline
- 1-2 algorithms tested
- Minimal tuning
- Basic comparison
- Moderate performance (e.g., R² 0.45-0.60)

### Needs Improvement (0-12 points)
- Poor data splitting (data leakage)
- No baseline
- Single model or poor implementation
- No tuning
- Poor performance (e.g., R² < 0.45)

---

## 5. Model Validation & Governance (10 points)

### Excellent (9-10 points)
- Comprehensive validation on test data
- Thorough error analysis with insights
- Complete model documentation/card
- Clear limitations and assumptions documented
- Thoughtful monitoring strategy

### Good (7-8 points)
- Solid validation performed
- Basic error analysis
- Good model documentation
- Limitations mentioned
- Basic monitoring plan

### Satisfactory (5-6 points)
- Minimal validation
- Limited error analysis
- Basic documentation
- Some limitations noted

### Needs Improvement (0-4 points)
- No proper validation
- No error analysis
- Poor or missing documentation
- No consideration of limitations

---

## 6. Visualization & Dashboard (10 points)

### Excellent (9-10 points)
- Professional, interactive dashboard (Streamlit)
- Clear KPIs and metrics
- Effective visualizations
- User-friendly interface
- Designed for non-technical stakeholders
- Deployed and accessible

### Good (7-8 points)
- Working dashboard
- Good visualizations
- Clear metrics
- Functional interface
- Mostly accessible

### Satisfactory (5-6 points)
- Basic dashboard
- Limited interactivity
- Simple visualizations
- Functional but basic

### Needs Improvement (0-4 points)
- No dashboard or non-functional
- Poor visualizations
- Not user-friendly
- Incomplete

---

## 7. Automation & Reproducibility (5 points)

### Excellent (5 points)
- Fully automated pipeline
- Experiment tracking implemented (MLflow)
- One-command reproducibility
- Well-structured code

### Good (4 points)
- Mostly automated
- Basic experiment tracking
- Reproducible with minor setup
- Clean code

### Satisfactory (3 points)
- Partially automated
- Manual steps required
- Basic reproducibility

### Needs Improvement (0-2 points)
- Not automated
- Not reproducible
- Poor structure

---

## 8. Code Quality & Documentation (10 points)

### Excellent (9-10 points)
- Clean, PEP 8 compliant code
- Comprehensive docstrings and comments
- Excellent README with setup instructions
- Clear project structure
- Git best practices followed
- All deliverables complete

### Good (7-8 points)
- Clean, readable code
- Good documentation
- Solid README
- Good project structure
- Decent Git usage

### Satisfactory (5-6 points)
- Functional code
- Basic documentation
- Minimal README
- Acceptable structure

### Needs Improvement (0-4 points)
- Poor code quality
- Lack of documentation
- Missing or poor README
- Disorganized

---

## 9. Communication & Insights (5 points)

### Excellent (5 points)
- Clear, compelling narrative
- Actionable business insights
- Honest about limitations
- Well-presented findings
- Professional presentation

### Good (4 points)
- Clear communication
- Good insights
- Limitations addressed
- Solid presentation

### Satisfactory (3 points)
- Basic communication
- Some insights
- Functional presentation

### Needs Improvement (0-2 points)
- Unclear communication
- No real insights
- Poor or missing presentation

---

## Bonus Points (up to +5)

Additional credit for:
- [ ] Deployed dashboard to cloud (+2)
- [ ] Real-time predictions implemented (+2)
- [ ] API endpoints created (+2)
- [ ] Advanced techniques (e.g., deep learning, ensemble methods) (+2)
- [ ] Exceptional documentation or visualization (+1)
- [ ] Creative problem-solving (+1)

---

## Grade Scale

| Points | Grade | Description |
|--------|-------|-------------|
| 90-100+ | A | Exceptional work, publication-ready |
| 80-89 | B | Strong work, portfolio-worthy |
| 70-79 | C | Solid work, meets requirements |
| 60-69 | D | Needs improvement in key areas |
| < 60 | F | Does not meet minimum requirements |

---

## Self-Assessment

Before submission, rate yourself on each criterion and identify:
1. Your strongest areas
2. Areas needing improvement
3. Lessons learned
4. What you'd do differently next time

---

## Instructor Feedback Template

**Student Name:** _________________
**Date:** _________________

### Strengths:
- 
- 
- 

### Areas for Improvement:
- 
- 
- 

### Overall Comments:


**Total Score: _____ / 100**

**Grade: _____**
