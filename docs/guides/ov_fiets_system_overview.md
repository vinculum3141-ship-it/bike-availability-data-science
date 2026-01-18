# 🚲 OV-fiets System Overview

**Document Purpose:** Provide learners with essential domain knowledge about the OV-fiets bike-sharing system to inform data science decisions.

**Last Updated:** January 18, 2026

---

## 🌍 What is OV-fiets?

**OV-fiets** (Public Transport Bike) is the Netherlands' national bike-sharing system, operated by NS (Dutch Railways). It's designed to solve the **"last mile problem"** — bridging the gap between train stations and final destinations.

### Key Statistics
- **450+ locations** across the Netherlands (primarily at train stations)
- **20,000+ bikes** in circulation
- **4+ million rentals** per year
- **Integrated with OV-chipkaart** (public transport smart card)

---

## 🏗️ System Architecture

### Station-Based, No-Dock Design

Unlike many bike-sharing systems (e.g., Citi Bike, Santander Cycles), **OV-fiets does not use docking stations**:

- **Storage:** Bikes are stored inside secure bike parking facilities at train stations
- **Staff-managed:** NS staff handle bike distribution and maintenance
- **Same-station returns:** Bikes must be returned to the **same station** where they were rented (with rare exceptions for specific inter-station agreements)
- **No GPS tracking:** Bikes are not tracked in real-time during rental periods

**Implications for Data Science:**
- Availability data reflects **bikes in facility**, not bikes in docks
- Cannot track bike movement during rental
- Returns must be predicted for the same station
- No rebalancing algorithms (unlike dock-based systems)

---

## 🔄 Operational Constraints

### 1. **Real-Time Data Refresh**
- **API update frequency:** ~15 minutes
- **Data staleness:** Predictions older than 15 minutes may be outdated
- **Use case impact:** Short-term predictions (2-4 hours) are most actionable

### 2. **Rental Duration**
- **Maximum rental period:** 72 hours (3 days)
- **Typical rental:** 1-4 hours for commuters, 12-48 hours for tourists
- **Late fees:** Apply after 72 hours

### 3. **Access Requirements**
- **OV-chipkaart:** Required for all rentals (no casual/tourist option without registration)
- **Subscription fee:** €0.01/year + €4.15 per 24-hour rental period
- **Advance registration:** Users must activate OV-fiets on their card before first use

### 4. **Station Capacity**
- **Varies by location:** Major stations (Amsterdam Centraal, Utrecht Centraal) have 100+ bikes; small stations may have 10-20
- **No overflow:** If facility is full, bikes cannot be returned (user must wait or find another location)
- **Stockouts:** Common during peak hours at commuter-heavy stations

---

## 👥 User Populations

### Commuters (Primary User Base)
**Characteristics:**
- Daily or weekly users
- Predictable patterns (morning/evening peaks)
- Short rentals (1-4 hours)
- Same route repeatedly

**Prediction Challenge:**
- Binary classification: "Will bikes be available at 8 AM tomorrow?" (Track A)

### Tourists / Multi-Day Users (Secondary User Base)
**Characteristics:**
- Occasional users
- Weekend/holiday spikes
- Long rentals (12-72 hours)
- Explore multiple destinations

**Prediction Challenge:**
- Regression: "How many bikes will be available next Saturday?" (Track B)
- Time series: "Forecast availability for the next 3 days" (Track B)

---

## 📊 Data Characteristics

### What the Data Includes
- **Station ID** and name
- **Current bike count** (bikes in facility, not rented)
- **Timestamp** (updated every ~15 minutes)
- **Location** (latitude, longitude)

### What the Data Does NOT Include
- Individual bike IDs or tracking
- User demographics
- Rental start/end times
- Trip origins/destinations
- Maintenance schedules
- Staff interventions (manual rebalancing)

### Data Quality Considerations
- **Missing values:** Occasional API downtime or station offline
- **Outliers:** Sudden spikes (bulk returns after events)
- **Anomalies:** Station closures, capacity changes, system upgrades

---

## 🎯 Why This Matters for Data Science

### Domain Knowledge Shapes Modeling Decisions

1. **Feature Engineering:**
   - Train schedules matter (commuter peaks align with train arrivals)
   - Holiday calendars matter (tourist demand spikes)
   - Weather matters differently for commuters (willing to bike in rain) vs tourists (avoid rain)

2. **Model Selection:**
   - **Classification (Track A):** Best for "is a bike available?" (commuter use case)
   - **Regression (Track B):** Best for "how many bikes?" (capacity planning)
   - **Time series (Track B):** Best for multi-day forecasts (tourist use case)

3. **Validation Strategy:**
   - Must account for 15-minute data staleness
   - Cannot validate beyond 72-hour rental period
   - Peak hour predictions more critical than off-peak

4. **Business Impact:**
   - **Commuters:** Need high availability during peak hours (8-9 AM, 5-6 PM)
   - **Tourists:** Need multi-day forecasts for trip planning
   - **NS Operations:** Need capacity planning to optimize bike distribution

---

## 🔗 Data Sources

### Primary Data Source
- **API:** CityBikes API (Amsterdam OV-fiets endpoint)
- **Documentation:** https://api.citybik.es/v2/
- **Update frequency:** ~15 minutes
- **No API key required:** Open data

### Supplementary Data
- **Weather:** KNMI (Royal Netherlands Meteorological Institute) or OpenWeatherMap
- **Train schedules:** NS API (optional, requires API key)
- **Holiday calendar:** Dutch national holidays, school vacations
- **Events:** Amsterdam event calendars (optional)

---

## 🚀 Next Steps

- **Track A learners:** Focus on commuter patterns, short-term classification
- **Track B learners:** Explore tourist patterns, long-term regression/time series

**Related Documents:**
- [Use Case Comparison](use_case_comparison.md) — Compare commuter vs tourist prediction problems
- [Learning Pathways](learning_pathways.md) — Choose your track
- [Open Data Sources](../references/open_data_sources.md) — Detailed data source documentation

---

**Document Maintainer:** Course Development Team  
**Questions?** See [open_data_sources.md](open_data_sources.md) for API details.
