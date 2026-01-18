# Module 02: Data Acquisition

## 📌 Module Overview
Learn how to acquire data from various sources including APIs, open data portals, and local files. This module lays the **foundation for both learning tracks** — all students work with the same data sources.

**🎯 Dual-Track Context**: This is a **foundation module** (shared by Track A and Track B). You'll learn about the OV-fiets system's operational constraints, which will help you understand the two prediction problems we'll explore in Module 3.

**📖 Start Here**: Read [MODULE_02_OVERVIEW.md](MODULE_02_OVERVIEW.md) first! It covers:
- Why data acquisition matters (80% of data science work!)
- Common challenges and solutions
- REST API concepts and best practices
- Module learning objectives and structure
---

## � Learning Path

**Module 1 Taught You**: In Module 1, you learned the fundamentals:
- How to make API requests with `requests.get()`
- How to parse JSON responses
- How to convert data to DataFrames
- How to handle basic errors

**This Module's Focus**: **Practice and apply** what you learned! Write your own code to:
- Fetch bike data from CityBikes API
- Fetch weather data from Open-Meteo API
- Store and manage data files
- Merge datasets with different time granularities

**Your Journey**:
1. **Module 1**: Learned concepts through guided examples
2. **Now (Module 2)**: Practice with scaffolded exercises → Build confidence

> 💡 **Tip**: Each notebook has exercises with TODO markers. Try them first, then check the solutions!

---

## 🎓 Course Development Strategy

### Pedagogical Approach for This Module
Module 2 uses **reduced scaffolding** for M2_01 & M2_02 (building on M1) and **progressive scaffolding** for M2_03 & M2_04 (new concepts).

**M2_01 & M2_02 Strategy (Apply M1 Knowledge):**
- **Scaffolding**: 20-40% - Force recall and application from Module 1
- **Rationale**: If taught in M1, provide hints only (no templates)
- **Goal**: Identify gaps early, build independence, genuine skill development
- **Approach**: Review M1 → Attempt with hints → Verify with solutions

**M2_03 & M2_04 Strategy (New Concepts):**
- **Scaffolding**: 70% → 30% progressive through 5 parts
- **Rationale**: Lower entry barrier for new material
- **Goal**: Learn patterns first, then practice independently
- **Approach**: Observe → Guided practice → Independent application

**Progressive Difficulty (All Notebooks):**
- Part 1: Setup & Introduction (90% complete)
- Part 2: Guided Practice (70% for new, 30% for review)
- Part 3: Moderate Challenge (50%)
- Part 4: Independent Work (30%)
- Part 5: Advanced Challenge (10% + optional tasks)

**Solution Notebooks:**
- `M2_01_SOLUTIONS.ipynb` through `M2_04_SOLUTIONS.ipynb`
- Use AFTER attempting tasks yourself
- Available for when genuinely stuck
- Shows alternative approaches

**Optional Challenges:**
- Build retry decorators, multi-API comparisons
- Design data lineage trackers
- Real-world integration scenarios

---

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Fetch data from REST APIs
- Access open data portals (Amsterdam OV-fiets, weather)
- Handle API authentication and rate limits
- Save and load data locally
- Combine data from multiple sources
- **NEW:** Understand OV-fiets operational constraints (15-min refresh, no docking stations, same-station returns)
- **NEW:** Identify patterns that suggest two distinct use cases (commuter vs tourist)

## 📚 Module Content

### 📄 MODULE_02_OVERVIEW.md (Read First!)
- Conceptual foundation for data acquisition
- REST API deep dive with diagrams
- File format comparisons
- Data flow architecture
- Best practices and security

### 📓 Notebooks (Work Through in Order)

#### M2_01_amsterdam_bike_api.ipynb
- **Your Task**: Fetch bike data from CityBikes API (practice M1 concepts!)
- **Exercises**: API requests, error handling, DataFrame conversion
- Connect to CityBikes API (fetch Amsterdam networks)
- Understand API structure and endpoints
- Fetch real-time bike availability data
- Handle API responses

#### M2_02_weather_data_api.ipynb
- **Your Task**: Fetch weather data from Open-Meteo API (more practice!)
- **Exercises**: Weather API calls, DataFrame conversion, bikeability scoring
- Access Open-Meteo weather API
- Fetch historical weather data
- Understand weather variables
- Match weather data to bike data timestamps

#### M2_03_data_storage.ipynb
- Explore different file formats (CSV, JSON, Parquet, Feather)
- Implement data versioning strategies
- Create a data catalog system
- Best practices for raw vs processed data

#### M2_04_merge_datasets.ipynb
- **New Concept**: Time-aligned data merging
- Combine bike and weather datasets
- Handle different time granularities
- Validate merged results

### 📝 MODULE_02_SELF_EVALUATION.md (Complete at End)
- Self-assessment checklist
- Learning objectives review
- Reflection questions
- Next steps preparation

---

## 🎯 Learning Sequence

**Recommended Order:**
1. 📖 Read [MODULE_02_OVERVIEW.md](MODULE_02_OVERVIEW.md) - Get the big picture
2. 💻 M2_01 - Practice API fetching with bike data
3. 💻 M2_02 - Practice API fetching with weather data
4. 💻 M2_03 - Learn storage best practices
5. 💻 M2_04 - Master data merging
6. ✅ Complete [MODULE_02_SELF_EVALUATION.md](MODULE_02_SELF_EVALUATION.md)

---

## 📝 Naming Convention
Follow this pattern: `M2_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Check [open data sources](../../docs/references/open_data_sources.md) for data links
- Reference [code snippets](../../docs/references/code_snippets.md) for API examples
- Always save raw data before processing
- Follow [coding standards](../../docs/standards/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `requests` - API calls
- `pandas` - Data manipulation
- `json` - JSON handling

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 🌐 [Open Data Sources](../../docs/references/open_data_sources.md) - Where to get data
- � [OV-fiets System Overview](../../docs/guides/ov_fiets_system_overview.md) - **NEW:** Understanding the domain
- 📚 [Code Snippets](../../docs/references/code_snippets.md) - API and data loading examples
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Best practices
- 📊 [Data Organization](../../data/README.md) - How to structure data

## ✨ Checkpoint
Before moving to Module 03, ensure:
- [ ] You can fetch data from at least one API
- [ ] Raw data is saved in `data/raw/`
- [ ] You have both bike and weather data
- [ ] Data sources are documented
- [ ] **NEW:** You understand OV-fiets operational constraints (no docks, 15-min refresh, same-station returns)

## 🔜 What's Next?
**Module 3 Preview**: In the next module, you'll explore this data and discover **two distinct rental patterns** — commuters (short-term) and tourists (multi-day). At the end of Module 3, you'll choose your learning track:
- **Track A (Beginner):** Classification for short-term predictions
- **Track B (Advanced):** Regression + Time series for long-term forecasting

💡 **Tip:** Keep the operational constraints in mind as you explore patterns in Module 3!
- [ ] Code is clean and well-documented

---
**Next Module:** Module 03 - Exploration & Profiling
