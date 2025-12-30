# Module 02: Data Acquisition

## 📌 Module Overview
Learn how to acquire data from various sources including APIs, open data portals, and local files.

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- Fetch data from REST APIs
- Access open data portals (Amsterdam, KNMI weather)
- Handle API authentication and rate limits
- Save and load data locally
- Combine data from multiple sources

## ✅ Your Tasks
Create the following notebooks in this folder:

### M2_01_amsterdam_bike_api.ipynb
- Connect to Amsterdam bike-sharing API
- Understand API structure and endpoints
- Fetch real-time bike availability data
- Handle API responses

### M2_02_weather_data_api.ipynb
- Access KNMI (Dutch weather service) API
- Fetch historical weather data
- Understand weather variables
- Match weather data to bike data timestamps

### M2_03_data_storage.ipynb
- Save raw data to `data/raw/`
- Choose appropriate file formats (CSV, JSON, Parquet)
- Implement data versioning
- Document data sources

### M2_04_merge_datasets.ipynb
- Merge bike and weather data
- Handle different time granularities
- Deal with missing timestamps
- Validate merged dataset

## 📝 Naming Convention
Follow this pattern: `M2_{number}_{description}.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Use the `src/data_acquisition.py` module for reusable functions
- Store API keys in environment variables (never commit them!)
- Check [open data sources](../../docs/open_data_sources.md) for data links
- Reference [code snippets](../../docs/code_snippets.md) for API examples
- Always save raw data before processing
- Follow [coding standards](../../docs/coding_standards.md) for clean code

## 📚 Key Libraries & Resources
**Libraries**:
- `requests` - API calls
- `pandas` - Data manipulation
- `json` - JSON handling

**Documentation**:
- 📓 [Notebook Template](../notebook_template.ipynb) - Start here
- 🌐 [Open Data Sources](../../docs/open_data_sources.md) - Where to get data
- 📚 [Code Snippets](../../docs/code_snippets.md) - API and data loading examples
- 📐 [Coding Standards](../../docs/coding_standards.md) - Best practices
- 📊 [Data Organization](../../data/README.md) - How to structure data

## ✨ Checkpoint
Before moving to Module 03, ensure:
- [ ] You can fetch data from at least one API
- [ ] Raw data is saved in `data/raw/`
- [ ] You have both bike and weather data
- [ ] Data sources are documented
- [ ] No API keys are committed to git

---
**Next Module:** Module 03 - Exploration & Profiling
