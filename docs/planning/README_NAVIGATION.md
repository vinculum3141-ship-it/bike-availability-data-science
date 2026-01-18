# 🗺️ README Navigation Guide

This document provides a comprehensive map of all README files in the repository and their relationships.

---

## 📚 Entry Points Overview

This repository contains **30+ README files** organized hierarchically. Each serves as an entry point for different aspects of the project.

**NEW:** This course now offers **dual-track learning** with flexible pathways. See [Learning Pathways Guide](learning_pathways.md) for details.

---

## 🏠 Main Entry Point

### [README.md](../README.md) - **Project Home**
**Purpose**: Main entry point for the entire repository  
**Audience**: Everyone (students, instructors, contributors)  
**Key Sections**:
- **NEW:** Dual-track introduction (Track A: Classification, Track B: Regression + Time Series)
- Project overview and Smart Cities framing
- Prerequisites and time commitment
- What You'll Learn (core + track-specific skills)
- Quick Start guide
- Setup instructions
- Learning resources (including track selection guides)
- Capstone project info

**Links to**:
- **NEW:** Learning Pathways Guide, Use Case Comparison, OV-fiets System Overview, Course Structure
- All module READMEs
- Documentation guides
- Capstone guidelines
- Data directories

---

## 📓 Notebook Documentation

### [notebooks/README.md](../notebooks/README.md) - **Notebook Hub**
**Purpose**: Guide for working with Jupyter notebooks  
**Audience**: Students creating notebooks  
**Key Sections**:
- Module structure table (10 modules)
- Notebook template usage
- Naming conventions
- Setup cell template
- Workflow for each module
- Quality checklist

**Links to**:
- Each module README
- Notebook template
- Example notebook
- Coding standards
- Code snippets
- All docs guides

---

## 🗂️ Module READMEs (10 Total)

Each module README follows a consistent structure with learning objectives, tasks, tips, resources, and checkpoints.

### Module 01: Introduction
**[notebooks/Module_01_Introduction/README.md](../notebooks/Module_01_Introduction/README.md)**  
**Focus**: Project setup, problem definition  
**Key Tasks**: Project intro, environment setup, problem definition  
**Special Resources**: Colab setup, dependency management

### Module 02: Data Acquisition
**[notebooks/Module_02_Data_Acquisition/README.md](../notebooks/Module_02_Data_Acquisition/README.md)**  
**Focus**: APIs, data collection, storage  
**Key Tasks**: API connections, data downloads, storage  
**Special Resources**: Open data sources, data organization guide

### Module 03: Exploration & Profiling
**[notebooks/Module_03_Exploration_Profiling/README.md](../notebooks/Module_03_Exploration_Profiling/README.md)**  
**Focus**: EDA, profiling, patterns  
**Key Tasks**: Data profiling, distribution analysis, quality checks  
**Special Resources**: Example EDA notebook, visualization snippets  
**NEW:** Module 3 includes **track selection decision point** at the end

### Module 04: Feature Engineering 🔀 **TRACK DIVERGENCE**
**[notebooks/Module_04_Feature_Engineering/README.md](../notebooks/Module_04_Feature_Engineering/README.md)**  
**Focus**: Creating meaningful features  
**Track A (Classification)**: Time features, weather features, train schedules (short-term prediction)  
**Track B (Regression/TS)**: Extended temporal features, weather forecasts, event calendars, lag features (long-term prediction)  
**Special Resources**: Feature engineering snippets, data leakage warnings  
**NEW:** Contains sub-track folders: `track_a_commuter/` and `track_b_multiday/`

### Module 05: Modeling 🔀 **TRACKS CONTINUE**
**[notebooks/Module_05_Modeling/README.md](../notebooks/Module_05_Modeling/README.md)**  
**Focus**: Training ML models  
**Track A (Classification)**: Logistic Regression, Random Forest Classifier, XGBoost, classification metrics  
**Track B (Regression/TS)**: Linear/Ridge Regression, Random Forest Regressor, ARIMA, Prophet, uncertainty quantification  
**Special Resources**: Model training snippets, experiment tracking guide  
**NEW:** Contains sub-track folders: `track_a_classification/` and `track_b_regression/`

### Module 06: Validation & Governance 🔗 **TRACKS CONVERGE**
**[notebooks/Module_06_Validation_Governance/README.md](../notebooks/Module_06_Validation_Governance/README.md)**  
**Focus**: Testing, documentation, governance  
**Key Tasks**: Model validation (classification or regression), error analysis, interpretability, documentation  
**Special Resources**: Model documentation guidelines, evaluation snippets  
**NEW:** Includes track-specific validation examples

### Module 07: Visualization
**[notebooks/Module_07_Visualization/README.md](../notebooks/Module_07_Visualization/README.md)**  
**Focus**: Dashboards, communication  
**Key Tasks**: Static plots, interactive viz, dashboard prototypes  
**Special Resources**: Reporting template, visualization snippets

### Module 08: Automation
**[notebooks/Module_08_Automation/README.md](../notebooks/Module_08_Automation/README.md)**  
**Focus**: Pipelines, reproducibility  
**Key Tasks**: Pipeline design, automation, testing, deployment  
**Special Resources**: Pipeline snippets, automation examples

### Module 09: Experimentation
**[notebooks/Module_09_Experimentation/README.md](../notebooks/Module_09_Experimentation/README.md)**  
**Focus**: MLflow, tracking, tuning  
**Key Tasks**: MLflow setup, experiment tracking, hyperparameter tuning  
**Special Resources**: Experiment best practices, MLflow snippets

### Module 10: Collaboration
**[notebooks/Module_10_Collaboration/README.md](../notebooks/Module_10_Collaboration/README.md)**  
**Focus**: Git, code review, deployment  
**Key Tasks**: Version control, code review, documentation, deployment  
**Special Resources**: reporting template

---

## 📊 Data Documentation

### [data/README.md](../data/README.md) - **Data Hub**
**Purpose**: Explain data organization and workflows  
**Audience**: Students working with datasets  
**Key Sections**:
- Directory structure (raw/ and processed/)
- Data organization guidelines
- Naming conventions
- Data sources table
- Security and privacy rules
- Pipeline flow diagram
- Code snippets for loading/saving
- Validation checklist

**Links to**:
- raw/README.md
- processed/README.md
- Open data sources
- Code snippets
- Coding standards
- Dependency management
- Module 02-04 (data acquisition through feature engineering)

### [data/raw/README.md](../data/raw/README.md) - **Raw Data Guide**
**Purpose**: Document raw data organization  
**Key Content**: File naming, data sources, storage guidelines

### [data/processed/README.md](../data/processed/README.md) - **Processed Data Guide**
**Purpose**: Document processed data organization  
**Key Content**: Transformation tracking, versioning, formats

---

## 📋 Documentation Guides (10+ Files)

### Track Selection & Learning Pathways 🎯 **NEW**

#### [docs/guides/learning_pathways.md](../guides/learning_pathways.md)
**Purpose**: Visualize complete learning journeys for both tracks  
**Covers**: Track A vs Track B pathways, self-assessment, milestones, learning strategies

#### [docs/guides/use_case_comparison.md](../guides/use_case_comparison.md)
**Purpose**: Compare commuter vs tourist prediction problems  
**Covers**: Decision tree, prerequisites checklist, feature comparison, capstone options

#### [docs/guides/ov_fiets_system_overview.md](../guides/ov_fiets_system_overview.md)
**Purpose**: Domain knowledge for OV-fiets bike-sharing system  
**Covers**: No-dock system, operational constraints, user populations, data characteristics

#### [docs/guides/course_structure_dual_track.md](../guides/course_structure_dual_track.md)
**Purpose**: Full course structure with dual-track organization  
**Covers**: Module-by-module breakdown, track divergence/convergence, learning pathways

### Setup & Environment

### [docs/standards/coding_standards.md](../standards/coding_standards.md)
**Purpose**: Python and data science coding standards  
**Covers**: PEP 8, naming, docstrings, DS-specific patterns, before/after examples

### [docs/code_snippets.md](../docs/code_snippets.md)
**Purpose**: Quick reference for common tasks  
**Covers**: Data loading, cleaning, feature engineering, visualization, ML code

### [docs/dependency_management.md](../docs/dependency_management.md)
**Purpose**: Package installation and management  
**Covers**: requirements.txt, virtual environments, troubleshooting

### [docs/open_data_sources.md](../docs/open_data_sources.md)
**Purpose**: List of data sources for the project  
**Covers**: Bike sharing, weather, geographic, event data sources

### [docs/experiment_best_practices.md](../docs/experiment_best_practices.md)
**Purpose**: MLflow and experiment tracking guide  
**Covers**: MLflow setup, tracking experiments, comparing runs, best practices

### [docs/model_documentation_guidelines.md](../docs/model_documentation_guidelines.md)
**Purpose**: How to document ML models  
**Covers**: Model cards, documentation templates, governance

### [docs/reporting_template.md](../docs/reporting_template.md)
**Purpose**: Stakeholder reporting guide  
**Covers**: Executive summaries, technical details, recommendations

### [docs/setup_google_colab.md](../docs/setup_google_colab.md)
**Purpose**: Google Colab setup instructions  
**Covers**: Colab basics, installing packages, mounting data, GPU usage

---

## 🎓 Capstone Documentation

### [capstone/capstone_guidelines.md](../capstone/capstone_guidelines.md)
**Purpose**: Complete capstone project requirements  
**Covers**: Objectives, deliverables, timeline, submission guidelines

### [capstone/self_evaluation.md](../capstone/self_evaluation.md)
**Purpose**: Self-assessment tool for students  
**Covers**: Checklist, quality questions, reflection, and scoring guide

---

## 🔄 Cross-Reference Map

### Quick Reference: Where to Find What

| Need | Start Here |
|------|-----------|
| **Getting started** | [Main README](../README.md) → Quick Start |
| **Create a notebook** | [notebooks/README.md](../notebooks/README.md) → Workflow section |
| **Module tasks** | Specific [Module README](../notebooks/) |
| **Code examples** | [code_snippets.md](../docs/code_snippets.md) |
| **Code quality** | [coding_standards.md](../docs/coding_standards.md) |
| **Setup environment** | [Main README](../README.md) + [dependency_management.md](../docs/dependency_management.md) |
| **Find data** | [open_data_sources.md](../docs/open_data_sources.md) |
| **Organize data** | [data/README.md](../data/README.md) |
| **Track experiments** | [experiment_best_practices.md](../docs/experiment_best_practices.md) |
| **Document models** | [model_documentation_guidelines.md](../docs/model_documentation_guidelines.md) |
| **Create reports** | [reporting_template.md](../docs/reporting_template.md) |
| **Use Colab** | [setup_google_colab.md](../docs/setup_google_colab.md) |
| **Capstone project** | [capstone_guidelines.md](../capstone/capstone_guidelines.md) |

---

## 📖 Recommended Reading Order

### For New Students

1. **[Main README](../README.md)** - Understand the project
2. **[Quick Start](../README.md#-quick-start)** - Follow the 6-step guide
3. **[notebooks/README.md](../notebooks/README.md)** - Learn the workflow
4. **[coding_standards.md](../docs/coding_standards.md)** - Learn best practices
5. **[Module 01 README](../notebooks/Module_01_Introduction/README.md)** - Start the course
6. Follow modules 02-10 in order

### For Quick Reference

1. **[code_snippets.md](../docs/code_snippets.md)** - Copy-paste solutions
2. **[Module README](../notebooks/)** for current module - See tasks
3. **[notebook template](../notebooks/notebook_template.ipynb)** - Structure
4. **[example notebook](../notebooks/example_data_exploration.ipynb)** - Learn by example

### For Instructors

1. **[Main README](../README.md)** - Overall structure
2. **[capstone_guidelines.md](../capstone/capstone_guidelines.md)** - Project requirements
3. **[self_evaluation.md](../capstone/self_evaluation.md)** - Student self-assessment tool
4. All module READMEs - Review learning objectives

---

## 🧩 README Interdependencies

### Module README Dependencies
Each module README references:
- ✅ Notebook template (for structure)
- ✅ Coding standards (for quality)
- ✅ Code snippets (for examples)
- ✅ Specific docs relevant to that module

### Common References Across All Modules
- **[notebook_template.ipynb](../notebooks/notebook_template.ipynb)** - Referenced in all 10 modules
- **[coding_standards.md](../docs/coding_standards.md)** - Referenced in all 10 modules
- **[code_snippets.md](../docs/code_snippets.md)** - Referenced in all 10 modules

### Module-Specific Documentation Links
- **Module 02** → open_data_sources.md, data/README.md
- **Module 03** → example_data_exploration.ipynb
- **Module 05** → experiment_best_practices.md
- **Module 06** → model_documentation_guidelines.md
- **Module 07** → reporting_template.md
- **Module 09** → experiment_best_practices.md
- **Module 10** → reporting_template.md

---

## ✅ Consistency Checklist

All READMEs have been reviewed for:
- [x] Consistent formatting and structure
- [x] Working cross-references to new materials
- [x] References to notebook template
- [x] References to coding standards
- [x] References to code snippets
- [x] Clear purpose and audience
- [x] Logical information flow
- [x] No broken links
- [x] Updated resource sections

---

## 🔍 Search Strategy

### By Topic
- **Setup**: Main README → dependency_management.md → Module 01
- **Data**: data/README.md → open_data_sources.md → Module 02
- **Coding**: coding_standards.md → code_snippets.md
- **ML**: Module 05 → experiment_best_practices.md → model_documentation_guidelines.md
- **Visualization**: Module 07 → reporting_template.md
- **Deployment**: Module 10

### By Role
- **Beginner**: Main README → Quick Start → Module 01
- **Developer**: coding_standards.md → code_snippets.md → module READMEs
- **Data Scientist**: data/README.md → modules 02-09
- **ML Engineer**: modules 05, 08, 09 → experiment_best_practices.md
- **Student (Capstone)**: capstone_guidelines.md → self_evaluation.md

---

**Navigation Tip**: Use your editor's "Go to File" (Ctrl+P / Cmd+P) feature to quickly open any README by typing "readme" and the folder name! 🚀
