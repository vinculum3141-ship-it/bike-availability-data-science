# Module 04: Feature Engineering

## 📌 Module Overview
Transform raw data into meaningful features for machine learning models.

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
- Create lag features and rolling statistics
- Scale and normalize features

## ✅ Your Tasks
Create the following notebooks in this folder:

### M4_01_temporal_features.ipynb
- Extract hour, day_of_week, month, season
- Create is_weekend, is_holiday flags
- Engineer rush_hour indicators
- Create cyclical time encodings

### M4_02_weather_features.ipynb
- Bin temperature into categories
- Create weather condition groups
- Engineer "feels_like" temperature
- Handle missing weather data

### M4_03_lag_rolling_features.ipynb
- Create lag features (previous hour availability)
- Calculate rolling averages (3hr, 6hr, 24hr)
- Compute rolling standard deviations
- Create trend indicators

### M4_04_feature_scaling.ipynb
- Normalize numerical features
- Encode categorical variables
- Handle skewed distributions
- Save processed features to `data/processed/`

## 📝 Naming Convention
Follow this pattern: `M4_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/feature_engineering.py` for reusable transformations
- Check [code snippets](../../docs/code_snippets.md) for feature engineering examples
- Avoid data leakage (don't use future data!)
- Document feature meanings clearly
- Keep track of feature importance ideas
- Follow [coding standards](../../docs/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `pandas` - Feature creation
- `numpy` - Mathematical operations
- `scikit-learn` - Scaling and encoding
- `category_encoders` - Advanced encoding

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📚 [Code Snippets](../../docs/code_snippets.md) - Feature engineering examples
- 📐 [Coding Standards](../../docs/coding_standards.md) - Best practices
- 📊 [Data Organization](../../data/README.md) - Save processed data here

## ⚠️ Important
- Never use future information in features (data leakage!)
- Apply same transformations to train/validation/test sets
- Save feature engineering pipelines for reproducibility

## ✨ Checkpoint
Before moving to Module 05, ensure:
- [ ] You have time-based features
- [ ] Weather features are engineered
- [ ] Lag and rolling features are created
- [ ] Features are scaled appropriately
- [ ] Processed data is saved to `data/processed/`

---
**Next Module:** Module 05 - Modeling
