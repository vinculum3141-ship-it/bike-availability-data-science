# Module 04: Feature Engineering

## 📌 Module Overview
Transform raw data into meaningful features for machine learning models.

---

## 🎯 Track Selection: Choose Your Path

**At this point, the course diverges into two tracks based on your decision from Module 3.**

### Track A: Commuter Prediction (Binary Classification)
📁 **Folder:** `track_a_commuter/`  
**Goal:** Predict bike availability in the next 15 minutes (available/not available)  
**Features Focus:** Short-term, immediate patterns  
**Notebooks:**
- M4A_01: Temporal features (rush hour, cyclical encodings)
- M4A_02: Current weather features
- M4A_03: Train schedule features (next 15-30 minutes)

→ [Go to Track A README](./track_a_commuter/README.md)

### Track B: Multi-Day Tourist Prediction (Regression/Time Series)
📁 **Folder:** `track_b_multiday/`  
**Goal:** Predict number of bikes available over 24-72 hours  
**Features Focus:** Long-term trends, forecasts, events  
**Notebooks:**
- M4B_01: Extended temporal features (seasonal, lag features)
- M4B_02: Weather forecasts (24-72 hour predictions)
- M4B_03: Event calendar features (festivals, holidays)

→ [Go to Track B README](./track_b_multiday/README.md)

### Track Comparison

| Aspect | Track A (Commuter) | Track B (Multi-Day) |
|--------|-------------------|---------------------|
| **Prediction Horizon** | 15 minutes | 24-72 hours |
| **Problem Type** | Binary Classification | Regression/Time Series |
| **Feature Complexity** | Moderate | High |
| **Time Commitment** | 3-4 hours | 5-6 hours |
| **Prerequisites** | Module 3 complete | Track A OR ML fundamentals |
| **Weather Data** | Current conditions | Forecasts |
| **Temporal Features** | Rush hour, current patterns | Seasonal, lag features, trends |

### Can I Do Both Tracks?
**Yes!** Many learners complete Track A first (simpler) then proceed to Track B.  
**Recommended sequence:** Track A → Track B (builds confidence and understanding)

### Still Deciding?
- Review [Use Case Comparison Guide](../../docs/guides/use_case_comparison.md)
- Check [Learning Pathways Guide](../../docs/guides/learning_pathways.md)
- Revisit [M3_05 Pattern Analysis](../Module_03_Exploration_Profiling/M3_05_pattern_analysis.ipynb)

---

## ⚠️ Critical Domain Insight for Course Developers

**OV-fiets System Characteristics:**
- **No docking system**: `docks_available` field is always 0
- **Same-station returns**: Bikes must return to origin station
- **After-hours flexibility**: Bikes can be left outside without docking

**Impact on Module 4 Feature Engineering:**
- ❌ **CANNOT create dock-based features**:
  - No "docks_full_ratio", "dock_pressure", "dock_availability_rate"
  - No dock-related lag features
  - No dock rebalancing patterns

- ✅ **FOCUS on bike-centric features**:
  - `bikes_per_station_hour` (hourly availability patterns)
  - `zero_bike_frequency` (how often station runs out)
  - `bike_availability_rolling_mean` (temporal trends)
  - `station_to_station_flow` (origin-return constraint)
  - `after_hours_return_patterns` (unique to OV-fiets)

- ✅ **Key assumptions to encode**:
  - Station capacity is relatively fixed (bike inventory)
  - bikes_available ≤ station_capacity at all times

**Reference:** See M2_01 SOLUTIONS notebook, Task 8.1 for full explanation.

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 4 teaches **feature engineering techniques** with progressive independence.

**Scaffolding Strategy:**
- **Initial**: 70% complete - Learn feature engineering patterns
- **Progressive**: 70% → 20% as concepts build on each other
- **Goal**: Create features independently, understand feature importance
- **Approach**: See examples → Practice variations → Design custom features

**Progressive Difficulty (Each Notebook):**
- Part 1: Feature Concepts (90% complete)
- Part 2: Basic Features (60%)
- Part 3: Intermediate Features (40%)
- Part 4: Advanced Features (25%)
- Part 5: Custom Features (10% + creative challenges)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` for verification
- Multiple feature engineering approaches
- Best practices and pitfalls explained

**Optional Challenges:**
- Domain-specific features
- Automated feature generation
- Feature interaction exploration

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Create time-based features (hour, day, month, etc.)
- Engineer weather-related features
- Handle categorical variables
- Create lag features and rolling statistics (Track B)
- Scale and normalize features

## ✅ Your Tasks

**Choose your track and complete the notebooks in that folder:**

### Track A: Commuter Prediction (`track_a_commuter/`)
1. **M4A_01_temporal_features.ipynb**
   - Extract hour, day_of_week, month, season
   - Create is_weekend, is_holiday flags
   - Engineer rush_hour indicators
   - Create cyclical time encodings

2. **M4A_02_weather_features.ipynb**
   - Bin temperature into categories
   - Create weather condition groups
   - Engineer rain indicators
   - Handle missing weather data

3. **M4A_03_train_schedule.ipynb**
   - Create "minutes until next train" features
   - Calculate train frequency (next 15-30 minutes)
   - Build train proximity indicators
   - Combine train + rush hour interactions

### Track B: Multi-Day Tourist (`track_b_multiday/`)
1. **M4B_01_extended_temporal.ipynb**
   - Create extended temporal features (day, month, season)
   - Build lag features (24hr, 7-day)
   - Calculate rolling statistics (24hr, 48hr, weekly)
   - Engineer interaction features (weekend × season)

2. **M4B_02_weather_forecasts.ipynb**
   - Use 24-72 hour weather forecasts (not current conditions)
   - Create temperature forecast features
   - Build precipitation probability features
   - Engineer weather trend indicators

3. **M4B_03_event_calendars.ipynb**
   - Integrate Amsterdam event calendars
   - Create tourist season indicators
   - Build major event features (festivals, conferences)
   - Engineer school holiday indicators

### Both Tracks: Feature Scaling (Optional)
After completing your track's notebooks, you may want to normalize and scale features.  
See [coding standards](../../docs/standards/coding_standards.md) for best practices.

## 📝 Naming Convention
Follow this pattern: `M4_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/feature_engineering.py` for reusable transformations
- Check [code snippets](../../docs/references/code_snippets.md) for feature engineering examples
- Avoid data leakage (don't use future data!)
- Document feature meanings clearly
- Keep track of feature importance ideas
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `pandas` - Feature creation
- `numpy` - Mathematical operations
- `scikit-learn` - Scaling and encoding
- `category_encoders` - Advanced encoding

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - Feature engineering examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices
- 📊 [Data Organization](../../data/README.md) - Save processed data here

## ⚠️ Important
- Never use future information in features (data leakage!)
- Apply same transformations to train/validation/test sets
- Save feature engineering pipelines for reproducibility

## ✨ Checkpoint
Before moving to Module 05, ensure:

**Track A Checklist:**
- [ ] Temporal features created (rush hour, cyclical encodings)
- [ ] Current weather features engineered
- [ ] Train schedule features built
- [ ] Features saved to `data/processed/track_a_*.csv`

**Track B Checklist:**
- [ ] Extended temporal features created (seasonal, lag, rolling)
- [ ] Weather forecast features engineered
- [ ] Event calendar features integrated
- [ ] Time series features validated (no data leakage!)
- [ ] Features saved to `data/processed/track_b_*.csv`

---
**Next Module:** Module 05 - Modeling  
- **Track A:** Go to `Module_05_Modeling/track_a_classification/`
- **Track B:** Go to `Module_05_Modeling/track_b_regression/`
