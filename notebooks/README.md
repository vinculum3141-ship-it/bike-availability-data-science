# 📓 Notebooks Directory

This directory contains all course modules and example notebooks to guide your learning journey.

---

## �️ Module Structure

The course is organized into 10 modules covering the complete data science lifecycle:

| Module | Topic | Focus |
|--------|-------|-------|
| [Module 01](Module_01_Introduction/) | Introduction | Project setup, problem definition |
| [Module 02](Module_02_Data_Acquisition/) | Data Acquisition | APIs, data collection, storage |
| [Module 03](Module_03_Exploration_Profiling/) | Exploration | EDA, profiling, patterns |
| [Module 04](Module_04_Feature_Engineering/) | Feature Engineering | Creating meaningful features |
| [Module 05](Module_05_Modeling/) | Modeling | Training ML models |
| [Module 06](Module_06_Validation_Governance/) | Validation | Testing, documentation, governance |
| [Module 07](Module_07_Visualization/) | Visualization | Dashboards, communication |
| [Module 08](Module_08_Automation/) | Automation | Pipelines, reproducibility |
| [Module 09](Module_09_Experimentation/) | Experimentation | MLflow, tracking, tuning |
| [Module 10](Module_10_Collaboration/) | Collaboration | Git, code review, deployment |

**📖 Each module folder contains a README** with:
- Learning objectives
- Specific tasks to complete
- Suggested notebook names
- Key concepts and resources
- Checkpoint criteria

---

## 📓 Getting Started with Notebooks

### 1. Use the Template

Start every notebook from our template:

**📄 [notebook_template.ipynb](notebook_template.ipynb)**

This template includes:
- Standard setup and imports
- Configuration section
- Data loading structure
- Analysis sections
- Results and summary

**To use**: Copy the template and rename following the naming convention below.

### 2. Learn from the Example

See best practices in action:

**🎓 [example_data_exploration.ipynb](example_data_exploration.ipynb)**

This working example demonstrates:
- Complete data exploration workflow
- Professional code organization
- Multiple visualization types
- Proper documentation
- Summary and insights

---

## 📝 Notebook Naming Convention

Use this pattern inside each module folder:

```
M{module}_{number}_{description}.ipynb
```

**Examples**:
```
Module_02_Data_Acquisition/
├── M2_01_amsterdam_bike_api.ipynb
├── M2_02_weather_data_api.ipynb
├── M2_03_data_storage.ipynb
└── M2_04_merge_datasets.ipynb
```

**Benefits**:
- ✅ Clear learning sequence
- ✅ Easy navigation
- ✅ Consistent organization
- ✅ Simple grading/review

---

## 🔧 Notebook Setup Cell

Every notebook should include this setup cell at the beginning:

```python
# ═══════════════════════════════════════════════════════════
# NOTEBOOK SETUP - Run This Cell First!
# ═══════════════════════════════════════════════════════════

import sys
import os
from datetime import datetime

# Standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure display
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-darkgrid')
%matplotlib inline

# Check if running in Google Colab
if 'google.colab' in sys.modules:
    print("📍 Running in Google Colab")
    # Uncomment to install requirements
    # !pip install -q -r ../requirements.txt
else:
    print("📍 Running locally")

# Add project root to path
project_root = os.path.abspath('..' if 'notebooks' in os.getcwd() else '.')
if project_root not in sys.path:
    sys.path.append(project_root)

print("✅ Setup complete!")
```

---

## 🎯 Workflow for Each Module

### Step 1: Read the Module README
Start by reading the README in each module folder for:
- Learning objectives
- Tasks to complete
- Suggested notebook structure

### Step 2: Copy the Template
```bash
cp notebook_template.ipynb Module_XX/MX_01_your_topic.ipynb
```

### Step 3: Follow the Structure
Use the template sections:
1. Setup & Imports
2. Configuration
3. Data Loading
4. Analysis (your work here)
5. Save Results
6. Summary

### Step 4: Reference Resources
As you work, use:
- [Code Snippets](../docs/code_snippets.md) - Quick copy-paste solutions
- [Coding Standards](../docs/coding_standards.md) - Best practices
- [Example Notebook](example_data_exploration.ipynb) - Working example

### Step 5: Complete Checkpoint
Before moving to the next module, verify the checkpoint criteria in the module README.

---

## 📚 Additional Resources

### Templates & Examples
- 📓 [Notebook Template](notebook_template.ipynb) - Your starting point
- 🎓 [Example Notebook](example_data_exploration.ipynb) - Best practices demo

### Documentation
- 📐 [Coding Standards](../docs/coding_standards.md) - Write clean code
- 📚 [Code Snippets](../docs/code_snippets.md) - Common operations
- 🔧 [Google Colab Setup](../docs/setup_google_colab.md) - Cloud setup

### Data & Sources
- 🌐 [Open Data Sources](../docs/open_data_sources.md) - Where to get data
- 📊 [Data README](../data/README.md) - Data organization

### Best Practices
- 🧪 [Experiment Tracking](../docs/experiment_best_practices.md) - MLflow guide
- 📋 [Model Documentation](../docs/model_documentation_guidelines.md) - Document models
- 📈 [Reporting Template](../docs/reporting_template.md) - Present findings

---

## 💡 Tips for Success

### Do's ✅
- ✅ Start each notebook with the setup cell
- ✅ Follow the naming convention
- ✅ Use descriptive variable names
- ✅ Add markdown cells to explain your thinking
- ✅ Save your work frequently
- ✅ Test code with small samples first
- ✅ Document your findings

### Don'ts ❌
- ❌ Skip the setup cell
- ❌ Use generic variable names (df1, df2)
- ❌ Leave notebooks without explanations
- ❌ Commit without running "Restart & Run All"
- ❌ Hardcode file paths
- ❌ Forget to add summaries

---

## 🆘 Getting Help

**Stuck on something?**
1. Check the module README for guidance
2. Review the example notebook
3. Search the code snippets guide
4. Review the coding standards
5. Check [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## ✨ Quality Checklist

Before considering a notebook complete:

- [ ] Follows naming convention
- [ ] Has setup cell at the beginning
- [ ] Uses clear variable names
- [ ] Includes markdown explanations
- [ ] All cells run without errors (Restart & Run All)
- [ ] Has a summary section
- [ ] Findings are documented
- [ ] Figures have titles and labels
- [ ] Code follows standards
- [ ] No hardcoded paths or credentials

---

**Ready to start?** Head to [Module 01](Module_01_Introduction/) and begin your data science journey! 🚀
