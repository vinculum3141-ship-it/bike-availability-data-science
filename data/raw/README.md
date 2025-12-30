# Raw Data Directory

This directory stores **original, unmodified data** from external sources.

---

## 📌 Purpose

Raw data is the source of truth for your analysis. Keep it:
- **Untouched**: Never modify files in this directory
- **Versioned**: Track when data was collected
- **Documented**: Record source, date, and method

---

## 📥 What Goes Here

### Bike Availability Data
- Files: `bike_availability_YYYY-MM.csv`
- Source: Amsterdam Open Data Portal API
- Format: CSV with timestamp, station_id, bikes_available, docks_available
- Collection method: API calls or manual download

### Weather Data
- Files: `weather_YYYY-MM.csv`
- Source: KNMI (Royal Netherlands Meteorological Institute)
- Format: CSV with hourly weather observations
- Variables: temperature, precipitation, wind, humidity

### Reference Data
- Files: `stations_info.csv`, `holidays_2024.csv`
- Source: Various (document in data dictionary)
- Purpose: Supporting information for analysis

---

## 📝 Naming Convention

Use consistent, descriptive names:

```
{data_type}_{time_period}_{version}.{extension}

Examples:
- bike_availability_2024-01.csv
- weather_2024-01-to-03.csv
- stations_info_v2.json
```

---

## 🚫 What NOT to Store Here

- ❌ Processed/cleaned data → use `data/processed/`
- ❌ Feature-engineered data → use `data/processed/`
- ❌ Model outputs → use separate output directory
- ❌ Large files (>100MB) → add to `.gitignore`, use cloud storage
- ❌ Temporary files → delete after use

---

## 📚 Data Documentation

For each dataset, document:

1. **Source**: Where did it come from?
2. **Date Collected**: When was it downloaded?
3. **Collection Method**: API, manual download, scraping?
4. **Coverage**: Time range, geographic area
5. **Known Issues**: Missing data, outliers, errors

Create a `data_dictionary.md` or use this template:

```markdown
## Dataset: bike_availability_2024-01.csv

**Source**: Amsterdam Open Data Portal  
**URL**: https://data.amsterdam.nl/...  
**Date Collected**: 2024-02-01  
**Method**: API calls using `src/data_acquisition.py`  
**Time Range**: 2024-01-01 to 2024-01-31  
**Records**: 372,000 hourly observations  
**Stations**: 50 bike-sharing stations  

**Known Issues**:
- Missing data on 2024-01-15 (API outage)
- Station 23 had sensor malfunction Jan 10-12
```

---

## 💾 Storage Best Practices

### For Small Files (<10MB)
```bash
# Add to git
git add data/raw/bike_data_sample.csv
git commit -m "Add sample bike data for January 2024"
```

### For Large Files (>10MB)
```bash
# Add to .gitignore
echo "data/raw/large_dataset.csv" >> .gitignore

# Document location in README instead
# "Large files stored in Google Drive: [link]"
```

### For Very Large Files (>100MB)
- Use cloud storage (Google Drive, AWS S3, Azure Blob)
- Use Git LFS (Large File Storage)
- Provide download script in `src/data_acquisition.py`

---

## 🔄 Data Versioning

Track data changes:

```bash
# Method 1: Timestamp in filename
bike_availability_2024-01_downloaded-2024-02-01.csv

# Method 2: Version number
bike_availability_v1.csv
bike_availability_v2.csv

# Method 3: Data versioning tool (DVC)
dvc add data/raw/bike_data.csv
git add data/raw/bike_data.csv.dvc
```

---

## ✅ Checklist: Adding New Raw Data

Before adding new data to this directory:

- [ ] Downloaded from documented source
- [ ] Named according to convention
- [ ] Documented in README or data dictionary
- [ ] Checked file size (add to .gitignore if large)
- [ ] Verified data quality (spot check)
- [ ] Noted collection date
- [ ] Recorded any known issues

---

## 📖 Example Directory Structure

```
data/raw/
├── README.md (this file)
├── .gitkeep
├── bike_availability_2024-01.csv
├── bike_availability_2024-02.csv
├── bike_availability_2024-03.csv
├── weather_2024-Q1.csv
├── stations_info.json
├── holidays_2024.csv
└── data_dictionary.md
```

---

## 🔗 Related Resources

- [Data Acquisition Module](../../notebooks/Module_02_Data_Acquisition/)
- [Open Data Sources](../../docs/open_data_sources.md)
- [Data Processing Guide](../processed/README.md)

---

**Remember**: Raw data should remain raw. All transformations happen in notebooks or scripts, with results saved to `data/processed/`! 📊
