# 📚 Course Structure: Dual-Track Edition

**Course Title:** Data Science for Smart Cities: Bike Sharing Prediction  
**Platform:** Udemy (Self-paced)  
**Last Updated:** January 18, 2026  
**Total Duration:** 20-30 hours (Track A) | 30-45 hours (Both Tracks)

---

## 🎯 Course Overview

This course offers **two learning paths** to accommodate diverse skill levels:

- **Track A (Beginner):** Focus on classification for short-term predictions (Modules 1-3 → 4A → 5A → 6-10 → Capstone A)
- **Track B (Advanced):** Add regression and time series for long-term forecasting (All Track A + 4B + 5B → Capstone B)

**Track Selection:** Students learn about both tracks in Module 1 and make an informed decision at Module 3 end.

---

## 📋 Module Structure

### 🔹 **Module 1 – Introduction & Project Overview**

**Duration:** 30–45 min  
**Track:** Foundation (All Students)

**Learning Objectives:**
- Understand the scope and goals of the course project
- Learn about smart cities, bike-sharing systems, and open data in the Netherlands
- Explore the problem of predicting bike availability
- **NEW:** Introduction to dual-track structure (Track A vs Track B)

**Content:**
- Video: Project goals & workflow overview
- Video: **Dual-Track Introduction** (commuter vs multi-day prediction)
- Reading: Open datasets (Amsterdam Open Data, KNMI weather)
- Reading: **Track Selection Guide** (preview of Module 3 decision point)
- Notebook: Explore raw dataset

**Exercise:**
- Identify data sources and their schema
- Download and inspect sample data
- **NEW:** Complete self-assessment quiz (informational, not binding)

**Outcomes:**
- Explain the importance of data science in smart cities
- Identify open data sources relevant to bike-sharing prediction
- Set up the project environment in Google Colab
- **NEW:** Understand two prediction use cases (commuter vs multi-day)

---

### 🔹 **Module 2 – Data Acquisition & Integration**

**Duration:** 1–2 hrs  
**Track:** Foundation (All Students)

**Learning Objectives:**
- Learn how to fetch data from APIs and CSV files
- Combine multiple datasets into a single dataset for analysis
- Merge multiple datasets
- Handle missing values
- **NEW:** Understand operational constraints (15-min API refresh, 72-hour rentals)

**Content:**
- Video: Using requests and pandas for data fetching
- Video: **OV-fiets Operational Context** (no docks, same-station returns)
- Notebook: Integrate bike-sharing data with weather and time features
- Notebook: **Domain Insights** (SOLUTIONS notebook already has this)

**Exercise:**
- Write a Python script to combine datasets into a single CSV
- Document the data sources
- **NEW:** Identify commuter vs tourist rental patterns in data

**Outcomes:**
- Access Amsterdam Open Data and KNMI weather data
- Merge datasets correctly using Python and Pandas
- Document data sources and structure
- **NEW:** Understand real operational data constraints

---

### 🔹 **Module 3 – Data Exploration & Profiling**

**Duration:** 1.5–2.5 hrs  
**Track:** Foundation (All Students)

**Learning Objectives:**
- Perform exploratory data analysis (EDA)
- Explore and profile data to identify trends, patterns, and quality issues
- Visualize distributions and relationships between variables
- **NEW:** Identify commuter vs tourist patterns
- **NEW:** Make informed track selection decision

**Content:**
- Video: Using pandas-profiling and sweetviz
- Video: **Pattern Analysis** (commuter peak hours vs tourist multi-day)
- Notebook: Visualize bike availability trends, weather impact
- Notebook: **NEW - M3_05 Commuter vs Tourist Pattern Analysis**

**Exercise:**
- Generate an EDA report
- Identify missing or unusual data points
- **NEW:** Analyze temporal patterns (weekday vs weekend, peak hours, holiday spikes)
- **NEW:** Visualize two distinct user populations

**Outcomes:**
- Perform descriptive statistics and generate summary reports
- Identify missing values, outliers, and anomalies
- Create visualizations using Pandas, Seaborn, and Pandas-Profiling
- **NEW:** Distinguish commuter from tourist rental behavior
- **NEW:** 🎯 DECISION POINT: Choose Track A, Track B, or Both

**Track Selection Guide (End of Module 3):**
- Self-assessment checklist
- Prerequisites reminder (Python basics vs ML fundamentals)
- Time commitment (20-30 hrs vs 30-45 hrs)
- Link to use case comparison guide

---

## 🔀 **TRACKS DIVERGE HERE**

Students now choose their learning path. Beginners typically follow Track A; advanced learners do both tracks.

---

### 🔹 **Module 4A – Feature Engineering (Beginner Track)**

**Duration:** 1.5–2 hrs  
**Track:** Track A - Classification

**Learning Objectives:**
- Transform raw data into machine learning-ready inputs for **short-term classification**
- Learn techniques for creating meaningful features for **2-4 hour predictions**
- Transform features for modeling

**Content:**
- Video: Feature engineering concepts for classification
- Video: **Commuter Prediction Features** (peak hours, train schedules)
- Notebook: Create time-based features (hour, day, is_peak)
- Notebook: Weather features (current conditions)
- Notebook: Train schedule integration

**Exercise:**
- Engineer at least 5 classification-focused features
- Use ColumnTransformer and pipelines for transformations
- Focus on features relevant to short-term availability

**Outcomes:**
- Create time-based, weather-based features for classification
- Build preprocessing pipelines using Scikit-learn
- Prepare a final dataset ready for binary classification modeling

---

### 🔹 **Module 4B – Advanced Feature Engineering (Advanced Track)**

**Duration:** 1.5–2 hrs  
**Track:** Track B - Regression/Time Series  
**Prerequisites:** Complete Module 4A or have ML experience

**Learning Objectives:**
- Transform raw data for **long-term regression** and **time series forecasting**
- Learn techniques for creating features for **1-3 day predictions**
- Handle extended temporal patterns

**Content:**
- Video: Advanced feature engineering for regression
- Video: **Multi-Day Forecasting Features** (holidays, events, tourist attractions)
- Notebook: Extended temporal features (holidays, long weekends, school vacations)
- Notebook: Weather forecasts (3-day ahead)
- Notebook: Event calendar integration (festivals, holidays)

**Exercise:**
- Engineer at least 8 advanced features
- Create lag features for multiple time periods
- Handle tourist attraction proximity

**Outcomes:**
- Create long-term temporal and event-based features
- Build advanced preprocessing pipelines
- Prepare dataset for regression and time series modeling

---

### 🔹 **Module 5A – Modeling: Classification (Beginner Track)**

**Duration:** 2–2.5 hrs  
**Track:** Track A - Classification

**Learning Objectives:**
- Train baseline and advanced **classification models**
- Compare different algorithms for **binary prediction** (bike available: yes/no)
- Evaluate with classification metrics

**Content:**
- Video: **Classification models** (Logistic Regression, Random Forest, XGBoost)
- Video: **Classification metrics** (accuracy, precision, recall, F1-score)
- Notebook: Implement baseline logistic regression
- Notebook: Train Random Forest and XGBoost classifiers
- Notebook: Handle imbalanced data

**Exercise:**
- Train a Logistic Regression baseline
- Train a Random Forest or XGBoost model
- Compare performance metrics (accuracy, F1-score, precision/recall)
- Create confusion matrix

**Outcomes:**
- Implement classification models for short-term prediction
- Evaluate model performance with appropriate classification metrics
- Document findings and select best-performing model
- **Target:** Predict bike availability 2-4 hours ahead

---

### 🔹 **Module 5B – Advanced Modeling: Regression & Time Series (Advanced Track)**

**Duration:** 2.5–3 hrs  
**Track:** Track B - Regression/Time Series  
**Prerequisites:** Complete Module 5A or have ML experience

**Learning Objectives:**
- Train **regression models** for continuous predictions
- Implement **time series forecasting** techniques
- Compare classification vs regression approaches
- Quantify prediction uncertainty

**Content:**
- Video: **Regression models** (Linear Regression, Random Forest Regressor, Gradient Boosting)
- Video: **Time series models** (ARIMA, Prophet, LSTM basics)
- Video: **Uncertainty quantification** (confidence intervals, prediction intervals)
- Notebook: Implement regression models
- Notebook: Train time series models (ARIMA, Prophet)
- Notebook: Multi-step ahead forecasting
- Notebook: Uncertainty quantification

**Exercise:**
- Train multiple regression models
- Implement at least one time series model (Prophet or ARIMA)
- Compare regression vs classification approaches
- Calculate prediction intervals

**Outcomes:**
- Implement regression and time series models for long-term forecasting
- Evaluate model performance with regression metrics (MAE, RMSE, R²)
- Compare different forecasting techniques
- **Target:** Predict bike counts 1-3 days ahead

---

## 🔀 **TRACKS CONVERGE HERE**

All students continue with integration modules, applying concepts to their chosen model(s).

---

### 🔹 **Module 6 – Model Validation & Governance**

**Duration:** 1.5–2 hrs  
**Track:** Integration (All Students)

**Learning Objectives:**
- Learn model validation techniques and governance best practices
- Evaluate model performance reliably
- Document assumptions and limitations
- Track experiments and document assumptions
- **NEW:** Validate different model types (classification vs regression)

**Content:**
- Video: Train/test split, cross-validation, MLflow tracking
- Video: **Validating Classification Models** (Track A focus)
- Video: **Validating Regression Models** (Track B focus)
- Notebook: Track experiments and record metrics
- Notebook: **Model comparison** (if completed both tracks)

**Exercise:**
- Implement cross-validation for your model type
- Log results in MLflow
- **NEW:** Compare validation strategies (classification vs regression)

**Outcomes:**
- Perform train/test splits and cross-validation
- Track experiments in MLflow
- Document model limitations and assumptions
- **NEW:** Understand validation differences between model types

---

### 🔹 **Module 7 – Visualization & Communication**

**Duration:** 1.5–2 hrs  
**Track:** Integration (All Students)

**Learning Objectives:**
- Visualize model predictions and communicate insights effectively
- Build interactive dashboards for stakeholders
- **NEW:** Communicate different prediction types (classification vs regression)

**Content:**
- Video: Using Plotly and Streamlit
- Video: **Dashboards for Classification** (Track A focus)
- Video: **Dashboards for Regression/Forecasting** (Track B focus)
- Notebook: Visualize predictions vs. actual values
- Notebook: **Track-specific visualizations**

**Exercise:**
- Create an interactive dashboard with Streamlit for your model
- Highlight top 5 bike stations with prediction gaps
- **NEW:** Visualize appropriate outputs (probabilities vs counts vs time series)

**Outcomes:**
- Create interactive visualizations using Plotly or Streamlit
- Present predicted vs actual bike availability clearly
- Build a dashboard to communicate insights to city planners or users
- **NEW:** Adapt visualizations to model type

---

### 🔹 **Module 8 – Automation & Reproducibility**

**Duration:** 1–2 hrs  
**Track:** Integration (All Students)

**Learning Objectives:**
- Automate the end-to-end workflow for repeatability
- Ensure reproducibility of data science pipeline results
- **NEW:** Handle different pipeline types (classification vs regression)

**Content:**
- Video: Using Papermill for reproducible notebooks
- Notebook: Pipeline automation from data acquisition to visualization
- Notebook: **Track-specific pipeline considerations**

**Exercise:**
- Run the full pipeline with a single script for your model
- Verify reproducibility
- **NEW:** Document pipeline differences between tracks

**Outcomes:**
- Create a Python script or notebook that runs the full pipeline
- Use Papermill or equivalent tools for reproducible notebook execution
- Share reproducible workflows via GitHub
- **NEW:** Understand automation for different model types

---

### 🔹 **Module 9 – Experimentation & Continuous Learning**

**Duration:** 1–1.5 hrs  
**Track:** Integration (All Students)

**Learning Objectives:**
- Experiment with different features, models, and parameters
- Compare different feature sets and models
- Learn from experiment results
- Learn how to track and improve model performance iteratively
- **NEW:** Compare experiments across tracks (if completed both)

**Content:**
- Video: Experimentation and logging best practices
- Notebook: Track multiple experiments with MLflow
- Notebook: **Cross-track comparison** (if applicable)

**Exercise:**
- Experiment with different features or time windows for your model
- Document which changes improve performance
- **NEW:** (Optional) Compare Track A vs Track B performance

**Outcomes:**
- Conduct experiments to improve predictive performance
- Track all experiments in MLflow
- Analyze experiment results to inform next steps
- **NEW:** Understand trade-offs between different modeling approaches

---

### 🔹 **Module 10 – Collaboration & Reporting**

**Duration:** 30–60 min  
**Track:** Integration (All Students)

**Learning Objectives:**
- Learn how to share work with peers and stakeholders
- Document findings in a professional manner
- Write reports for stakeholders

**Content:**
- Video: Using GitHub for collaboration
- Example report template for city planners
- **NEW:** Track-specific reporting examples

**Exercise:**
- Publish notebook and dashboard to GitHub
- Write a short report summarizing insights and recommendations
- **NEW:** Tailor report to your prediction type (short-term vs long-term)

**Outcomes:**
- Publish notebooks and dashboards on GitHub
- Write a mini-report summarizing methodology, findings, and recommendations
- Communicate insights to technical and non-technical audiences

---

### 🔹 **Module 11 – Capstone Project**

**Duration:** 2–4 hrs (depends on track)  
**Track:** All Students (Track-specific requirements)

**Learning Objectives:**
- Apply all concepts in an end-to-end data science project
- Implement a full end-to-end workflow
- Demonstrate mastery of all modules

**Track A Capstone (Beginner):**
- Build complete classification pipeline
- Predict bike availability 2-4 hours ahead
- Dashboard with binary predictions
- Report on commuter use case

**Track B Capstone (Advanced):**
- Build complete regression/time series pipeline
- Predict bike counts 1-3 days ahead
- Dashboard with forecasts and uncertainty
- Report on multi-day planning use case

**Both Tracks Capstone (Ambitious):**
- Implement both models
- Comparison dashboard
- Recommendation engine (when to use which model)
- Comprehensive report

**Exercise:**
- Build the complete pipeline for your chosen track(s)
- Submit code, dashboard, and report as a portfolio-ready project

**Outcomes:**
- Build a complete bike availability prediction workflow
- Produce a reproducible notebook and interactive dashboard
- Submit a professional report, suitable for a portfolio or resume
- **Self-evaluate using provided rubric**

---

## 🎓 Completion & Certification

**Completion Criteria:**
- Complete capstone project (any track)
- Self-evaluate using grading rubric
- Receive single course certificate

**Certificate States:** "Data Science for Smart Cities: Bike Sharing Prediction"  
*(Learners self-assess their level and track completion)*

---

## 🚀 Optional Extensions

Available to all students regardless of track:

- Real-time prediction with streaming data (Kafka/MQTT)
- Deploy a public Streamlit app
- Compare multiple cities' bike-sharing patterns
- Ensemble methods (combine Track A and Track B models)
- Deep learning for time series (LSTM, GRU)

---

## 🛠️ Delivery & Tools

**Video Lectures:** Pre-recorded screencasts (track-specific videos added)  
**Notebooks:** Google Colab (free cloud execution)  
**Datasets:** Open data from Amsterdam (OV-fiets), KNMI  
**Version Control:** GitHub  
**Experiment Tracking:** MLflow (local or free-tier)  
**Visualization:** Plotly, Streamlit  
**Documentation:** Comprehensive READMEs + SOLUTIONS notebooks

---

## 📊 Course Statistics

| Metric | Track A | Track B | Both Tracks |
|--------|---------|---------|-------------|
| Duration | 20-30 hrs | +10-15 hrs | 30-45 hrs |
| Modules | 1-3, 4A, 5A, 6-10, 11 | All Track A + 4B, 5B | All modules |
| Skill Level | Beginner | Advanced | Comprehensive |
| Model Types | Classification | Regression, Time Series | Both |
| Prediction Horizon | 2-4 hours | 1-3 days | Both |
| Prerequisites | Python basics | + ML fundamentals | Same as Track B |
| Capstone Complexity | Standard | Advanced | Comprehensive |

---

## 🗺️ Learning Pathways

### Beginner Path (Track A Only)
```
Module 1 (Intro + Track Awareness)
    ↓
Module 2 (Data Acquisition)
    ↓
Module 3 (EDA + Track Decision) → Choose Track A
    ↓
Module 4A (Classification Features)
    ↓
Module 5A (Classification Models)
    ↓
Modules 6-10 (Integration)
    ↓
Module 11 (Capstone Track A)
```

### Advanced Path (Both Tracks)
```
Module 1 (Intro + Track Awareness)
    ↓
Module 2 (Data Acquisition)
    ↓
Module 3 (EDA + Track Decision) → Choose Both Tracks
    ↓
Module 4A + 4B (All Features)
    ↓
Module 5A + 5B (All Models)
    ↓
Modules 6-10 (Integration with comparison)
    ↓
Module 11 (Comprehensive Capstone)
```

---

## 📝 Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-01-18 | 2.0 | Added dual-track structure (Track A + Track B) |
| - | 1.0 | Original single-path course structure |

---

**Document Owner:** Course Development Team  
**Last Reviewed:** January 18, 2026  
**Next Review:** After Phase 1 implementation
