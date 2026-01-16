# Module 02: Data Acquisition - Self Evaluation

**Your Name**: [Your Name]  
**Date Completed**: [YYYY-MM-DD]  
**Module**: Module 02 - Data Acquisition

---

## 📋 Completion Checklist

### Notebooks Completed

- [ ] **M2_01_amsterdam_bike_api.ipynb** - Amsterdam Bike Data Acquisition
  - [ ] Successfully fetched data from CityBikes API
  - [ ] Implemented error handling for API requests
  - [ ] Created station map visualization
  - [ ] Saved raw bike data with metadata

- [ ] **M2_02_weather_data_api.ipynb** - Weather Data Acquisition
  - [ ] Successfully fetched weather data from Open-Meteo API
  - [ ] Calculated bikeability score based on weather conditions
  - [ ] Validated weather data quality
  - [ ] Saved processed weather data

- [ ] **M2_03_data_storage.ipynb** - Data Storage Patterns
  - [ ] Compared file formats (CSV, JSON, Parquet, Feather)
  - [ ] Implemented data versioning system
  - [ ] Created data documentation and catalog
  - [ ] Set up proper .gitignore for data files

- [ ] **M2_04_merge_datasets.ipynb** - Merge Datasets
  - [ ] Merged bike and weather data successfully
  - [ ] Implemented time alignment strategies
  - [ ] Handled missing data appropriately
  - [ ] Validated and saved final merged dataset

### Artifacts Created

- [ ] Raw bike data files in `data/raw/`
- [ ] Raw weather data files in `data/raw/`
- [ ] Processed/merged data files in `data/processed/`
- [ ] Metadata files for all datasets
- [ ] Updated `data/raw/README.md` documenting data sources
- [ ] Updated `data/processed/README.md` documenting transformations

---

## 🎯 Learning Objectives Assessment

Rate your understanding (1-5 scale: 1=Beginner, 5=Expert)

### Technical Skills

| Skill | Rating (1-5) | Notes |
|-------|--------------|-------|
| Fetch data from REST APIs | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Parse JSON responses | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Implement error handling | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Validate data quality | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Save data in different formats | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Merge datasets with time alignment | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Handle missing timestamps | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Create data documentation | ☐1 ☐2 ☐3 ☐4 ☐5 | |

### Best Practices

| Practice | Implemented? | Notes |
|----------|--------------|-------|
| Never modify raw data | ☐ Yes ☐ No | |
| Document data sources | ☐ Yes ☐ No | |
| Version datasets | ☐ Yes ☐ No | |
| Validate before saving | ☐ Yes ☐ No | |
| Use appropriate file formats | ☐ Yes ☐ No | |
| Never commit API keys | ☐ Yes ☐ No | |
| Proper .gitignore setup | ☐ Yes ☐ No | |
| Create metadata files | ☐ Yes ☐ No | |

### Conceptual Understanding

**Answer these questions to assess your understanding:**

1. **When would you choose Parquet over CSV?**
   
   [Your answer here]

2. **What are the main challenges when merging datasets with different time granularities?**
   
   [Your answer here]

3. **Why is it important to never modify raw data files?**
   
   [Your answer here]

4. **How would you handle API rate limits in a production system?**
   
   [Your answer here]

5. **What information should always be included in data documentation?**
   
   [Your answer here]

---

## 💡 Reflection

### What I Learned

**Top 3 key takeaways from this module:**

1. [Your takeaway #1]

2. [Your takeaway #2]

3. [Your takeaway #3]

### Challenges Encountered

**Describe challenges you faced and how you overcame them:**

| Challenge | Solution | What I Learned |
|-----------|----------|----------------|
| [Challenge 1] | [How you solved it] | [Lesson learned] |
| [Challenge 2] | [How you solved it] | [Lesson learned] |
| [Challenge 3] | [How you solved it] | [Lesson learned] |

### Areas for Improvement

**What topics do you want to review or practice more?**

- [ ] [Topic 1]
- [ ] [Topic 2]
- [ ] [Topic 3]

---

## 🚀 Real-World Application

### How would you apply these skills?

**Describe a real-world scenario where you would use data acquisition skills:**

[Your scenario here - e.g., "I would use these skills to build a system that fetches weather and traffic data to predict delivery times for a food delivery service..."]

### Dataset Ideas

**What other datasets would you like to acquire and analyze?**

1. [Dataset idea 1 - source, purpose]
2. [Dataset idea 2 - source, purpose]
3. [Dataset idea 3 - source, purpose]

---

## 📊 Data Quality Assessment

### Review Your Final Dataset

Answer these questions about your merged bike-weather dataset:

| Question | Answer |
|----------|--------|
| How many rows in final dataset? | |
| How many columns? | |
| Date range covered? | |
| Completeness (% non-null)? | |
| Number of stations? | |
| Any data quality issues? | |
| Correlation: bikes vs temperature? | |
| Correlation: bikes vs precipitation? | |

### Data Files Inventory

List all data files you created:

**Raw Data:**
- [ ] `amsterdam_bike_[timestamp].json` - [Size: XX KB, Records: XX]
- [ ] `amsterdam_bike_[timestamp].csv` - [Size: XX KB, Records: XX]
- [ ] `weather_amsterdam_[timestamp].csv` - [Size: XX KB, Records: XX]
- [ ] Metadata files for each dataset

**Processed Data:**
- [ ] `bike_weather_merged_[timestamp].parquet` - [Size: XX KB, Records: XX]
- [ ] `bike_weather_merged_[timestamp].csv` - [Size: XX KB, Records: XX]
- [ ] Documentation and metadata files

---

## ✅ Module Completion Criteria

Check all that apply:

### Required (Must Complete)

- [ ] All 4 notebooks completed and executed successfully
- [ ] Fetched data from at least 2 different APIs
- [ ] Raw data saved in `data/raw/` directory
- [ ] Processed data saved in `data/processed/` directory
- [ ] Data quality validated
- [ ] Datasets merged with time alignment
- [ ] No API keys committed to git

### Recommended (Strongly Suggested)

- [ ] Implemented error handling in all API calls
- [ ] Created metadata for all datasets
- [ ] Documented data sources in README files
- [ ] Compared multiple file formats
- [ ] Implemented data versioning
- [ ] Created data catalog
- [ ] All learner tasks completed

### Optional (Going Above and Beyond)

- [ ] Automated data collection with scheduled scripts
- [ ] Implemented retry logic with exponential backoff
- [ ] Created data quality dashboard
- [ ] Fetched data from additional sources (holidays, traffic, etc.)
- [ ] Built reusable data pipeline
- [ ] Created comprehensive data documentation

---

## 📝 Final Self-Assessment

### Overall Module Completion

**Rate your overall completion of Module 02:**

☐ **100%** - Completed everything, including optional challenges  
☐ **90-99%** - Completed all required work and most recommended tasks  
☐ **80-89%** - Completed all required work and some recommended tasks  
☐ **70-79%** - Completed all required work  
☐ **Below 70%** - Some required work incomplete

### Confidence Level

**How confident do you feel with data acquisition skills?**

☐ **Very Confident** - I can independently acquire and integrate data from multiple sources  
☐ **Confident** - I understand the concepts and can implement with minor guidance  
☐ **Somewhat Confident** - I grasp the basics but need more practice  
☐ **Not Confident** - I need to review the material and practice more

### Ready for Next Module?

**Do you feel ready to proceed to Module 03: Data Exploration & Profiling?**

☐ **Yes** - I'm confident with the material and excited to move forward  
☐ **Almost** - I want to review a few topics but generally feel ready  
☐ **Not Yet** - I need more practice before moving on

**If "Not Yet", what specific topics do you want to review?**

[Your answer here]

---

## 🎓 Instructor Review (Optional)

**If you're working with an instructor or mentor, have them complete this section:**

### Instructor Comments

**Strengths observed:**

[Instructor feedback]

**Areas for improvement:**

[Instructor feedback]

**Recommendations:**

[Instructor feedback]

**Approved to proceed to Module 03?**

☐ Yes ☐ No (needs revision)

**Instructor Signature**: _________________ **Date**: _________

---

## 📚 Additional Resources Reviewed

**List any additional resources you explored beyond the module content:**

- [ ] [Resource name and link]
- [ ] [Resource name and link]
- [ ] [Resource name and link]

---

## 🎉 Celebration!

**You've completed Module 02! Take a moment to acknowledge your progress.**

**What are you most proud of accomplishing in this module?**

[Your reflection here]

**What excites you most about the next module?**

[Your thoughts here]

---

**Date Completed**: __________________

**Ready for Module 03**: ☐ Yes ☐ Need Review

**Signature**: ______________________

---

*Keep this evaluation for your records. It will help you track your progress throughout the course and identify areas for continued growth.*
