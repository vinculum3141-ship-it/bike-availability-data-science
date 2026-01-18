# Module 07: Visualization & Communication

## 📌 Module Overview
Create compelling visualizations and dashboards to communicate insights to stakeholders.

---

## 🎯 Track-Aware Visualization

**Visualization needs differ significantly between classification and regression/forecasting models.**

### Visualization Differences by Track

| Aspect | Track A (Classification) | Track B (Regression/Time Series) |
|--------|-------------------------|----------------------------------|
| **Primary Viz** | Confusion matrix heatmaps, ROC curves | Time series plots, forecast bands |
| **Performance Display** | Precision/Recall bars, F1 scores | RMSE trends, residual plots |
| **Predictions** | Binary indicators (available/not) | Numeric values with uncertainty |
| **Dashboard Focus** | Real-time availability alerts | Multi-day forecast calendars |
| **Key Insights** | False positive/negative patterns | Seasonal trends, forecast accuracy |
| **User Interface** | Traffic light indicators, alerts | Line charts with confidence intervals |

### Common Visualization Tasks (Both Tracks)
- Feature importance charts
- Model comparison plots
- Station-level performance maps
- Time-of-day patterns
- Weather impact visualizations
- Stakeholder reports

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 7 teaches **visualization and communication** - essential data science skills.

**Scaffolding Strategy:**
- **Initial**: 65% complete - Learn visualization best practices
- **Progressive**: 65% → 20% for creative freedom
- **Goal**: Design effective visualizations independently, communicate insights clearly
- **Approach**: Design principles → Tools → Practice → Create custom dashboards

**Progressive Difficulty (Each Notebook):**
- Part 1: Visualization Principles (80% complete)
- Part 2: Basic Charts (55%)
- Part 3: Interactive Viz (40%)
- Part 4: Dashboard Design (25%)
- Part 5: Custom Dashboards (15% + creative projects)

**Solution Notebooks:**
- Separate `*_SOLUTIONS.ipynb` with design alternatives
- Multiple visualization approaches
- Best practices and accessibility considerations

**Optional Challenges:**
- Real-time dashboards
- Mobile-responsive designs
- Storytelling with data

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Design effective visualizations appropriate for your model type
- Build interactive dashboards for classification or forecasting
- Communicate insights to non-technical audiences
- Create reusable visualization components

## ✅ Your Tasks

**Complete these notebooks - examples provided for both tracks:**

### M7_01_static_visualizations.ipynb
**Track A examples:**
- Confusion matrix heatmaps
- ROC curve and precision-recall curves
- Feature importance bar charts
- Classification error patterns by time/station
- Threshold sensitivity analysis

**Track B examples:**
- Time series plots with actuals vs predictions
- Residual plots (scatter, histogram, Q-Q)
- Forecast accuracy by horizon (24h, 48h, 72h)
- Seasonal decomposition plots
- Uncertainty band visualizations

**Both tracks:**
- Station-level performance maps
- Weather impact scatter plots
- Publication-quality exports

### M7_02_interactive_plots.ipynb
**Track A examples:**
- Interactive confusion matrix (drill-down by station)
- ROC curve with threshold slider
- Time-series classification performance
- False positive/negative exploration tool
- Real-time availability status map

**Track B examples:**
- Interactive forecast plots with zoom/pan
- Multi-horizon forecast comparison
- Uncertainty interval adjustment
- Seasonal pattern explorer
- Forecast vs actual comparison tool

**Both tracks:**
- Plotly/Bokeh interactive charts
- Hover information for context
- Linked visualizations (brush & link)

### M7_03_dashboard_prototype.ipynb
**Track A: Commuter Prediction Dashboard**
- Current availability status (all stations)
- Prediction confidence indicators
- False alarm rate monitoring
- Rush hour performance metrics
- Station-level drill-down

**Track B: Multi-Day Forecast Dashboard**
- 3-day forecast calendar view
- Confidence interval displays
- Historical accuracy trends
- Seasonal pattern indicators
- Event impact visualization

**Both tracks:**
- Key metrics and KPIs
- Performance monitoring charts
- Alert thresholds and notifications

### M7_04_streamlit_app.ipynb
**Track A: Build classification dashboard in `apps/streamlit_dashboard.py`**
- Real-time bike availability predictions
- Station selection and filtering
- Prediction confidence display
- Historical accuracy tracking
- Alert configuration

**Track B: Build forecasting dashboard in `apps/streamlit_dashboard.py`**
- Multi-day forecast display
- Uncertainty visualization
- Horizon selection (24h/48h/72h)
- Forecast accuracy metrics
- Event calendar integration

## 📝 Naming Convention
Follow this pattern: `M7_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use `src/visualization.py` for reusable plotting functions
- Check [code snippets](../../docs/references/code_snippets.md) for visualization examples
- Reference [reporting template](../../docs/best_practices/reporting_template.md) for stakeholder communication
- Keep dashboards simple and focused
- Design for your audience (technical vs business)
- Test with real users if possible
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `matplotlib` / `seaborn` - Static plots
- `plotly` - Interactive visualizations
- `streamlit` - Dashboard framework

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - Visualization examples
- 📈 [Reporting Template](../../docs/best_practices/reporting_template.md) - Present findings
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices

## 🎨 Visualization Best Practices
- Choose appropriate chart types
- Use color purposefully
- Label axes clearly
- Provide context (titles, annotations)
- Make it accessible (colorblind-friendly)

## ✨ Checkpoint
Before moving to Module 08, ensure:

**Track A (Classification):**
- [ ] Confusion matrix and ROC curves created
- [ ] Classification performance visualizations complete
- [ ] Interactive classification dashboard prototyped
- [ ] Streamlit app shows real-time availability predictions
- [ ] Stakeholder-friendly alert displays implemented

**Track B (Regression/Time Series):**
- [ ] Forecast plots with uncertainty bands created
- [ ] Residual analysis visualizations complete
- [ ] Interactive forecast dashboard prototyped
- [ ] Streamlit app shows multi-day forecasts
- [ ] Uncertainty communication clear and intuitive

**Both Tracks:**
- [ ] Static publication-quality plots exported
- [ ] Interactive Plotly/Bokeh charts functional
- [ ] Dashboard tested with sample users
- [ ] Visualizations accessible and colorblind-friendly

---
**Next Module:** Module 08 - Automation  
- **Track A:** Classification prediction pipelines
- **Track B:** Time series forecasting pipelines
