# 🚇 Assignment 1: Metro Route & Fare Data Automation

## 📌 Project Overview

This project is a Python-based automation system that collects **metro route, fare, total travel time, and intermediate station details** using the **UP Metro Rail (UPMRC) public API**.

The script processes all possible source–destination station pairs, extracts relevant route information, and stores the results in a structured CSV file for analysis and reuse.

---

## 🎯 Objective

- Automate metro route and fare data collection  
- Eliminate manual data gathering  
- Demonstrate API integration and data processing  
- Generate a clean and reusable dataset  

---

## 🧠 Overview of `station.py`

The `station.py` script reads station data from a CSV file, dynamically calls the UPMRC API for each station pair, extracts route information, applies rate limiting, and stores the processed data into a CSV file.

---

## 🔧 Technologies & Libraries Used

- **Python 3**
- **requests** – API calls  
- **pandas** – CSV handling and data processing  
- **time** – Rate limiting  
- **os** – Directory management  

---

## ⚙️ Configuration Details

- **Input File:** `Stations.csv`  
- **Output File:** `output/Fares.csv`  
- **API:** UPMRC Route API  
- **Request Delay:** 0.5 seconds  

---

## 🔄 Explanation of `station.py` (Important Logic)

### 📌 Purpose of the Script

`station.py` automatically fetches metro route, fare, travel time, and intermediate station details between all station pairs using the official UPMRC API and saves the processed data into a CSV file.

---

### 🔧 Imports Used

- `requests` – API communication  
- `pandas` – Data processing  
- `time` – API rate limiting  
- `os` – Output folder creation  

---

### 🌐 API URL Builder Function

- Dynamically creates API URLs for any source → destination  
- Uses least-distance route logic  
- Improves modularity and readability  

---

### 📥 Reading Station Data

- Reads `Stations.csv`
- Extracts station codes and names
- Creates a lookup dictionary for fast access  

---

### 🔁 Core Processing Logic

- Uses nested loops to generate **all station combinations**
- Skips same source and destination
- Total API calls: `N × (N − 1)`
- Ensures complete network traversal  

---

### 📡 API Handling & Data Extraction

- Sends API requests with headers and timeout  
- Skips failed responses safely  
- Extracts fare, total travel time, and station path  

---

### 🚏 Intermediate Station Logic

- Removes source and destination stations
- Stores only intermediate stops  

---

### 📁 Output Handling

- Automatically creates `output/` folder
- Writes results to `output/Fares.csv`
- Overwrites old data to keep output updated  

---

## 📊 Flowchart of `station.py`

```mermaid
flowchart TD
    A[Start Script] --> B[Read Stations.csv]
    B --> C[Extract station codes & names]
    C --> D[Initialize results list]

    D --> E[Select Source Station]
    E --> F[Select Destination Station]

    F --> G{Source == Destination?}
    G -- Yes --> F
    G -- No --> H[Build API URL]

    H --> I[Send API Request]
    I --> J{Response OK?}

    J -- No --> F
    J -- Yes --> K[Parse JSON Response]

    K --> L[Extract fare, time & path]
    L --> M[Extract intermediate stations]
    M --> N[Store result]

    N --> O[Wait REQUEST_DELAY]
    O --> F

    F -->|All destinations done| P[Next source]
    P -->|All sources done| Q[Create output folder]
    Q --> R[Write Fares.csv]
    R --> S[End Script]
