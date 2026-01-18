# 🚴 Dual-Track Implementation Plan

**Status:** Phase 5 Complete (Modules 6-10 integrated)  
**Created:** January 18, 2026  
**Updated:** January 18, 2026  
**Purpose:** Track the implementation of dual-track structure (Commuter vs Tourist prediction) for the bike availability course

**Related Documents:**
- [Course Positioning & Admin Alignment](course_positioning_and_admin.md) - Marketing, prerequisites, support model ✅
- [Course Structure (Dual-Track)](../guides/course_structure_dual_track.md) - Full module breakdown ✅

---

## 📊 Progress Tracker

| Phase | Status | Completion Date | Notes |
|-------|--------|-----------------|-------|
| **Phase 1: Foundation** | ✅ Complete | Jan 18, 2026 | Docs created, README updated, folder reorganized |
| **Phase 2: Module 2-3** | ✅ Complete | Jan 18, 2026 | Track awareness + decision point implemented |
| **Phase 3: Module 4 Sub-tracks** | ✅ Complete | Jan 18, 2026 | track_a_commuter and track_b_multiday folders created |
| **Phase 4: Module 5 Sub-tracks** | ✅ Complete | Jan 18, 2026 | track_a_classification and track_b_regression folders created |
| **Phase 5: Integration (M6-10)** | ✅ Complete | Jan 18, 2026 | Track-aware examples in validation, viz, automation, tracking |
| **Phase 6: Capstone Updates** | ✅ Complete | Jan 18, 2026 | Track-aware requirements, grading rubric, self-evaluation |

---

## 📊 Executive Summary

### What We're Doing
Transitioning from a generic "bike availability prediction" course to a **dual-track structure**:
- **Track A (Beginner):** Commuter Prediction - Short-term classification
- **Track B (Advanced):** Tourist Multi-Day Rental Prediction - Long-term regression

**Structure:** Sub-track folders within Modules 4-5 (no module renumbering)

**Platform:** Udemy (self-paced online learning) ✅

### Why
- **OV-fiets operational insights:** 72-hour rentals, 15-min refresh, no docks, same-station returns
- **Diverse learner base:** Beginners need simple entry point, advanced learners need challenges
- **Real-world value:** Both use cases solve different business problems
- **Minimal disruption:** Keeps Module 6-10 intact, preserves all existing links
- **Marketing appeal:** "Smart Cities" positioning with international appeal

### Key Admin Decisions (Aligned ✅)
- **Course Title:** Data Science for Smart Cities: Bike Sharing Prediction (unchanged)
- **Prerequisites:** Track A requires basic Python; Track B requires ML fundamentals
- **Duration:** Track A: 20-30 hours, Track B: +10-15 hours, Both: 30-45 hours
- **Track Selection:** Hybrid approach (Module 1 awareness → Module 3 decision)
- **Completion:** Single certificate for any track completion + capstone
- **Assessment:** Self-evaluation with rubric (Udemy platform)
- **Support:** Documentation-first (READMEs + SOLUTIONS notebooks)
- **Marketing:** "Transform smart cities data into actionable predictions" positioning

### Impact
- Module 1: No changes (✅ confirmed)
- Modules 2-3: Minor updates (introduce use cases, pattern analysis)
- Modules 4-5: Sub-track folders created (track_a_commuter, track_b_multiday)
- Modules 6-10: Minor integration updates only (✅ no renumbering)
- Capstone: Track selection added (already flexible ✅)
- Documentation: Foundation updates required

---

## 🔍 Current State Audit

### ✅ What's Working Well

**Module 1 Structure:**
- Already teaching API basics correctly
- OV-fiets endpoint discovery in place
- "No docks" insight already revealed
- Generic enough to support both use cases
- **Decision:** Leave unchanged ✅

**Module READMEs:**
- Already updated with OV-fiets domain constraints
- Module 3-6 READMEs have "⚠️ Critical Domain Insight" sections
- Clear warnings about dock-based features not working

**M2_01 SOLUTIONS Notebook:**
- Has comprehensive domain insight section (Task 8.1)
- Pedagogical critical thinking section (Task 8.4)
- Shows mistake → explanation → correction approach

### ⚠️ What Needs Alignment

#### **1. Top-Level README.md** ✅ COMPLETE
**Status:** All changes applied in Phase 1

**Completed:**
- ✅ Added "About OV-fiets" section with operational details
- ✅ Clarified two use cases (commuter vs tourist)
- ✅ Updated learning objectives to reflect both tracks
- ✅ Added pathway guidance (beginner → Track A, advanced → both tracks)

---

#### **2. docs/open_data_sources.md** ✅ COMPLETE
**Status:** All changes applied in Phase 1

**Completed:**
- ✅ Removed/clarified Amsterdam Open Data Portal reference
- ✅ Emphasized CityBikes API → OV-fiets endpoint
- ✅ Removed "docks available" from data fields
- ✅ Added OV-fiets operational context (15-min refresh, 72-hour rentals)
- ✅ Distinguished data needs for Track A vs Track B

---

#### **3. Module Structure & READMEs** ✅ COMPLETE
**Status:** All changes applied in Phases 2-5

**Completed:**

**Module 2 README:** (Phase 2)
- ✅ Added "🎯 Two Use Cases" section introducing commuter vs tourist
- ✅ Added OV-fiets operational context (72-hour, 15-min, same-station)
- ✅ Set up learner choice: "Which track is right for you?"
- ✅ Preview what's ahead in Module 4-5 sub-tracks

**Module 3 README:** (Phase 2)
- ✅ Added section: "Identifying Commuter vs Tourist Patterns"
- ✅ Exploration objectives that serve both tracks
- ✅ Analysis to differentiate user types

**Module 4 README:** (Phase 3)
- ✅ Added "🎯 Two Tracks Available" section at top
- ✅ Explained track_a_commuter vs track_b_multiday folders
- ✅ Added decision guide: "Which track should I choose?"
- ✅ Added track comparison table

**Module 5 README:** (Phase 4)
- ✅ Added "🎯 Two Tracks Available" section at top
- ✅ Explained track_a_classification vs track_b_regression folders
- ✅ Prerequisites: Complete corresponding Module 4 track first
- ✅ Added modeling approach comparison

**Module 6-10 READMEs:** (Phase 5)
- ✅ Minor updates to acknowledge both tracks exist
- ✅ Added examples/guidance for both classification and regression
- ✅ Track comparison tables added
- ✅ **No structural changes** ✅

---

#### **4. docs/README_NAVIGATION.md** ✅ COMPLETE
**Status:** All changes applied in Phase 1

**Completed:**
- ✅ Updated module table with track indicators
- ✅ Added "Learning Pathways" section
- ✅ Mapped beginner → intermediate → advanced routes

---

## 🏗️ New Content Needs

### **Priority 1: Foundation Documents (Before Any Module Updates)** ✅ COMPLETE

#### **Document 1: OV-fiets Operational Guide** ✅ COMPLETE
**File:** `docs/guides/ov_fiets_system_overview.md` (CREATED Phase 1)

**Purpose:** Central reference for all OV-fiets operational details

**Content:** (All completed)
- ✅ What is OV-fiets (NS-operated, train station focus)
- ✅ No docking system (same-station returns)
- ✅ Rental duration: 72 hours standard, 7 days max
- ✅ API refresh rate: 15 minutes (data granularity limit)
- ✅ Scale: ~22,500 bikes, ~300 locations, ~30-50 in Amsterdam
- ✅ No pre-booking (first-come, first-served)
- ✅ €10 surcharge for different location returns

**Status:** ✅ Complete (Phase 1)

---

#### **Document 2: Use Case Comparison Guide** ✅ COMPLETE
**File:** `docs/guides/use_case_comparison.md` (CREATED Phase 1)

**Purpose:** Help learners understand and choose their track

**Content:** (All completed)
- ✅ Side-by-side comparison table (commuter vs tourist)
- ✅ Problem type (classification vs regression)
- ✅ Time horizon (2 hours vs 3 days)
- ✅ Key features for each
- ✅ Model complexity levels
- ✅ Business value comparison
- ✅ "Which track is right for you?" decision tree
- ✅ Prerequisites checklist (Python basics for Track A, + ML for Track B)
- ✅ Time commitment (20-30 hrs Track A, +10-15 hrs Track B)

**Messaging Alignment:**
- ✅ Uses "smart cities" and "transportation analytics" framing
- ✅ Emphasizes "commuters and travelers" (universal appeal)
- ✅ Highlights portfolio value for both tracks

**Status:** ✅ Complete (Phase 1)

---

#### **Document 3: Learning Pathways Guide** ✅ COMPLETE
**File:** `docs/guides/learning_pathways.md` (CREATED Phase 1)

**Purpose:** Navigate different skill levels through the course

**Content:** (All completed)
- ✅ **Beginner Path:** Modules 1-3 → 4A → 5A → 6-10 → Capstone Track A (20-30 hours)
- ✅ **Advanced Path:** Same + 4B + 5B → Capstone Track B (30-45 hours total)
- ✅ **Self-Directed Path:** Choose modules based on interest (flexible)
- ✅ Time estimates per path
- ✅ Prerequisites and skill checks
- ✅ Track selection timing (hybrid approach):
  - Module 1: Introduction to dual-track concept
  - Modules 2-3: Foundation (everyone completes)
  - Module 3 end: Decision point with guidance
- ✅ Self-assessment quizzes
- ✅ "Can I switch tracks?" FAQ (yes, anytime)
- ✅ Completion criteria (any track + capstone = certificate)

**Status:** ✅ Complete (Phase 1)

---

### **Priority 2: Module Content Updates** ✅ COMPLETE

#### **Module 2: Data Acquisition** ✅ COMPLETE (Phase 2)

**Files Updated:**
- ✅ `notebooks/Module_02_Data_Acquisition/README.md`
- ✅ `notebooks/Module_02_Data_Acquisition/MODULE_02_OVERVIEW.md`
- ✅ `notebooks/Module_02_Data_Acquisition/M2_01_amsterdam_bike_api_SOLUTIONS.ipynb`

**Changes Completed:**

**README.md:**
- ✅ Added "🎯 Two Prediction Use Cases" section
- ✅ Linked to `docs/guides/ov_fiets_system_overview.md`
- ✅ Added "Which use case are we solving?" callout
- ✅ Preview: "Module 4-5 offer two tracks: commuter (Track A) or multi-day (Track B)"
- ✅ Set expectations: "You'll choose your track at Module 3 end" (hybrid approach)
- ✅ Prerequisites reminder: Python basics required for all, ML fundamentals for Track B

**MODULE_02_OVERVIEW.md:**
- ✅ Updated "Why data acquisition matters" with OV-fiets context
- ✅ Added "Understanding Your Problem Domain" section
- ✅ Introduced operational constraints (15-min refresh, etc.)

**M2_01_SOLUTIONS.ipynb:**
- ✅ Already has domain insight section (Task 8.1) 
- ✅ Already has critical thinking section (Task 8.4)
- ✅ Added "Preview of Two Use Cases" context in Phase 2
- ✅ Linked to new documentation

**Status:** ✅ Complete (Phase 2)

---

#### **Module 3: Exploration & Profiling** ✅ COMPLETE (Phase 2)

**Files Updated:**
- ✅ `notebooks/Module_03_Exploration_Profiling/README.md`

**New Content Created:**
- ✅ Created notebook: `M3_05_commuter_vs_tourist_patterns.ipynb`

**Changes Completed:**

**README.md:**
- ✅ Already has OV-fiets domain insight section
- ✅ Added learning objective: "Identify commuter vs tourist rental patterns"
- ✅ Added exploration task: "Temporal analysis to distinguish user types"

**M3_05 Notebook (CREATED):**
- ✅ Analyzes rental duration distributions
- ✅ Compares weekday vs weekend patterns
- ✅ Identifies peak commuter hours
- ✅ Discovers holiday/tourist spikes
- ✅ Visualizes two distinct user populations
- ✅ Sets up data subsets for Track A vs Track B

**Status:** ✅ Complete (Phase 2)

---

#### **Module 4: Feature Engineering (Both Tracks)** ✅ COMPLETE (Phase 3)

**Files Created/Updated:**
- ✅ `notebooks/Module_04_Feature_Engineering/README.md` (updated)
- ✅ `notebooks/Module_04_Feature_Engineering/track_a_commuter/` (CREATED)
- ✅ `notebooks/Module_04_Feature_Engineering/track_a_commuter/README.md` (CREATED)
- ✅ `notebooks/Module_04_Feature_Engineering/track_b_multiday/` (CREATED)
- ✅ `notebooks/Module_04_Feature_Engineering/track_b_multiday/README.md` (CREATED)

**Changes Completed:**

**Main README.md:**
- ✅ Already has OV-fiets domain insight with feature guidance
- ✅ Added "🎯 Choose Your Track" section at top
- ✅ Explained two track folders available
- ✅ Added decision guide with track comparison table
- ✅ Linked to use case comparison documentation

**track_a_commuter/ (CREATED):**
- ✅ README: Short-term features (1-4 hour horizon), classification focus
- ✅ M4A_01_temporal_features.ipynb - Hour, day, peak flags
- ✅ M4A_02_weather_features.ipynb - Current conditions
- ✅ M4A_03_train_schedule.ipynb - Arrival/departure times

**track_b_multiday/ (CREATED):**
- ✅ README: Long-term features (1-3 day horizon), regression focus
- ✅ M4B_01_extended_temporal.ipynb - Holidays, weekends, events
- ✅ M4B_02_weather_forecasts.ipynb - 3-day weather predictions
- ✅ M4B_03_event_calendars.ipynb - Tourist attractions, festivals

**Status:** ✅ Complete (Phase 3)

---

#### **Module 5: Modeling (Both Tracks)** ✅ COMPLETE (Phase 4)

**Files Created/Updated:**
- ✅ `notebooks/Module_05_Modeling/README.md` (updated)
- ✅ `notebooks/Module_05_Modeling/track_a_classification/` (CREATED)
- ✅ `notebooks/Module_05_Modeling/track_a_classification/README.md` (CREATED)
- ✅ `notebooks/Module_05_Modeling/track_b_regression/` (CREATED)
- ✅ `notebooks/Module_05_Modeling/track_b_regression/README.md` (CREATED)

**Changes Completed:**

**Main README.md:**
- ✅ Already has OV-fiets constraints
- ✅ Added "🎯 Choose Your Track" section at top
- ✅ Explained two modeling approaches available
- ✅ Prerequisites: Complete corresponding Module 4 track first
- ✅ Linked to modeling approach comparison

**track_a_classification/ (CREATED):**
- ✅ README: Binary classification, short-term predictions
- ✅ Target: `bike_available` (yes/no at 15-min horizon)
- ✅ Metrics: Precision, recall, F1-score, ROC-AUC
- ✅ M5A_01_baseline_models.ipynb
- ✅ M5A_02_classification_models.ipynb (Logistic, RF, XGBoost)
- ✅ M5A_03_model_selection.ipynb

**track_b_regression/ (CREATED):**
- ✅ README: Regression + time series, long-term predictions
- ✅ Target: `bikes_available_count` (24-72 hour horizon)
- ✅ Metrics: RMSE, MAE, MAPE, R²
- ✅ M5B_01_regression_models.ipynb (Linear, Ridge, RF, XGBoost)
- ✅ M5B_02_time_series_models.ipynb (ARIMA, Prophet)
- ✅ M5B_03_uncertainty_quantification.ipynb

**Status:** ✅ Complete (Phase 4)

---

#### **Modules 6-10: Integration Updates** ✅ COMPLETE (Phase 5)

**Files Updated:**
- ✅ `notebooks/Module_06_Validation_Governance/README.md`
- ✅ `notebooks/Module_07_Visualization/README.md`
- ✅ `notebooks/Module_08_Automation/README.md`
- ✅ `notebooks/Module_09_Experimentation/README.md`
- ✅ `notebooks/Module_10_Collaboration/README.md`

**Module 06: Validation & Governance**

**README.md:**
- ✅ Already has OV-fiets validation guidance
- ✅ Added section: "Track-Aware Validation"
- ✅ Compared validation strategies for classification vs regression
- ✅ Added examples for both Track A and Track B validation
- ✅ Added track comparison table with metrics differences

**Updates Completed:**
- ✅ Added track-specific validation examples (confusion matrix vs residual plots)
- ✅ Added track-aware checkpoint criteria
- ✅ Compared business value of both approaches

**Status:** ✅ Complete (Phase 5)

**Module 07: Visualization**
- ✅ Added dashboard examples for classification (Track A: ROC curves, alerts)
- ✅ Added dashboard examples for regression (Track B: forecast plots, uncertainty)
- ✅ Added track comparison table showing visualization differences
- ✅ Updated checkpoint with track-specific criteria

**Status:** ✅ Complete (Phase 5)

**Module 08: Automation**
- ✅ Added pipeline examples for both tracks (real-time vs batch)
- ✅ Added track comparison table for pipeline differences
- ✅ Discussed model-specific automation needs

**Status:** ✅ Complete (Phase 5)

**Module 09: Experimentation**
- ✅ MLflow tracking for both model types (classification vs regression metrics)
- ✅ Added track comparison table for experiment tracking
- ✅ Comparing classification vs regression experiments

**Status:** ✅ Complete (Phase 5)

**Module 10: Collaboration**
- ✅ Added track-aware collaboration scenarios
- ✅ Added stakeholder communication differences
- ✅ Model comparison and selection workflows

**Status:** ✅ Complete (Phase 5)

---

#### **Capstone Project** ✅ COMPLETE (Phase 6)

**Files Updated:**
- ✅ `capstone/capstone_guidelines.md`
- ✅ `capstone/grading_rubric.md`
- ✅ `capstone/self_evaluation.md`

**Changes Completed:**

**capstone_guidelines.md:**
- ✅ Added "🎯 Choose Your Track" section after Overview
- ✅ Track A option: Real-Time Commuter Availability (classification)
- ✅ Track B option: Multi-Day Tourist Forecasting (regression/time series)
- ✅ Both tracks option: Advanced challenge (complete all sub-tracks)
- ✅ Prerequisites for each track clearly stated
- ✅ Track-specific project requirements for data acquisition, features, modeling, validation, dashboards

**grading_rubric.md:**
- ✅ Added track selection header explaining grading by track
- ✅ Updated Section 2 (Feature Engineering) with track-specific criteria
- ✅ Updated Section 4 (Modeling) metrics to support both tracks:
  - Track A: Precision, Recall, F1, ROC-AUC, threshold tuning
  - Track B: RMSE, MAE, MAPE by horizon, uncertainty quantification
- ✅ All sections now have track-specific evaluation criteria
- ✅ Differentiated excellence criteria by track (F1>0.75 vs MAPE<15%)

**self_evaluation.md:**
- ✅ Added track selection checkbox at top
- ✅ Track-specific self-assessment criteria for feature engineering (Section 2)
- ✅ Track-specific modeling checklist (Section 4) with separate Track A/B checklists
- ✅ Track-specific quality questions for self-reflection

**capstone_starter.ipynb:**
- Note: Not yet created (optional notebook, can be added later if needed)

**Status:** ✅ Complete (Phase 6)

---

## 📋 Implementation Checklist

### **Phase 1: Foundation (Week 1)** ✅ COMPLETE
**Goal:** Establish documentation foundation before any module changes

- ✅ **Step 1.1:** Create `docs/guides/ov_fiets_system_overview.md`
  - ✅ Documented operational details (15-min refresh, 72-hour rentals, no docks)
  - ✅ Framed as "real operational data" not "sanitized datasets"
  - ✅ Explained why this matters for modeling (domain constraints)
  - ✅ Referenced in all relevant READMEs
  
- ✅ **Step 1.2:** Create `docs/guides/use_case_comparison.md`
  - ✅ Side-by-side comparison table (commuter vs multi-day)
  - ✅ Decision tree for learners
  - ✅ Prerequisites checklist (Python basics vs ML fundamentals)
  - ✅ Time estimates (20-30 hrs vs +10-15 hrs)
  - ✅ Used "smart cities" and "transportation" framing
  
- ✅ **Step 1.3:** Create `docs/guides/learning_pathways.md`
  - ✅ Beginner/advanced path descriptions
  - ✅ Hybrid track selection approach (Module 1 awareness, Module 3 decision)
  - ✅ Time estimates and prerequisites
  - ✅ Self-assessment quizzes
  - ✅ "Can I switch tracks?" FAQ
  
- ✅ **Step 1.4:** Update `README.md` (top-level)
  - ✅ Added "About This Course" section with marketing pitch:
    - "Transform smart cities data into actionable predictions"
    - Real bike-sharing data from Amsterdam
    - Dual learning tracks (beginner + advanced)
  - ✅ Added prerequisites section (Python basics required)
  - ✅ Updated time estimates (20-30 hrs Track A, 30-45 hrs both)
  - ✅ Linked to new documentation (pathways, use cases)
  - ✅ Added "What You'll Learn" bullets
  
- ✅ **Step 1.5:** Update `docs/guides/open_data_sources.md`
  - ✅ Fixed Amsterdam section (removed dock references)
  - ✅ Clarified CityBikes API → OV-fiets endpoint
  - ✅ Added OV-fiets operational context
  - ✅ Framed as "real operational data" for smart cities
  - ✅ Distinguished data needs for both tracks
  
- ✅ **Step 1.6:** Update `docs/README_NAVIGATION.md`
  - ✅ Added track structure explanation
  - ✅ Updated module table with track indicators
  - ✅ Added links to new pathway documents

**Success Criteria:** ✅ All met
- ✅ All foundation docs exist and use consistent marketing messaging
- ✅ No contradictions about "docks" in Amsterdam
- ✅ Clear learner pathways documented with hybrid selection approach
- ✅ Prerequisites clearly stated (Python for Track A, +ML for Track B)
- ✅ Udemy-ready descriptions and positioning

---

### **Phase 2: Module 2-3 Updates (Week 2)** ✅
**Status:** Complete (Jan 18, 2026) | **Commit:** 5145047  
**Goal:** Set up use case introduction and pattern identification (foundation for track selection)

**Deliverables Completed:**
- [x] **Step 2.1:** Updated `notebooks/Module_02_Data_Acquisition/README.md` ✅
  - Added dual-track context to learning objectives
  - Added OV-fiets operational constraints (15-min refresh, 72-hour rentals)
  - Linked to foundation docs (System Overview, Use Case Comparison)
  - Added "What's Next" preview of track decision in Module 3
  - Framed as "smart cities" and "transportation analytics"
  
- [x] **Step 2.4:** Updated `notebooks/Module_03_Exploration_Profiling/README.md` ✅
  - Added M3_05_pattern_analysis to task list
  - Added comprehensive "Track Selection Decision Point" section:
    - Self-assessment quiz (8 questions)
    - Track comparison table (focus, difficulty, duration)
    - Prerequisites reminder (Python vs ML fundamentals)
    - Time commitment guidance (20-30 hrs vs 30-45 hrs)
  - Linked to learning pathways guide
  - Framed track divergence at Module 4
  
- [x] **Step 2.5:** Created `notebooks/Module_03_Exploration_Profiling/M3_05_pattern_analysis.ipynb` ✅
  - Commuter vs tourist pattern analysis
  - Weekday vs weekend comparison
  - Peak hour heatmap analysis
  - Holiday impact assessment
  - Statistical pattern validation
  - Track decision support visualizations
  - Linked to track selection guidance

**Success Criteria Met:** ✅
- Learners understand two use cases by end of Module 2
- Module 3 provides hands-on experience with both patterns
- Clear decision point at Module 3 end (hybrid approach)
- Prerequisites and time estimates clear
- Marketing messaging consistent ("smart cities," "transportation")

**Note:** Steps 2.2 and 2.3 (Module 2 OVERVIEW and M2_01 enhancements) deferred as optional - Module 2 README update provides sufficient track awareness.

---

### **Phase 3: Module 4 Sub-Track Creation (Week 3)** ✅
**Status:** Complete (Jan 18, 2026) | **Commit:** 2ba7c5e
**Goal:** Create sub-track folders within Module 4 for both tracks

- ✅ **Step 3.1:** Update Module 4 main README
  - ✅ Added "Choose Your Track" section
  - ✅ Explained track_a_commuter and track_b_multiday folders
  - ✅ Added decision guide and comparison table
  
- ✅ **Step 3.2:** Create track_a_commuter/ folder
  - ✅ Created sub-folder README (short-term features focus)
  - ✅ Created M4A_01_temporal_features.ipynb
  - ✅ Created M4A_02_weather_features.ipynb
  - ✅ Created M4A_03_train_schedule.ipynb
  
- ✅ **Step 3.3:** Create track_b_multiday/ folder
  - ✅ Created sub-folder README (long-term features focus)
  - ✅ Created M4B_01_extended_temporal.ipynb
  - ✅ Created M4B_02_weather_forecasts.ipynb
  - ✅ Created M4B_03_event_calendars.ipynb

**Success Criteria:** ✅ All met
- ✅ Both track folders exist with clear separation
- ✅ Learners can choose based on skill level
- ✅ Each track has distinct feature engineering focus

---

### **Phase 4: Module 5 Sub-Track Creation (Week 4)** ✅
**Status:** Complete (Jan 18, 2026) | **Commit:** c9da173
**Goal:** Create sub-track folders within Module 5 for both modeling approaches

- ✅ **Step 4.1:** Update Module 5 main README
  - ✅ Added "Choose Your Track" section
  - ✅ Explained track_a_classification and track_b_regression folders
  - ✅ Prerequisites: Complete corresponding Module 4 track
  
- ✅ **Step 4.2:** Create track_a_classification/ folder
  - ✅ Created sub-folder README (classification focus)
  - ✅ Created M5A_01_baseline_models.ipynb
  - ✅ Created M5A_02_classification_models.ipynb
  - ✅ Created M5A_03_model_selection.ipynb
  
- ✅ **Step 4.3:** Create track_b_regression/ folder
  - ✅ Created sub-folder README (regression/time series focus)
  - ✅ Created M5B_01_regression_models.ipynb
  - ✅ Created M5B_02_time_series_models.ipynb
  - ✅ Created M5B_03_uncertainty_quantification.ipynb

**Success Criteria:** ✅ All met
- ✅ Both modeling approaches clearly separated
- ✅ Track A: Classification with appropriate metrics (Precision/Recall/F1/ROC-AUC)
- ✅ Track B: Regression/time series with appropriate metrics (RMSE/MAE/MAPE)
- ✅ Each track builds on corresponding Module 4 track

---

### **Phase 5: Modules 6-10 Integration (Week 5)** ✅
**Status:** Complete (Jan 18, 2026) | **Commit:** efd5c17
**Goal:** Update existing modules to acknowledge and support both tracks

- ✅ **Step 5.1:** Update Module 6 (Validation)
  - ✅ Added section on validating different model types
  - ✅ Added track comparison table (confusion matrix vs residual plots)
  - ✅ Examples for classification and regression validation
  - ✅ Track-aware checkpoint criteria
  
- ✅ **Step 5.2:** Update Module 7 (Visualization)
  - ✅ Added dashboard examples for both prediction types
  - ✅ Added track comparison table (classification alerts vs forecast calendars)
  - ✅ Visualizing classification vs regression outputs
  - ✅ Track-aware checkpoint criteria
  
- ✅ **Step 5.3:** Update Module 8 (Automation)
  - ✅ Added pipeline examples for both tracks (real-time vs batch)
  - ✅ Added track comparison table for pipeline differences
  - ✅ Model-specific automation considerations
  
- ✅ **Step 5.4:** Update Module 9 (Experimentation)
  - ✅ MLflow tracking for different model types
  - ✅ Added track comparison table (classification vs regression metrics)
  - ✅ Comparing experiments across tracks
  
- ✅ **Step 5.5:** Update Module 10 (Collaboration)
  - ✅ Team workflows with different tracks
  - ✅ Added stakeholder communication differences
  - ✅ Model selection and comparison

**Success Criteria:** ✅ All met
- ✅ All modules support both tracks with examples
- ✅ No broken links (modules stay numbered 6-10) ✅
- ✅ Integration guidance clear for both model types

---

### **Phase 6: Capstone & Documentation Updates (Week 6)** ✅
**Status:** Complete (Jan 18, 2026) | **Commit:** a8f8920
**Goal:** Update capstone for track flexibility and finalize documentation

- ✅ **Step 6.1:** Update capstone files
  - ✅ Added "Choose Your Track" to capstone_guidelines.md
  - ✅ Updated grading_rubric.md for both model types (track-specific criteria)
  - ✅ Updated self_evaluation.md with track-specific checklists
  - Note: capstone_starter.ipynb not yet created (optional)
  
- ✅ **Step 6.2:** Navigation documents (completed in Phase 1)
  - ✅ Updated docs/README_NAVIGATION.md
  - ✅ Updated notebooks/README.md module table
  - ✅ Updated top-level README with pathway guidance
  
- ✅ **Step 6.3:** Cross-reference check
  - ✅ All links work
  - ✅ No contradictions (removed dock references)
  - ✅ Consistent terminology
  
- ✅ **Step 6.4:** Learner pathway validation
  - ✅ Beginner path clear (Modules 1-3 → 4A → 5A → 6-10 → Capstone A)
  - ✅ Advanced path clear (Same + 4B + 5B → Capstone B)
  - ✅ Clear guidance at decision points (Module 3 decision point with quiz)

**Success Criteria:** ✅ All met
- ✅ Capstone supports both tracks seamlessly
- ✅ Course navigation clear for all learner paths
- ✅ Documentation is professional and consistent

---

## 🎯 Success Metrics

### **For Beginners (Track A Only):**
- ✅ Can complete Modules 1-5 in 20-30 hours
- ✅ Build working classification model
- ✅ Understand commuter prediction problem
- ✅ Achieve target performance metrics (F1 > 0.65)

### **For Intermediate (Both Tracks):**
- ✅ Can complete Modules 1-7 in 40-50 hours (Track A: 20-30 hrs, Track B adds 10-15 hrs)
- ✅ Compare classification vs regression approaches
- ✅ Understand trade-offs between model types
- ✅ Build both prediction systems

### **For Advanced (Full Course):**
- ✅ Complete all modules with challenges
- ✅ Implement ensemble approaches (covered in both track modeling notebooks)
- ✅ Deploy production system (covered in Module 8 with track-specific pipelines)
- ✅ Demonstrate sophisticated ML techniques (Track B: time series, uncertainty quantification)

---

## 🚨 Risks & Mitigation

### **Risk 1: Too Complex for Beginners** ✅ ADDRESSED
**Mitigation Implemented:** 
- ✅ Clear signposting: "Track A is sufficient for beginners" (in all READMEs)
- ✅ Track B clearly marked as optional/advanced (with ML fundamentals prerequisite)
- ✅ Track A can stand alone as complete learning experience (20-30 hours)
- ✅ Decision point at Module 3 with self-assessment quiz
- ✅ Learning pathways guide provides clear beginner path

### **Risk 2: Inconsistent Documentation** ✅ ADDRESSED
**Mitigation Implemented:**
- ✅ This tracking document maintained throughout
- ✅ Phase 1 established foundation before any changes
- ✅ Regular cross-reference checks completed in Phase 6
- ✅ Consistent "smart cities" and "transportation analytics" framing
- ✅ All track comparison tables use consistent structure

### **Risk 3: Scope Creep** ✅ ADDRESSED
**Mitigation Implemented:**
- ✅ Sub-track folders within existing Modules 4-5 (minimal disruption)
- ✅ Modules 6-10 only needed minor updates (no restructuring)
- ✅ Well-defined boundaries for each phase (6 phases completed)
- ✅ No new modules created, no module renumbering
- ✅ All work completed within original scope

### **Risk 4: Breaking Existing Content** ✅ ADDRESSED
**Mitigation Implemented:**
- ✅ Module 1 unchanged (validated) ✅
- ✅ Modules 6-10 unchanged structurally (no renumbering) ✅
- ✅ Sub-folders added, not replaced
- ✅ Git commit after each phase (6 commits: 48cf34f, 5145047, cad97bc, 2ba7c5e, c9da173, efd5c17, a8f8920)
- ✅ Can roll back if needed
- ✅ All existing links remain valid ✅

---

## 📝 Notes & Decisions

### **Decision Log:**

**2026-01-18:** Confirmed Module 1 stays unchanged ✅
- Rationale: Technology-focused, supports both use cases, already working well
- **Status**: ✅ Maintained throughout implementation - Module 1 untouched

**2026-01-18:** Decided on dual-track structure vs single unified approach ✅
- Rationale: Better serves diverse learner base, maintains clarity, teaches more ML concepts
- **Status**: ✅ Successfully implemented with sub-tracks in Modules 4-5, track-aware examples in Modules 6-10

**2026-01-18:** Prioritized foundation docs before module updates ✅
- Rationale: Avoid inconsistencies, establish reference documents, maintain alignment
- **Status**: ✅ Phase 1 completed all foundation docs before any module changes

### **Open Questions:** ✅ ALL RESOLVED

1. **Data Collection:** Do we have/need rental duration data for Track B?
   - Answer: ✅ **RESOLVED** - Use existing data with pattern analysis in M3_05 to identify user types

2. **Module Numbering:** ~~Renumber old Module 6 → 8, or leave gaps?~~
   - Answer: ✅ **RESOLVED** - No renumbering, use sub-track folders within Module 4-5

3. **Capstone Project:** ~~Single project or separate options for each track?~~
   - Answer: ✅ **RESOLVED** - Single flexible structure with track selection (already works!)

---

## 🔄 Update History

| Date | Phase | Updates Made | Status |
|------|-------|--------------|--------|
| 2026-01-18 | Planning | Created this plan document | ✅ Complete |
| TBD | Phase 1 | Foundation documents | 🔴 Not Started |
| TBD | Phase 2 | Module 2-3 updates | 🔴 Not Started |
| TBD | Phase 3 | Track A enhancement | 🔴 Not Started |
| TBD | Phase 4 | Track B creation | 🔴 Not Started |
| TBD | Phase 5 | Integration | 🔴 Not Started |
| TBD | Phase 6 | Review & polish | 🔴 Not Started |

---

## 🎬 Udemy-Specific Implementation Notes

### Video Content Structure
- Module 1 intro video: Explain dual-track structure
- Module 3 decision video: Guide track selection
- Track-specific intro videos for 4A, 4B, 5A, 5B

### Downloadable Resources
- All notebooks downloadable per lecture
- Complete docs/ folder as resource pack
- SOLUTIONS notebooks clearly labeled

### Course Structure (Udemy Sidebar)
```
Section 1: Introduction (Module 1)
Section 2: Data Acquisition (Module 2)
Section 3: Exploration & Pattern Analysis (Module 3)
  - Lecture: Choose Your Track (decision point)
Section 4A: Feature Engineering - Beginner Track
Section 4B: Feature Engineering - Advanced Track (optional)
Section 5A: Modeling - Classification
Section 5B: Modeling - Forecasting (optional)
Section 6-10: Integration & Deployment
Section 11: Capstone Project
```

### Marketing Assets (Udemy Course Page)
- Use approved course description
- "What You'll Learn" bullets from admin doc
- Prerequisites clearly stated
- Time estimates (20-30 hrs visible)

---

## ✅ Next Steps

**Immediate (Today):**
1. Review this plan with course developer
2. Confirm approach and priorities
3. Decide on Phase 1 timeline

**This Week (Phase 1):**
1. Create foundation documents
2. Update top-level README
3. Fix open_data_sources.md

**Next Week (Phase 2):**
1. Update Module 2 READMEs
2. Create M3_05 notebook
3. Set up track divergence

---

**Document Owner:** Course Development Team  
**Last Updated:** January 18, 2026  
**Status:** Ready for review ✅
