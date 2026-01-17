# 📊 Module 02 Overview: Data Acquisition & Integration

**Module**: Module 02 - Data Acquisition  
**Prerequisites**: Module 01 complete  
**Estimated Time**: 6-8 hours  
**Difficulty**: Beginner to Intermediate

---

## 🎯 Module Purpose

This module teaches you how to **acquire real-world data from multiple sources** and **integrate them into a unified dataset** ready for analysis. You'll work with live APIs, understand data schemas, handle errors, and establish best practices for data storage.

---

## 💡 Why Data Acquisition Matters

### The Reality of Data Science

In real-world data science:
- 📊 **80% of time is spent** on data acquisition and cleaning
- 🌐 **Data is scattered** across multiple sources and formats
- ⏱️ **APIs have limits** - rate limits, authentication, downtime
- 🔄 **Data changes** - you need reproducible pipelines
- 📝 **Documentation is critical** - track what data came from where

### Common Challenges

1. **Schema Mismatches**
   - Bike data: hourly snapshots
   - Weather data: 10-minute intervals
   - **Solution**: Time alignment and aggregation

2. **Missing Data**
   - API downtime
   - Network errors
   - Incomplete historical records
   - **Solution**: Retry logic, fallbacks, validation

3. **Data Quality**
   - Incorrect timestamps
   - Invalid values (negative bikes?)
   - Duplicate records
   - **Solution**: Validation checks, data cleaning

4. **Reproducibility**
   - How to re-run the same analysis?
   - Version control for data
   - **Solution**: Scripts, documentation, versioning

---

## 🎓 Learning Objectives

By the end of this module, you will be able to:

### Technical Skills ✅
- [ ] Fetch data from REST APIs with proper error handling
- [ ] Parse JSON and CSV responses
- [ ] Implement retry logic for failed requests
- [ ] Validate data quality and completeness
- [ ] Save data in appropriate formats (CSV, JSON, Parquet)
- [ ] Merge datasets with different time granularities
- [ ] Handle missing timestamps and data gaps

### Best Practices ✅
- [ ] Organize raw vs. processed data
- [ ] Document data sources and transformations
- [ ] Never commit API keys to git
- [ ] Use environment variables for configuration
- [ ] Version your datasets
- [ ] Write reproducible data pipelines

### Data Science Thinking ✅
- [ ] Understand the difference between file-based and API-based data
- [ ] Plan for data quality issues early
- [ ] Design schemas before acquisition
- [ ] Think about time alignment challenges
- [ ] Consider rate limits and API constraints

---

## 📚 What You'll Build

### Four Core Notebooks

1. **M2_01: Amsterdam Bike API** 🚴
   - Connect to CityBikes API
   - Fetch real-time bike availability
   - Handle API responses
   - Save raw JSON data
   - **Output**: `data/raw/amsterdam_bike_{date}.json`

2. **M2_02: Weather Data API** 🌦️
   - Connect to Open-Meteo API
   - Fetch historical weather data
   - Parse weather variables
   - Save raw CSV data
   - **Output**: `data/raw/weather_{date}.csv`

3. **M2_03: Data Storage Patterns** 💾
   - Compare file formats (CSV vs JSON vs Parquet)
   - Implement versioning strategies
   - Set up `.gitignore` correctly
   - Document data lineage
   - **Output**: `data/processed/bike_clean.parquet`

4. **M2_04: Merge Datasets** 🔗
   - Time alignment strategies
   - Handle missing timestamps
   - Validate merged data
   - Create final integrated dataset
   - **Output**: `data/processed/merged_bike_weather.parquet`

---

## 🔄 Data Flow Diagram

```
┌─────────────────┐         ┌─────────────────┐
│  CityBikes API  │         │ Open-Meteo API  │
│   (Bike Data)   │         │ (Weather Data)  │
└────────┬────────┘         └────────┬────────┘
         │                           │
         │ M2_01                     │ M2_02
         │ fetch_bike_data()         │ fetch_weather_data()
         ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│   data/raw/     │         │   data/raw/     │
│  bike_*.json    │         │ weather_*.csv   │
└────────┬────────┘         └────────┬────────┘
         │                           │
         │ M2_03                     │ M2_03
         │ clean & validate          │ clean & validate
         ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│ data/processed/ │         │ data/processed/ │
│ bike_clean.pqt  │         │weather_clean.pqt│
└────────┬────────┘         └────────┬────────┘
         │                           │
         └───────────┬───────────────┘
                     │ M2_04
                     │ merge_datasets()
                     ▼
         ┌─────────────────────┐
         │  data/processed/    │
         │ merged_bike_weather │
         │      .parquet       │
         └─────────────────────┘
```

---

## 🆚 File-Based vs API-Based Data

### File-Based Data Sources

**Examples**: Downloaded CSVs, Excel files, archived data

**Advantages** ✅
- Simple to work with
- No rate limits
- Offline access
- Consistent format

**Disadvantages** ❌
- Quickly becomes outdated
- Manual updates required
- Large file sizes
- Version control issues

**When to Use**:
- Historical/static datasets
- One-time analyses
- Educational projects with sample data

---

### API-Based Data Sources

**Examples**: REST APIs, real-time data streams

**Advantages** ✅
- Always up-to-date
- Automated data collection
- Only fetch what you need
- No storage overhead

**Disadvantages** ❌
- Rate limits
- Requires authentication (sometimes)
- Network dependency
- API changes over time
- More complex error handling

**When to Use**:
- Real-time monitoring
- Automated pipelines
- Dynamic data that changes frequently

---

## 🔧 Key Technical Concepts

### 1. REST APIs

**What is a REST API?**
- **RE**presentational **S**tate **T**ransfer
- Standard way to access data over HTTP
- Uses URLs (endpoints) to request specific data
- Returns data in JSON or XML format

**Example Request**:
```python
import requests

url = "http://api.citybik.es/v2/networks/ns-bike-amsterdam"
response = requests.get(url)
data = response.json()
```

### 2. JSON Format

**JavaScript Object Notation** - human-readable data format

**Structure**:
```json
{
  "network": {
    "name": "NS Bike",
    "stations": [
      {
        "id": "123",
        "name": "Central Station",
        "bikes_available": 5,
        "timestamp": "2026-01-15T10:00:00Z"
      }
    ]
  }
}
```

### 3. Rate Limiting

**Why?** APIs limit requests to prevent abuse and ensure fair usage.

**Common Limits**:
- 60 requests per hour (GitHub)
- 1000 requests per day (OpenWeatherMap free tier)
- 10 requests per second (some APIs)

**Best Practices**:
```python
import time

def fetch_with_rate_limit(url, delay=1.0):
    """Fetch data with delay between requests."""
    response = requests.get(url)
    time.sleep(delay)  # Wait before next request
    return response
```

### 4. Error Handling

**Common Errors**:
- `404 Not Found` - Resource doesn't exist
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - API is down
- `ConnectionError` - Network problems

**Best Practices**:
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise exception for bad status
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    data = None
```

### 5. Data Validation

**Always validate**:
- ✅ Data types (int, float, string)
- ✅ Value ranges (bikes_available >= 0)
- ✅ Required fields present
- ✅ Timestamps in correct format
- ✅ No duplicates

```python
def validate_bike_data(df):
    """Validate bike availability data."""
    assert 'bikes_available' in df.columns, "Missing bikes_available"
    assert (df['bikes_available'] >= 0).all(), "Negative bike count"
    assert df['timestamp'].notna().all(), "Missing timestamps"
    return True
```

---

## 💾 Data Storage Best Practices

### File Formats Comparison

| Format | Use Case | Pros | Cons |
|--------|----------|------|------|
| **CSV** | Simple tabular data | Human-readable, universal | Large file size, no type info |
| **JSON** | Nested/hierarchical data | Flexible, preserves structure | Verbose, slower to parse |
| **Parquet** | Large datasets | Compressed, fast, typed | Not human-readable |

**Recommendation**: 
- 📁 Raw data → JSON/CSV (preserve original format)
- 📊 Processed data → Parquet (efficient storage)

### Directory Structure

```
data/
├── raw/                          # Never modify these
│   ├── amsterdam_bike_2026-01-15.json
│   ├── weather_2026-01-15.csv
│   └── README.md                 # Document each file
│
└── processed/                    # Transformed data
    ├── bike_clean_v1.parquet
    ├── weather_clean_v1.parquet
    ├── merged_v1.parquet
    └── README.md                 # Document transformations
```

### Versioning Strategy

**Filename Convention**:
```
{source}_{description}_{YYYY-MM-DD}_v{version}.{ext}

Examples:
- amsterdam_bike_2026-01-15_v1.json
- weather_hourly_2026-01-15_v2.csv
- merged_bike_weather_v3.parquet
```

---

## 🛡️ Security & Privacy

### ❌ NEVER Commit to Git

- API keys
- Passwords
- Personal data
- Large data files (> 100MB)

### ✅ Use Environment Variables

**Note**: The APIs in this course (CityBikes, Open-Meteo, KNMI) don't require authentication, but understanding secret management is important for future projects.

---

## 📖 Module Structure

### Notebooks

| Notebook | Focus | Time | Output |
|----------|-------|------|--------|
| M2_01 | Bike API | 90-120 min | `data/raw/bike_*.json` |
| M2_02 | Weather API | 90-120 min | `data/raw/weather_*.csv` |
| M2_03 | Storage Patterns | 60-90 min | `data/processed/*.parquet` |
| M2_04 | Data Integration | 120-150 min | `data/processed/merged.parquet` |

---

## ✅ Success Criteria

Before moving to Module 03, you should have:

### Artifacts Created
- [ ] Four completed notebooks (M2_01 through M2_04)
- [ ] Raw data files in `data/raw/`
- [ ] Processed data files in `data/processed/`
- [ ] Updated `data/raw/README.md` with data sources
- [ ] Updated `data/processed/README.md` with transformations

### Skills Demonstrated
- [ ] Successfully fetched data from at least 2 APIs
- [ ] Implemented error handling for API requests
- [ ] Validated data quality
- [ ] Merged datasets with different time granularities
- [ ] Saved data in appropriate formats
- [ ] Followed data organization best practices

### Understanding Achieved
- [ ] Understand API basics and REST principles
- [ ] Know when to use CSV vs JSON vs Parquet
- [ ] Can explain time alignment challenges
- [ ] Aware of rate limiting and error handling
- [ ] Appreciate importance of data documentation

---

## 🚀 Next Steps

After completing Module 02:

1. **Module 03: Data Exploration & Profiling**
   - Exploratory Data Analysis (EDA)
   - Statistical profiling
   - Data quality assessment
   - Visualization techniques

2. **Module 04: Feature Engineering**
   - Create time-based features
   - Engineer weather features
   - Derive business metrics

---

## 📚 Additional Resources

### Documentation
- 🌐 [CityBikes API Documentation](http://api.citybik.es/v2/)
- 🌦️ [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- 📊 [Pandas I/O Tools](https://pandas.pydata.org/docs/user_guide/io.html)
- 🔧 [Requests Library](https://requests.readthedocs.io/)

### Guides in This Repo
- 📖 [Open Data Sources](../open_data_sources.md)
- 💻 [Code Snippets](../code_snippets.md)
- 📐 [Coding Standards](../coding_standards.md)

### External Learning
- 📺 [REST API Concepts (YouTube)](https://www.youtube.com/watch?v=7YcW25PHnAA)
- 📖 [Working with APIs in Python](https://realpython.com/python-api/)
- 📚 [JSON Format Guide](https://www.json.org/json-en.html)

---

## 💪 You've Got This!

Data acquisition might seem intimidating at first, but remember:
- Start simple - get one API working first
- APIs are just URLs that return data
- Error handling gets easier with practice
- Documentation is your friend
- The community is here to help

**Ready to get started? Head to** [M2_01_amsterdam_bike_api.ipynb](../../notebooks/Module_02_Data_Acquisition/M2_01_amsterdam_bike_api.ipynb)!

---

*Last updated: 2026-01-15*
