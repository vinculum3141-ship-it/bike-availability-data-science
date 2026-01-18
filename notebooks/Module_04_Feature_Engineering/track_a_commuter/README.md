# Track A: Commuter Prediction (Classification)

## 🎯 Track Focus
**Goal:** Predict whether bikes will be available in the **next 15 minutes** (binary classification)

**Why This Track?**
- Focus on short-term, immediate availability
- Perfect for commuters who need "bike available now?"
- Simpler problem: binary classification (available/not available)
- Shorter feature horizon: focus on current conditions

## 📊 Feature Engineering Strategy

### Time Horizon: **15 Minutes**
All features in this track focus on **immediate patterns**:
- Current hour/day patterns (rush hour identification)
- Current weather conditions (not forecasts)
- Recent availability trends (last 1-2 hours)
- Train arrival schedules (next 15-30 minutes)

### Key Feature Categories

#### 1. **Temporal Features** (M4A_01)
- Hour of day (0-23) with rush hour indicators
- Day of week (weekday vs weekend)
- Holiday indicators
- Cyclical encodings (sin/cos transformations)
- **Focus**: Identify peak commuter times

#### 2. **Weather Features** (M4A_02)
- Current temperature binning
- Current weather conditions
- Rain indicator (yes/no)
- **Focus**: Current conditions affecting bike choice

#### 3. **Train Schedule Features** (M4A_03)
- Minutes until next train arrival
- Number of trains in next 15 minutes
- Peak vs off-peak train frequency
- **Focus**: Train station bike demand patterns

#### 4. **Short-Term Lag Features**
- Bikes available 15 minutes ago
- Bikes available 30 minutes ago
- Rolling mean (last 1-2 hours)
- **Focus**: Very recent trends

### Success Criteria
Your features should help answer:
- "Is it rush hour right now?"
- "Did bikes just run out?"
- "Is a train arriving soon?"
- "What's the weather like right now?"

## 🔗 What's Next?
After completing feature engineering, you'll move to:
- **Module 5 Track A**: Classification models (Logistic Regression, Random Forest, XGBoost)
- **Evaluation**: Precision, recall, F1-score
- **Goal**: Minimize false negatives (predict "available" when bikes run out)

## 📚 Resources
- [Use Case Comparison Guide](../../../docs/guides/use_case_comparison.md)
- [OV-fiets System Overview](../../../docs/guides/ov_fiets_system_overview.md)
- [Learning Pathways Guide](../../../docs/guides/learning_pathways.md)
