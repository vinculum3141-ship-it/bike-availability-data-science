# 🗺️ Learning Pathways Guide

**Document Purpose:** Visualize complete learning journeys for Track A (Beginner) and Track B (Advanced) to help learners plan their course experience.

**Last Updated:** January 18, 2026

---

## 🎓 Course Learning Pathways

This course offers **two flexible learning paths** designed to accommodate different skill levels and time commitments. You'll choose your path at the **end of Module 3** after exploring the data and understanding both use cases.

---

## 🛤️ Pathway Overview

```
                    START HERE
                        ↓
        ╔═══════════════════════════════════╗
        ║   Module 1: Introduction          ║
        ║   - Project overview              ║
        ║   - Dual-track introduction       ║
        ║   - Self-assessment (optional)    ║
        ╚═══════════════════════════════════╝
                        ↓
        ╔═══════════════════════════════════╗
        ║   Module 2: Data Acquisition      ║
        ║   - API access                    ║
        ║   - Data merging                  ║
        ║   - Operational context           ║
        ╚═══════════════════════════════════╝
                        ↓
        ╔═══════════════════════════════════╗
        ║   Module 3: EDA & Profiling       ║
        ║   - Pattern analysis              ║
        ║   - Commuter vs tourist patterns  ║
        ║   - DECISION POINT (end of M3)    ║
        ╚═══════════════════════════════════╝
                        ↓
            ┌───────────┴───────────┐
            │                       │
    ╔═══════▼═══════╗      ╔═══════▼═══════════╗
    ║  TRACK A      ║      ║  TRACK B          ║
    ║  Classification║      ║  Both Tracks      ║
    ╚═══════════════╝      ╚═══════════════════╝
```

---

## 📘 Track A: Beginner Path (Classification)

**Target Audience:** New to machine learning, want focused learning path  
**Duration:** 20-30 hours  
**Problem Type:** Binary classification (bike available: yes/no)  
**Use Case:** Short-term commuter predictions (2-4 hours ahead)

### Complete Module Sequence

```
Module 1: Introduction (30-45 min)
    ↓
Module 2: Data Acquisition (1-2 hrs)
    ↓
Module 3: EDA & Pattern Analysis (1.5-2.5 hrs)
    ↓  [DECISION: Choose Track A]
    ↓
Module 4A: Feature Engineering for Classification (1.5-2 hrs)
    │   - Time-based features (hour, day, is_peak)
    │   - Weather features (current conditions)
    │   - Train schedule integration
    ↓
Module 5A: Classification Modeling (2-2.5 hrs)
    │   - Logistic Regression baseline
    │   - Random Forest Classifier
    │   - XGBoost Classifier
    │   - Classification metrics
    ↓
Module 6: Model Validation (1.5-2 hrs)
    │   - Focus on classification validation
    ↓
Module 7: Visualization & Communication (1.5-2 hrs)
    │   - Classification dashboards
    ↓
Module 8: Automation & Reproducibility (1-2 hrs)
    ↓
Module 9: Experimentation (1-1.5 hrs)
    ↓
Module 10: Collaboration & Reporting (30-60 min)
    ↓
Module 11: Capstone Project - Track A (2-3 hrs)
    │   - Complete classification pipeline
    │   - Binary prediction dashboard
    │   - Commuter-focused report
    ↓
  ✅ COMPLETE
```

### Learning Milestones

| Milestone | Achievement | Module |
|-----------|------------|--------|
| 🎯 **Setup Complete** | Environment configured, data accessed | M1-M2 |
| 📊 **Data Explored** | Understand patterns, make track decision | M3 |
| 🔧 **Features Built** | Created 5+ classification features | M4A |
| 🤖 **Model Trained** | 3 classifiers trained and evaluated | M5A |
| 📈 **Model Validated** | Cross-validation, MLflow tracking | M6 |
| 📺 **Dashboard Built** | Interactive Streamlit app | M7 |
| 🔄 **Pipeline Automated** | End-to-end reproducible workflow | M8 |
| 🎓 **Capstone Done** | Portfolio-ready project | M11 |

### Skills Acquired (Track A)

**Data Science:**
- ✅ API data fetching and integration
- ✅ Exploratory data analysis
- ✅ Feature engineering for classification
- ✅ Binary classification modeling
- ✅ Model evaluation (accuracy, precision, recall, F1)
- ✅ Cross-validation and experiment tracking

**Tools & Technologies:**
- ✅ Python, Pandas, NumPy
- ✅ Scikit-learn (preprocessing, classification)
- ✅ Matplotlib, Seaborn, Plotly
- ✅ Streamlit (dashboards)
- ✅ MLflow (experiment tracking)
- ✅ Google Colab, GitHub

**Domain Knowledge:**
- ✅ Bike-sharing systems
- ✅ Commuter behavior patterns
- ✅ Short-term prediction strategies

---

## 📗 Track B: Advanced Path (Regression + Time Series)

**Target Audience:** Have ML fundamentals, want comprehensive experience  
**Duration:** 30-45 hours (includes all Track A content + Track B additions)  
**Problem Types:** Classification + Regression + Time series  
**Use Cases:** Commuter predictions + Multi-day tourist forecasting

### Complete Module Sequence

```
Module 1: Introduction (30-45 min)
    ↓
Module 2: Data Acquisition (1-2 hrs)
    ↓
Module 3: EDA & Pattern Analysis (1.5-2.5 hrs)
    ↓  [DECISION: Choose Both Tracks]
    ↓
Module 4A: Feature Engineering for Classification (1.5-2 hrs)
    │   [Same as Track A]
    ↓
Module 4B: Advanced Feature Engineering (1.5-2 hrs) ⭐ NEW
    │   - Extended temporal features (holidays, long weekends)
    │   - Weather forecasts (3-day ahead)
    │   - Event calendar integration
    │   - Tourist attraction proximity
    │   - Multi-period lag features
    ↓
Module 5A: Classification Modeling (2-2.5 hrs)
    │   [Same as Track A]
    ↓
Module 5B: Regression & Time Series Modeling (2.5-3 hrs) ⭐ NEW
    │   - Linear/Ridge Regression
    │   - Random Forest Regressor
    │   - Gradient Boosting (XGBoost)
    │   - Time series models (ARIMA, Prophet)
    │   - Optional: LSTM basics
    │   - Uncertainty quantification
    ↓
Module 6: Model Validation (1.5-2 hrs)
    │   - Classification + Regression validation
    │   - Model comparison
    ↓
Module 7: Visualization & Communication (1.5-2 hrs)
    │   - Classification + Regression dashboards
    │   - Time series forecasts with intervals
    ↓
Module 8: Automation & Reproducibility (1-2 hrs)
    │   - Both pipeline types
    ↓
Module 9: Experimentation (1-1.5 hrs)
    │   - Cross-track comparison
    ↓
Module 10: Collaboration & Reporting (30-60 min)
    ↓
Module 11: Capstone Project - Both Tracks (3-4 hrs) ⭐ COMPREHENSIVE
    │   - Classification pipeline
    │   - Regression pipeline
    │   - Time series forecasts
    │   - Comparative dashboard
    │   - Recommendation engine
    │   - Comprehensive report
    ↓
  ✅ COMPLETE (Advanced)
```

### Learning Milestones

| Milestone | Achievement | Module |
|-----------|------------|--------|
| 🎯 **Setup Complete** | Environment configured, data accessed | M1-M2 |
| 📊 **Data Explored** | Understand patterns, choose both tracks | M3 |
| 🔧 **Classification Features** | Created 5+ features | M4A |
| 🔧 **Regression Features** | Created 15+ features total | M4B ⭐ |
| 🤖 **Classification Models** | 3 classifiers trained | M5A |
| 🤖 **Regression Models** | 4+ regression models trained | M5B ⭐ |
| 📈 **All Models Validated** | Complete validation strategy | M6 |
| 📺 **Advanced Dashboards** | Multi-model dashboards | M7 |
| 🔄 **Complex Pipeline** | Both pipelines automated | M8 |
| 🎓 **Comprehensive Capstone** | Advanced portfolio project | M11 ⭐ |

### Skills Acquired (Track B — Includes All Track A + Below)

**Advanced Data Science:**
- ⭐ Regression modeling (linear, tree-based, ensemble)
- ⭐ Time series forecasting (ARIMA, Prophet, LSTM)
- ⭐ Multi-step ahead predictions
- ⭐ Uncertainty quantification (confidence intervals, prediction intervals)
- ⭐ Long-term forecasting strategies
- ⭐ Model comparison (classification vs regression trade-offs)

**Advanced Tools:**
- ⭐ Statsmodels (ARIMA, statistical tests)
- ⭐ Prophet (Facebook's forecasting library)
- ⭐ Optional: TensorFlow/PyTorch (LSTM)

**Advanced Domain Knowledge:**
- ⭐ Tourist behavior patterns
- ⭐ Event impact on demand
- ⭐ Multi-day forecasting strategies

---

## 🧭 Self-Assessment Guide

### Before Starting (Module 1)

**Answer these questions to gauge your readiness:**

1. **Can you write Python functions and use loops?**
   - ✅ Yes → Continue
   - ❌ No → Complete Python fundamentals first

2. **Are you comfortable with Pandas DataFrames?**
   - ✅ Yes → Continue
   - ❌ No → Complete Pandas tutorial first

3. **Have you trained a machine learning model before?**
   - ✅ Yes → Consider Track B
   - ❌ No → Track A is perfect for you

4. **Do you understand concepts like overfitting, train/test split, and evaluation metrics?**
   - ✅ Yes → Track B recommended
   - ❌ No → Track A recommended

5. **How much time do you have?**
   - 20-30 hours → Track A
   - 30-45 hours → Track B

---

### At Decision Point (End of Module 3)

**After exploring the data, ask yourself:**

1. **Am I interested in binary predictions (yes/no) or continuous predictions (counts)?**
   - Binary → Track A
   - Both/Counts → Track B

2. **Do I want to learn time series forecasting?**
   - Not yet → Track A
   - Yes → Track B

3. **Am I comfortable with the pace so far?**
   - Yes, manageable → Can handle Track B
   - Challenging → Stick with Track A

4. **Do I want a comprehensive portfolio project?**
   - Standard is fine → Track A
   - Comprehensive → Track B

---

## 🔄 Flexible Learning: You Can Always Come Back!

**Important:** Your track choice is **not permanent**. The course is designed for flexible learning:

- ✅ **Start with Track A** → Come back later for Track B modules
- ✅ **Complete Track B** → You automatically have Track A
- ✅ **Switch mid-course** → Modules 4B and 5B are self-contained

**Recommendation:** If unsure, start with Track A to build confidence, then return for Track B.

---

## 📊 Comparison Table: Track A vs Track B

| Aspect | Track A | Track B |
|--------|---------|---------|
| **Duration** | 20-30 hrs | 30-45 hrs |
| **Difficulty** | Beginner | Advanced |
| **Prerequisites** | Python basics | Python + ML fundamentals |
| **Modules** | 1-3, 4A, 5A, 6-11 | 1-3, 4A, 4B, 5A, 5B, 6-11 |
| **Model Types** | Classification (3) | Classification + Regression + TS (7+) |
| **Prediction Horizon** | 2-4 hours | 2-4 hours + 1-3 days |
| **Use Cases** | Commuter | Commuter + Tourist |
| **Features** | 5-10 | 15-25 |
| **Capstone** | Standard | Advanced/Comprehensive |
| **Portfolio Impact** | Good | Excellent |

---

## 🎯 Recommended Learning Strategies

### Strategy 1: Beginner Path (Track A Only)
**Best for:** New to ML, limited time  
**Approach:** Focus on mastering classification thoroughly  
**Timeline:** 20-30 hours over 4-6 weeks

```
Week 1-2: Modules 1-3 (Foundation)
Week 3: Module 4A-5A (Classification)
Week 4-5: Modules 6-10 (Integration)
Week 6: Module 11 (Capstone)
```

---

### Strategy 2: Sequential Path (Track A → Track B)
**Best for:** Want both, prefer step-by-step  
**Approach:** Complete Track A, then add Track B later  
**Timeline:** 20-30 hours (Track A), then 10-15 hours (Track B additions)

```
Phase 1: Complete Track A (4-6 weeks)
Break: Apply skills, build confidence
Phase 2: Return for Track B (2-3 weeks)
```

---

### Strategy 3: Comprehensive Path (Both Tracks)
**Best for:** Have ML experience, want full experience  
**Approach:** Complete both tracks in one go  
**Timeline:** 30-45 hours over 6-10 weeks

```
Week 1-2: Modules 1-3 (Foundation)
Week 3-4: Modules 4A, 4B (All Features)
Week 5-6: Modules 5A, 5B (All Models)
Week 7-8: Modules 6-10 (Integration + Comparison)
Week 9-10: Module 11 (Comprehensive Capstone)
```

---

## 🚀 Next Steps

1. **Start Module 1** — Get introduced to both tracks
2. **Complete Modules 2-3** — Build foundation, explore data
3. **Make your decision** — End of Module 3 (use this guide + use case comparison)
4. **Commit to your path** — Or do both!
5. **Complete capstone** — Build portfolio-ready project

---

## 🔗 Related Documents

- **[Use Case Comparison](use_case_comparison.md)** — Detailed comparison of commuter vs tourist prediction
- **[OV-fiets System Overview](ov_fiets_system_overview.md)** — Understand the domain
- **[Course Structure](course_structure_dual_track.md)** — Full module-by-module breakdown

---

## 💬 Still Have Questions?

**Common Questions:**

**Q: Can I switch tracks mid-course?**  
A: Yes! Modules 4B and 5B are self-contained. You can complete Track A first, then come back.

**Q: Which track is better for my resume?**  
A: Track B (both) is more comprehensive, but Track A is perfectly portfolio-worthy. Choose based on your time and interest.

**Q: What if I get stuck on Track B?**  
A: You can always fall back to Track A. Every learner completes at least Track A.

**Q: Can I skip Track A and do only Track B?**  
A: Not recommended. Track B builds on Track A concepts. Do Track A first (or at minimum, have equivalent ML experience).

---

**Document Maintainer:** Course Development Team  
**Last Updated:** January 18, 2026

---

**🎓 Ready to start? Head to Module 1!**
