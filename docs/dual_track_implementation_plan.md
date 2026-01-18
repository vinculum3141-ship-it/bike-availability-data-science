# 🚴 Dual-Track Implementation Plan

**Status:** Planning  
**Created:** January 18, 2026  
**Updated:** January 18, 2026 (Admin alignment completed)  
**Purpose:** Track the implementation of dual-track structure (Commuter vs Tourist prediction) for the bike availability course

**Related Documents:**
- [Course Positioning & Admin Alignment](course_positioning_and_admin.md) - Marketing, prerequisites, support model ✅

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

#### **1. Top-Level README.md** 
**Current State:**
- Generic: "bike availability prediction"
- No mention of OV-fiets specifically
- No operational context
- No use case differentiation

**Issues:**
- Learners don't know WHAT they're building
- No business context or motivation
- Doesn't mention dual-track structure

**Needs:**
- [ ] Add "About OV-fiets" section with operational details
- [ ] Clarify two use cases (commuter vs tourist)
- [ ] Update learning objectives to reflect both tracks
- [ ] Add pathway guidance (beginner → Track A, advanced → both tracks)

---

#### **2. docs/open_data_sources.md**
**Current State:**
- References "Amsterdam Open Data Portal"
- Mentions "available docks" 
- Uses CityBikes API but doesn't clarify it's for OV-fiets

**Issues:**
- ❌ Implies Amsterdam has dock-based system (it doesn't!)
- Confusing: mentions "docks" when OV-fiets has none
- Doesn't explain OV-fiets operational characteristics

**Needs:**
- [ ] Remove/clarify Amsterdam Open Data Portal reference
- [ ] Emphasize CityBikes API → OV-fiets endpoint
- [ ] Remove "docks available" from data fields
- [ ] Add OV-fiets operational context (15-min refresh, 72-hour rentals)
- [ ] Distinguish data needs for Track A vs Track B

---

#### **3. Module Structure & READMEs**

**Current State:**
- Linear progression: Modules 1-10
- All modules treated as sequential
- No differentiation by skill level

**Issues:**
- Doesn't reflect beginner vs advanced pathways
- No clear point where tracks diverge
- Module 6+ content not yet defined for tourist prediction

**Needs:**

**Module 2 README:**
- [ ] Add "🎯 Two Use Cases" section introducing commuter vs tourist
- [ ] Add OV-fiets operational context (72-hour, 15-min, same-station)
- [ ] Set up learner choice: "Which track is right for you?"
- [ ] Preview what's ahead in Module 4-5 sub-tracks

**Module 3 README:**
- [ ] Add section: "Identifying Commuter vs Tourist Patterns"
- [ ] Exploration objectives that serve both tracks
- [ ] Analysis to differentiate user types

**Module 4 README:**
- [ ] Add "🎯 Two Tracks Available" section at top
- [ ] Explain track_a_commuter vs track_b_multiday folders
- [ ] Add decision guide: "Which track should I choose?"
- [ ] Link to use case comparison doc

**Module 5 README:**
- [ ] Add "🎯 Two Tracks Available" section at top
- [ ] Explain track_a_classification vs track_b_regression folders
- [ ] Prerequisites: Complete corresponding Module 4 track first
- [ ] Link to modeling approach comparison

**Module 6-10 READMEs:**
- [ ] Minor updates to acknowledge both tracks exist
- [ ] Add examples/guidance for both classification and regression
- [ ] Model comparison sections (where applicable)
- [ ] **No structural changes** ✅

---

#### **4. docs/README_NAVIGATION.md**
**Current State:**
- Documents 10 linear modules
- No mention of tracks or skill levels

**Needs:**
- [ ] Update module table with track indicators
- [ ] Add "Learning Pathways" section
- [ ] Map beginner → intermediate → advanced routes

---

## 🏗️ New Content Needs

### **Priority 1: Foundation Documents (Before Any Module Updates)**

#### **Document 1: OV-fiets Operational Guide**
**File:** `docs/ov_fiets_system_overview.md` (NEW)

**Purpose:** Central reference for all OV-fiets operational details

**Content:**
- What is OV-fiets (NS-operated, train station focus)
- No docking system (same-station returns)
- Rental duration: 72 hours standard, 7 days max
- API refresh rate: 15 minutes (data granularity limit)
- Scale: ~22,500 bikes, ~300 locations, ~30-50 in Amsterdam
- No pre-booking (first-come, first-served)
- €10 surcharge for different location returns

**Why First:** Every other document references this context

**Status:** 🔴 Not Started

---

#### **Document 2: Use Case Comparison Guide**
**File:** `docs/use_case_comparison.md` (NEW)

**Purpose:** Help learners understand and choose their track

**Content:**
- Side-by-side comparison table (commuter vs tourist)
- Problem type (classification vs regression)
- Time horizon (2 hours vs 3 days)
- Key features for each
- Model complexity levels
- Business value comparison
- "Which track is right for you?" decision tree
- Prerequisites checklist (Python basics for Track A, + ML for Track B)
- Time commitment (20-30 hrs Track A, +10-15 hrs Track B)

**Messaging Alignment:**
- Use "smart cities" and "transportation analytics" framing
- Emphasize "commuters and travelers" (universal appeal)
- Highlight portfolio value for both tracks

**Why:** Learners need clarity before choosing track (Module 3 decision point)

**Status:** 🔴 Not Started

---

#### **Document 3: Learning Pathways Guide**
**File:** `docs/learning_pathways.md` (NEW)

**Purpose:** Navigate different skill levels through the course

**Content:**
- **Beginner Path:** Modules 1-3 → 4A → 5A → 6-10 → Capstone Track A (20-30 hours)
- **Advanced Path:** Same + 4B + 5B → Capstone Track B (30-45 hours total)
- **Self-Directed Path:** Choose modules based on interest (flexible)
- Time estimates per path
- Prerequisites and skill checks
- Track selection timing (hybrid approach):
  - Module 1: Introduction to dual-track concept
  - Modules 2-3: Foundation (everyone completes)
  - Module 3 end: Decision point with guidance
- Self-assessment quizzes
- "Can I switch tracks?" FAQ (yes, anytime)
- Completion criteria (any track + capstone = certificate)

**Why:** Diverse learner base needs clear guidance (Udemy students self-paced)

**Status:** 🔴 Not Started

---

### **Priority 2: Module Content Updates**

#### **Module 2: Data Acquisition**

**Files to Update:**
- `notebooks/Module_02_Data_Acquisition/README.md`
- `notebooks/Module_02_Data_Acquisition/MODULE_02_OVERVIEW.md`
- `notebooks/Module_02_Data_Acquisition/M2_01_amsterdam_bike_api_SOLUTIONS.ipynb`

**Changes Needed:**

**README.md:**
- [ ] Add "🎯 Two Prediction Use Cases" section
- [ ] Link to `docs/ov_fiets_system_overview.md`
- [ ] Add "Which use case are we solving?" callout
- [ ] Preview: "Module 4-5 offer two tracks: commuter (Track A) or multi-day (Track B)"
- [ ] Set expectations: "You'll choose your track at Module 3 end" (hybrid approach)
- [ ] Prerequisites reminder: Python basics required for all, ML fundamentals for Track B

**MODULE_02_OVERVIEW.md:**
- [ ] Update "Why data acquisition matters" with OV-fiets context
- [ ] Add "Understanding Your Problem Domain" section
- [ ] Introduce operational constraints (15-min refresh, etc.)

**M2_01_SOLUTIONS.ipynb:**
- [x] ✅ Already has domain insight section (Task 8.1) 
- [x] ✅ Already has critical thinking section (Task 8.4)
- [ ] Consider adding: "Preview of Two Use Cases" cell before Key Takeaways
- [ ] Link to new documentation

**Status:** 🟡 Partially Complete (SOLUTIONS done, READMEs need updates)

---

#### **Module 3: Exploration & Profiling**

**Files to Update:**
- `notebooks/Module_03_Exploration_Profiling/README.md`

**New Content Needed:**
- [ ] Create notebook: `M3_05_commuter_vs_tourist_patterns.ipynb`

**Changes:**

**README.md:**
- [x] ✅ Already has OV-fiets domain insight section
- [ ] Add learning objective: "Identify commuter vs tourist rental patterns"
- [ ] Add exploration task: "Temporal analysis to distinguish user types"

**M3_05 Notebook (NEW):**
- [ ] Analyze rental duration distributions
- [ ] Compare weekday vs weekend patterns
- [ ] Identify peak commuter hours
- [ ] Discover holiday/tourist spikes
- [ ] Visualize two distinct user populations
- [ ] Set up data subsets for Track A vs Track B

**Status:** 🔴 Not Started

---

#### **Module 4: Feature Engineering (Both Tracks)**

**Files to Create/Update:**
- `notebooks/Module_04_Feature_Engineering/README.md` (update)
- `notebooks/Module_04_Feature_Engineering/track_a_commuter/` (NEW folder)
- `notebooks/Module_04_Feature_Engineering/track_a_commuter/README.md` (NEW)
- `notebooks/Module_04_Feature_Engineering/track_b_multiday/` (NEW folder)
- `notebooks/Module_04_Feature_Engineering/track_b_multiday/README.md` (NEW)

**Changes:**

**Main README.md:**
- [x] ✅ Already has OV-fiets domain insight with feature guidance
- [ ] Add "🎯 Choose Your Track" section at top
- [ ] Explain two track folders available
- [ ] Add decision guide with track comparison table
- [ ] Link to `docs/use_case_comparison.md`

**track_a_commuter/ (NEW):**
- [ ] README: Short-term features (1-4 hour horizon), classification focus
- [ ] M4A_01_temporal_features.ipynb - Hour, day, peak flags
- [ ] M4A_02_weather_features.ipynb - Current conditions
- [ ] M4A_03_train_schedule.ipynb - Arrival/departure times

**track_b_multiday/ (NEW):**
- [ ] README: Long-term features (1-3 day horizon), regression focus
- [ ] M4B_01_extended_temporal.ipynb - Holidays, weekends, events
- [ ] M4B_02_weather_forecasts.ipynb - 3-day weather predictions
- [ ] M4B_03_event_calendars.ipynb - Tourist attractions, festivals

**Status:** 🔴 Not Started

---

#### **Module 5: Modeling (Both Tracks)**

**Files to Create/Update:**
- `notebooks/Module_05_Modeling/README.md` (update)
- `notebooks/Module_05_Modeling/track_a_classification/` (NEW folder)
- `notebooks/Module_05_Modeling/track_a_classification/README.md` (NEW)
- `notebooks/Module_05_Modeling/track_b_regression/` (NEW folder)
- `notebooks/Module_05_Modeling/track_b_regression/README.md` (NEW)

**Changes:**

**Main README.md:**
- [x] ✅ Already has OV-fiets constraints
- [ ] Add "🎯 Choose Your Track" section at top
- [ ] Explain two modeling approaches available
- [ ] Prerequisites: Complete corresponding Module 4 track first
- [ ] Link to modeling approach comparison

**track_a_classification/ (NEW):**
- [ ] README: Binary classification, short-term predictions
- [ ] Target: `bike_available` (yes/no at 2-4 hour horizon)
- [ ] Metrics: Accuracy, precision, recall, F1-score
- [ ] M5A_01_baseline_model.ipynb
- [ ] M5A_02_classification_models.ipynb (Logistic, RF, XGBoost)
- [ ] M5A_03_model_selection.ipynb

**track_b_regression/ (NEW):**
- [ ] README: Regression, long-term predictions
- [ ] Target: `bikes_available_count` (1-3 day horizon)
- [ ] Metrics: MAE, RMSE, R²
- [ ] M5B_01_regression_models.ipynb (Linear, RF, Gradient Boosting)
- [ ] M5B_02_time_series_models.ipynb (ARIMA, Prophet, LSTM)
- [ ] M5B_03_uncertainty_quantification.ipynb

**Status:** 🔴 Not Started

---

#### **Modules 6-10: Integration Updates**

**Files to Update:**
- `notebooks/Module_06_Validation_Governance/README.md`
- `notebooks/Module_07_Visualization/README.md`
- `notebooks/Module_08_Automation/README.md`
- `notebooks/Module_09_Experimentation/README.md`
- `notebooks/Module_10_Collaboration/README.md`

**Module 06: Validation & Governance**

**README.md:**
- [x] ✅ Already has OV-fiets validation guidance
- [ ] Add section: "Validating Different Model Types"
- [ ] Compare validation strategies for classification vs regression
- [ ] Add examples for both Track A and Track B validation
- [ ] Model selection criteria (when to use which)

**Notebook Updates (Optional):**
- [ ] Add examples for classification validation
- [ ] Add examples for regression validation
- [ ] Compare business value of both approaches

**Status:** 🟡 Minor Updates Needed

**Module 07: Visualization**
- [ ] Add dashboard examples for classification (Track A)
- [ ] Add dashboard examples for regression (Track B)
- [ ] Show how to visualize different prediction types

**Module 08: Automation**
- [ ] Add pipeline examples for both tracks
- [ ] Discuss model-specific automation needs

**Module 09: Experimentation**
- [ ] MLflow tracking for both model types
- [ ] Comparing classification vs regression experiments

**Module 10: Collaboration**
- [ ] Team scenarios with different track responsibilities
- [ ] Model comparison and selection workflows

**Status:** 🟡 Minor Updates Needed

---

#### **Capstone Project**

**Files to Update:**
- `capstone/capstone_guidelines.md`
- `capstone/grading_rubric.md`
- `capstone/self_evaluation.md`

**Changes Needed:**

**capstone_guidelines.md:**
- [ ] Add "🎯 Choose Your Capstone Track" section after Overview
- [ ] Track A option: Commuter prediction (classification)
- [ ] Track B option: Multi-day prediction (regression)
- [ ] Both tracks option: Comparison system (ambitious)
- [ ] Prerequisites for each track clearly stated

**grading_rubric.md:**
- [ ] Update Section 4 (Modeling) metrics to support both tracks:
  - Classification: Accuracy, F1, Precision/Recall
  - Regression: R², MAE, RMSE
- [ ] Ensure all sections are track-agnostic
- [ ] Add bonus points for completing both tracks

**self_evaluation.md:**
- [ ] Add track selection question
- [ ] Track-specific self-assessment criteria

**capstone_starter.ipynb:**
- [ ] Add "Which Track Should I Choose?" guidance section
- [ ] Link to use case comparison doc
- [ ] Adjust checklist for track flexibility

**Status:** 🟡 Minor Updates Needed (Structure already flexible ✅)

---

## 📋 Implementation Checklist

### **Phase 1: Foundation (Week 1)**
**Goal:** Establish documentation foundation before any module changes

- [ ] **Step 1.1:** Create `docs/ov_fiets_system_overview.md`
  - Document operational details (15-min refresh, 72-hour rentals, no docks)
  - Frame as "real operational data" not "sanitized datasets"
  - Explain why this matters for modeling (domain constraints)
  - Add to all relevant READMEs as reference
  
- [ ] **Step 1.2:** Create `docs/use_case_comparison.md`
  - Side-by-side comparison table (commuter vs multi-day)
  - Decision tree for learners
  - Prerequisites checklist (Python basics vs ML fundamentals)
  - Time estimates (20-30 hrs vs +10-15 hrs)
  - Use "smart cities" and "transportation" framing
  
- [ ] **Step 1.3:** Create `docs/learning_pathways.md`
  - Beginner/advanced path descriptions
  - Hybrid track selection approach (Module 1 awareness, Module 3 decision)
  - Time estimates and prerequisites
  - Self-assessment quizzes
  - "Can I switch tracks?" FAQ
  
- [ ] **Step 1.4:** Update `README.md` (top-level)
  - Add "About This Course" section with marketing pitch:
    - "Transform smart cities data into actionable predictions"
    - Real bike-sharing data from Amsterdam
    - Dual learning tracks (beginner + advanced)
  - Add prerequisites section (Python basics required)
  - Update time estimates (20-30 hrs Track A, 30-45 hrs both)
  - Link to new documentation (pathways, use cases)
  - Add "What You'll Learn" bullets (from Udemy course description)
  
- [ ] **Step 1.5:** Update `docs/open_data_sources.md`
  - Fix Amsterdam section (remove dock references)
  - Clarify CityBikes API → OV-fiets endpoint
  - Add OV-fiets operational context
  - Frame as "real operational data" for smart cities
  - Distinguish data needs for both tracks
  
- [ ] **Step 1.6:** Update `docs/README_NAVIGATION.md`
  - Add track structure explanation
  - Update module table with track indicators
  - Add links to new pathway documents

**Success Criteria:** 
- All foundation docs exist and use consistent marketing messaging
- No contradictions about "docks" in Amsterdam
- Clear learner pathways documented with hybrid selection approach
- Prerequisites clearly stated (Python for Track A, +ML for Track B)
- Udemy-ready descriptions and positioning

---

### **Phase 2: Module 2-3 Updates (Week 2)**
**Goal:** Set up use case introduction and pattern identification (foundation for track selection)

- [ ] **Step 2.1:** Update Module 2 README
  - Add "Two Use Cases" section (commuter vs tourist)
  - Link to foundation docs (ov_fiets_system_overview, use_case_comparison)
  - Message: "You'll choose your track at Module 3 end"
  - Frame as "smart cities" and "transportation analytics"
  
- [ ] **Step 2.2:** Update Module 2 OVERVIEW
  - Add operational context (real data, not sanitized)
  - Introduce domain constraints (15-min refresh, 72-hour rental)
  - Emphasize universal problem (commuters/travelers everywhere)
  
- [ ] **Step 2.3:** Enhance M2_01 SOLUTIONS
  - Add "Preview of Two Use Cases" section (optional enhancement)
  - Link to use case comparison guide
  - Keep existing domain insights (already excellent)
  
- [ ] **Step 2.4:** Update Module 3 README
  - Add pattern identification objectives
  - Prepare for track divergence (Module 4)
  - Add "Choose Your Track" section at end:
    - Self-assessment checklist
    - Link to learning pathways guide
    - Prerequisites reminder (Python vs ML fundamentals)
    - Time commitment guidance (20-30 hrs vs 30-45 hrs)
  
- [ ] **Step 2.5:** Create M3_05 notebook
  - Commuter vs tourist pattern analysis
  - Show both use cases in data
  - Set up learner decision point
  - Link to track selection guidance

**Success Criteria:**
- Learners understand two use cases by end of Module 2
- Module 3 provides hands-on experience with both patterns
- Clear decision point at Module 3 end (hybrid approach)
- Prerequisites and time estimates clear
- Marketing messaging consistent ("smart cities," "transportation")

---

### **Phase 3: Module 4 Sub-Track Creation (Week 3)**
**Goal:** Create sub-track folders within Module 4 for both tracks

- [ ] **Step 3.1:** Update Module 4 main README
  - Add "Choose Your Track" section
  - Explain track_a_commuter and track_b_multiday folders
  - Add decision guide and comparison table
  
- [ ] **Step 3.2:** Create track_a_commuter/ folder
  - Create sub-folder README (short-term features focus)
  - Create M4A_01_temporal_features.ipynb
  - Create M4A_02_weather_features.ipynb
  - Create M4A_03_train_schedule.ipynb
  
- [ ] **Step 3.3:** Create track_b_multiday/ folder
  - Create sub-folder README (long-term features focus)
  - Create M4B_01_extended_temporal.ipynb
  - Create M4B_02_weather_forecasts.ipynb
  - Create M4B_03_event_calendars.ipynb

**Success Criteria:**
- Both track folders exist with clear separation
- Learners can choose based on skill level
- Each track has distinct feature engineering focus

---

### **Phase 4: Module 5 Sub-Track Creation (Week 4)**
**Goal:** Create sub-track folders within Module 5 for both modeling approaches

- [ ] **Step 4.1:** Update Module 5 main README
  - Add "Choose Your Track" section
  - Explain track_a_classification and track_b_regression folders
  - Prerequisites: Complete corresponding Module 4 track
  
- [ ] **Step 4.2:** Create track_a_classification/ folder
  - Create sub-folder README (classification focus)
  - Create M5A_01_baseline_model.ipynb
  - Create M5A_02_classification_models.ipynb
  - Create M5A_03_model_selection.ipynb
  
- [ ] **Step 4.3:** Create track_b_regression/ folder
  - Create sub-folder README (regression/time series focus)
  - Create M5B_01_regression_models.ipynb
  - Create M5B_02_time_series_models.ipynb
  - Create M5B_03_uncertainty_quantification.ipynb

**Success Criteria:**
- Both modeling approaches clearly separated
- Track A: Classification with appropriate metrics
- Track B: Regression/time series with appropriate metrics
- Each track builds on corresponding Module 4 track

---

### **Phase 5: Modules 6-10 Integration (Week 5)**
**Goal:** Update existing modules to acknowledge and support both tracks

- [ ] **Step 5.1:** Update Module 6 (Validation)
  - Add section on validating different model types
  - Examples for classification and regression validation
  - Model comparison framework
  
- [ ] **Step 5.2:** Update Module 7 (Visualization)
  - Add dashboard examples for both prediction types
  - Visualizing classification vs regression outputs
  
- [ ] **Step 5.3:** Update Module 8 (Automation)
  - Pipeline examples for both tracks
  - Model-specific automation considerations
  
- [ ] **Step 5.4:** Update Module 9 (Experimentation)
  - MLflow tracking for different model types
  - Comparing experiments across tracks
  
- [ ] **Step 5.5:** Update Module 10 (Collaboration)
  - Team workflows with different tracks
  - Model selection and comparison

**Success Criteria:**
- All modules support both tracks with examples
- No broken links (modules stay numbered 6-10) ✅
- Integration guidance clear for both model types

---

### **Phase 6: Capstone & Documentation Updates (Week 6)**
**Goal:** Update capstone for track flexibility and finalize documentation

- [ ] **Step 6.1:** Update capstone files
  - Add "Choose Your Track" to capstone_guidelines.md
  - Update grading_rubric.md for both model types
  - Update capstone_starter.ipynb with track guidance
  - Update self_evaluation.md
  
- [ ] **Step 6.2:** Update navigation documents
  - Update docs/README_NAVIGATION.md
  - Update notebooks/README.md module table
  - Update top-level README with pathway guidance
  
- [ ] **Step 6.3:** Cross-reference check
  - All links work
  - No contradictions
  - Consistent terminology
  
- [ ] **Step 6.4:** Learner pathway validation
  - Test beginner path (Modules 1-3 → 4A → 5A → 6-10 → Capstone A)
  - Test advanced path (Same + 4B + 5B → Capstone B)
  - Clear guidance at decision points?

**Success Criteria:**
- Capstone supports both tracks seamlessly
- Course navigation clear for all learner paths
- Documentation is professional and consistent

---

## 🎯 Success Metrics

### **For Beginners (Track A Only):**
- [ ] Can complete Modules 1-5 in 20-30 hours
- [ ] Build working classification model
- [ ] Understand commuter prediction problem
- [ ] Achieve 85%+ accuracy on test set

### **For Intermediate (Both Tracks):**
- [ ] Can complete Modules 1-7 in 40-50 hours
- [ ] Compare classification vs regression approaches
- [ ] Understand trade-offs between model types
- [ ] Build both prediction systems

### **For Advanced (Full Course):**
- [ ] Complete all modules with challenges
- [ ] Implement ensemble approaches
- [ ] Deploy production system
- [ ] Demonstrate sophisticated ML techniques

---

## 🚨 Risks & Mitigation

### **Risk 1: Too Complex for Beginners**
**Mitigation:** 
- Clear signposting: "Track A is sufficient for beginners"
- Track B clearly marked as optional/advanced
- Track A can stand alone as complete learning experience

### **Risk 2: Inconsistent Documentation**
**Mitigation:**
- This tracking document
- Phase 1 establishes foundation before any changes
- Regular cross-reference checks

### **Risk 3: Scope Creep**
**Mitigation:**
- Sub-track folders within existing Modules 4-5 (minimal disruption)
- Modules 6-10 only need minor updates (no restructuring)
- Well-defined boundaries for each phase

### **Risk 4: Breaking Existing Content**
**Mitigation:**
- Module 1 unchanged (validated) ✅
- Modules 6-10 unchanged structurally (no renumbering) ✅
- Sub-folders added, not replaced
- Git commit after each phase
- Can roll back if needed
- All existing links remain valid ✅

---

## 📝 Notes & Decisions

### **Decision Log:**

**2026-01-18:** Confirmed Module 1 stays unchanged ✅
- Rationale: Technology-focused, supports both use cases, already working well

**2026-01-18:** Decided on dual-track structure vs single unified approach
- Rationale: Better serves diverse learner base, maintains clarity, teaches more ML concepts

**2026-01-18:** Prioritized foundation docs before module updates
- Rationale: Avoid inconsistencies, establish reference documents, maintain alignment

### **Open Questions:**

1. **Data Collection:** Do we have/need rental duration data for Track B?
   - Answer: TBD - may need to synthesize or use historical patterns

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
