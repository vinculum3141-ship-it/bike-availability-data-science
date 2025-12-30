# 🌐 Open Data Sources

This document lists free, open data sources for the bike availability prediction project.

---

## 🚴 Bike Sharing Data

### Amsterdam Bike Data
- **Source**: City of Amsterdam Open Data Portal
- **URL**: https://data.amsterdam.nl/
- **API**: Real-time bike availability API
- **Description**: Real-time availability of bikes at bike-sharing stations
- **Update Frequency**: Real-time (every few minutes)
- **Data Fields**:
  - Station ID, name, location (lat/lon)
  - Number of available bikes
  - Number of available docks
  - Timestamp
  - Station status

### Alternative Bike Sharing Systems
- **CityBikes API**: http://api.citybik.es/v2/
  - Global bike-sharing data
  - Multiple cities worldwide
  - Free, no authentication required

- **Capital Bikeshare (Washington DC)**: 
  - https://www.capitalbikeshare.com/system-data
  - Historical trip data
  - Station information

---

## 🌦️ Weather Data

### KNMI (Royal Netherlands Meteorological Institute)
- **URL**: https://www.knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script
- **Description**: Dutch weather service with historical and real-time data
- **Access**: Free API, no authentication required
- **Data Fields**:
  - Temperature (current, min, max)
  - Precipitation
  - Wind speed and direction
  - Humidity
  - Air pressure
  - Visibility
  - Weather conditions

### Open-Meteo
- **URL**: https://open-meteo.com/
- **Description**: Free weather API with historical and forecast data
- **Access**: No API key required
- **Features**:
  - Historical weather data
  - 7-day forecasts
  - Hourly and daily data
  - Multiple locations worldwide

### OpenWeatherMap
- **URL**: https://openweathermap.org/api
- **Description**: Weather API with free tier
- **Access**: Free API key (limited calls/day)
- **Data**: Current, forecast, and historical weather

---

## 📅 Holiday & Event Data

### Netherlands Public Holidays
- **Source**: https://date.nager.at/Api
- **Description**: Public holidays for Netherlands
- **Access**: Free API
- **Use Case**: Feature for predicting increased/decreased bike usage

### School Holidays
- **Manual List**: Can be compiled from official Dutch education calendar
- **URL**: https://www.rijksoverheid.nl/onderwerpen/schoolvakanties

---

## 🗺️ Geographic Data

### OpenStreetMap
- **URL**: https://www.openstreetmap.org/
- **API**: Overpass API
- **Description**: Free geographic data
- **Use Cases**:
  - Points of interest near stations
  - Road networks
  - Public transport stops
  - Land use information

---

## 📊 Additional Useful Data

### Population & Demographics
- **CBS (Statistics Netherlands)**: https://www.cbs.nl/
- **Description**: Dutch population statistics by area
- **Access**: Open data portal

### Public Transport Data
- **NS (Dutch Railways)**: https://www.ns.nl/reisinformatie/ns-api
- **Description**: Train schedules and station information
- **Use Case**: Correlation with bike usage at train stations

---

## 🔑 API Best Practices

### Rate Limits
- **Respect API rate limits**
- Implement exponential backoff
- Cache responses when appropriate
- Use batch requests where available

### Authentication
```python
# Example: Store API keys in environment variables
import os

API_KEY = os.getenv('WEATHER_API_KEY')
```

### Error Handling
```python
import requests
import time

def fetch_with_retry(url, max_retries=3):
    for i in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if i == max_retries - 1:
                raise
            time.sleep(2 ** i)  # Exponential backoff
```

---

## 📝 Data Usage Guidelines

### Legal Considerations
- ✅ Check terms of service for each data source
- ✅ Cite data sources in your project
- ✅ Respect usage limits
- ✅ Don't redistribute without permission
- ✅ Use for educational purposes only

### Ethical Considerations
- Don't overload APIs with excessive requests
- Cache data to minimize repeated calls
- Be transparent about data sources
- Respect user privacy in public datasets

---

## 🔍 Finding More Data

### Open Data Portals
- **European Data Portal**: https://data.europa.eu/
- **Google Dataset Search**: https://datasetsearch.research.google.com/
- **Kaggle Datasets**: https://www.kaggle.com/datasets
- **Data.gov**: https://www.data.gov/ (US)

### Tips for Finding Data
1. Search for "{city} open data portal"
2. Look for government APIs
3. Check research repositories
4. Use dataset aggregators
5. Join open data communities

---

## 📚 Recommended Reading

- [Open Data Handbook](https://opendatahandbook.org/)
- [Best Practices for API Design](https://swagger.io/resources/articles/best-practices-in-api-design/)
- [Working with APIs in Python](https://realpython.com/api-integration-in-python/)

---

**Note**: Always verify that data sources are still active and accessible, as APIs and URLs may change over time.
