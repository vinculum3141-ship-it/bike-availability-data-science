# Module 03: Exploration & Profiling

## 📌 Module Overview
Explore your datasets, understand distributions, identify patterns, and detect data quality issues. **This module ends with a critical decision point** — you'll choose your learning track based on patterns you discover.

**🎯 Dual-Track Context**: This is the **last foundation module** (shared by all students). By the end, you'll identify **two distinct rental patterns** and choose between:
- **Track A (Beginner):** Classification for commuter short-term predictions
- **Track B (Advanced):** Regression + Time series for multi-day forecasting

**Decision Point**: End of this module → See "Track Selection Decision" section below

## ⚠️ Critical Domain Insight for Course Developers

**OV-fiets System Characteristics:**
- **No docking system**: `docks_available` field is always 0
- **Same-station returns**: Bikes must return to origin station
- **After-hours flexibility**: Bikes can be left outside without docking

**Impact on Module 3:**
- ❌ Don't expect dock utilization patterns in data
- ✅ Focus exploration on bike availability patterns only
- ✅ Station "capacity" = bike inventory, not physical docks
- ✅ Identify temporal patterns in bike availability
- ✅ Document this finding in profiling reports

**Reference:** See M2_01 SOLUTIONS notebook, Task 8.1 for full explanation.

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 3 introduces **new data exploration concepts** using progressive scaffolding.

**Scaffolding Strategy:**
- **Initial**: 70% complete - Learn EDA patterns and profiling tools
- **Progressive**: 70% → 30% through 5 parts per notebook
- **Goal**: Master exploration techniques, identify patterns independently
- **Approach**: Guided examples → Moderate practice → Independent analysis

**Progressive Difficulty (Each Notebook):**
- Part 1: Setup & Demos (90% complete)
- Part 2: Guided Practice (70%)
- Part 3: Moderate Analysis (50%)
- Part 4: Independent Exploration (30%)
- Part 5: Advanced Insights (10% + optional)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` for each notebook
- Attempt tasks first, then verify
- Multiple valid approaches shown

**Optional Challenges:**
- Deep-dive statistical tests
- Custom visualization functions
- Automated insight generation

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Perform exploratory data analysis (EDA)
- Generate automated data profiling reports
- Identify missing values and outliers
- Understand temporal patterns
- Visualize distributions and relationships
- **NEW:** Distinguish between commuter and tourist rental patterns
- **NEW:** Make an informed decision about which learning track to follow

## ✅ Your Tasks
Create the following notebooks in this folder:

### M3_01_basic_statistics.ipynb
- Calculate summary statistics
- Check data types and shapes
- Identify missing values
- Detect outliers

### M3_02_automated_profiling.ipynb
- Generate pandas-profiling report
- Analyze variable correlations
- Identify duplicate records
- Check data quality metrics

### M3_03_temporal_analysis.ipynb
- Analyze bike availability over time
- Identify daily/weekly patterns
- Detect seasonal trends
- Examine peak hours

### M3_04_visualization.ipynb
- Create distribution plots
- Visualize temporal patterns
- Explore relationships between variables
- Build correlation heatmaps

### M3_05_pattern_analysis.ipynb **NEW: Track Decision Support**
- **Commuter vs Tourist Patterns**: Analyze distinct user populations
- **Weekday vs Weekend**: Compare rental behaviors
- **Peak Hours**: Identify commuter rush patterns
- **Rental Duration**: Short-term (1-4 hrs) vs long-term (12-72 hrs)
- **Holiday Impact**: Tourist demand spikes
- **Decision Support**: Visualizations to help choose Track A or Track B

💡 **This notebook is critical for making your track choice!**

## 📝 Naming Convention
Follow this pattern: `M3_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Review the [example EDA notebook](../example_data_exploration.ipynb) for best practices
- Use `ydata-profiling` (formerly pandas-profiling) for quick automated analysis
- Look for patterns in time series data
- Check [code snippets](../../docs/references/code_snippets.md) for visualization examples
- Pay attention to data quality issues early
- Document insights for later feature engineering
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `pandas` - Data manipulation
- `ydata-profiling` - Automated profiling
- `matplotlib` / `seaborn` - Static visualizations
- `plotly` - Interactive visualizations

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 🎓 [Example EDA Notebook](../example_data_exploration.ipynb) - Learn from this
- �️ [Learning Pathways Guide](../../docs/guides/learning_pathways.md) - **NEW:** Visualize both tracks
- 🔀 [Use Case Comparison](../../docs/guides/use_case_comparison.md) - **NEW:** Commuter vs Tourist
- 🚲 [OV-fiets System Overview](../../docs/guides/ov_fiets_system_overview.md) - **NEW:** Domain context
- �📚 [Code Snippets](../../docs/references/code_snippets.md) - Visualization examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices
- 📊 [Data Organization](../../data/README.md) - Data structure guide

## ✨ Checkpoint
Before moving to Module 04, ensure:
- [ ] You understand the data distributions
- [ ] Missing values are documented
- [ ] You've identified key temporal patterns
- [ ] Data quality issues are noted
- [ ] Key insights are summarized
- [ ] **NEW:** You've completed M3_05 pattern analysis notebook
- [ ] **NEW:** You understand the difference between commuter and tourist patterns
- [ ] **NEW:** You've reviewed the track selection guides

---

## 🎯 TRACK SELECTION DECISION POINT

**Congratulations!** You've completed the foundation modules (1-3). Now it's time to **choose your learning path**.

### What You've Discovered
Through your exploration, you've identified **two distinct rental patterns**:

1. **Commuter Pattern (Short-term)**
   - Weekday peaks at 8-9 AM, 5-6 PM
   - Rental duration: 1-4 hours
   - Predictable daily patterns
   - Train schedule correlation

2. **Tourist Pattern (Multi-day)**
   - Weekend and holiday spikes
   - Rental duration: 12-72 hours
   - Seasonal variation
   - Event-driven demand

### Your Track Options

#### 🅰️ Track A: Classification (Beginner)
**Focus**: Predict bike availability (yes/no) for commuters  
**Duration**: 20-30 hours  
**Prerequisites**: Python basics (what you have now)  
**Problem**: "Will a bike be available at 8:30 AM tomorrow?"  

**You'll Learn:**
- Binary classification models
- Short-term feature engineering
- Imbalanced data handling
- Classification metrics

**Next Modules**: 4A → 5A → 6-10 → Capstone A

#### 🅱️ Track B: Regression + Time Series (Advanced)
**Focus**: Predict bike counts for tourists + capacity planning  
**Duration**: 30-45 hours (includes Track A + additional content)  
**Prerequisites**: Python + ML fundamentals  
**Problem**: "How many bikes will be available next Saturday?"  

**You'll Learn:**
- All Track A content PLUS
- Regression models
- Time series forecasting (ARIMA, Prophet)
- Long-term feature engineering
- Uncertainty quantification

**Next Modules**: 4A → 4B → 5A → 5B → 6-10 → Capstone B

### 📋 Decision Support Resources

Before choosing, review these guides:

1. **[Use Case Comparison](../../docs/guides/use_case_comparison.md)**
   - Detailed comparison table
   - Prerequisites checklist
   - Decision tree
   - Feature engineering differences

2. **[Learning Pathways Guide](../../docs/guides/learning_pathways.md)**
   - Complete learning journeys
   - Self-assessment quiz
   - Time commitment breakdown
   - Skills comparison

3. **[Course Structure](../../docs/guides/course_structure_dual_track.md)**
   - Module-by-module breakdown
   - Track divergence visualization
   - Capstone options

### 🤔 Still Unsure? Take the Self-Assessment

Answer these questions:

1. **Are you new to machine learning?**
   - YES → Track A recommended
   - NO → Consider Track B

2. **Do you have 30-45 hours available?**
   - YES → Track B gives comprehensive experience
   - NO → Track A completes in 20-30 hours

3. **Do you want to learn time series forecasting?**
   - YES → Track B required
   - NO → Track A is sufficient

4. **Is this for a job/portfolio?**
   - Senior DS role → Track B (more impressive)
   - Entry-level role → Track A is solid
   - Personal learning → Either works!

### ✅ Make Your Choice

**Option 1: Track A (Classification)**
→ Proceed to [Module 04: Feature Engineering](../Module_04_Feature_Engineering/README.md)  
→ Follow `track_a_commuter/` folders in Modules 4-5

**Option 2: Track B (Both Tracks)**
→ Proceed to [Module 04: Feature Engineering](../Module_04_Feature_Engineering/README.md)  
→ Complete BOTH `track_a_commuter/` and `track_b_multiday/` folders

**Option 3: Not Sure Yet**
→ Start with Track A, you can always come back for Track B later!

### 💡 Remember
- **Your choice is flexible** — you can always return for the other track
- **Both tracks** lead to portfolio-worthy projects
- **Track B includes Track A** — you get everything if you choose Track B

---

**Next Module**: Module 04 - Feature Engineering (with track-specific folders)
