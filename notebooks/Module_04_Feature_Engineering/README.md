# Module 04: Feature Engineering

## 📌 Module Overview
Transform raw data into meaningful features for machine learning models.

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
