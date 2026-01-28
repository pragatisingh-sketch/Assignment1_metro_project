

**A metro network simulation project in Python**  

This project represents data related to a metro system using Python. It loads metro stations from a dataset and provides functionality to work with the stations programmatically.

---

## 🧾 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Dataset](#dataset)  
4. [Installation](#installation)  
6. [Project Structure and flowchart](#project-structure-and-flowchart)
7. [Usage](#usage)
8. [Explanation of `station.py` (Important Logic)]
9. [Dependencies](#dependencies)
10. Explanation of station.py


---

## 📌 Overview

This project is a **Python-based agra metro** data processor that uses a CSV file (stations list) and code (`station.py`) to load and manipulate station data.
The intent is to practice programming concepts and handling metro system information.

---

## 🔍 Features

- Loads metro station data from `Stations.csv`  
- Represents each station using a Python class  
- Outputs results or logs to the `output/Fares.csv` directory  

## 📋 Dataset

The dataset `Stations.csv` contains the list of metro stations and related information that the Python script uses.
For example ---
id, station_code, station_name
1,  TEGT,         TAJ EAST GATE
2,  SCSG,         SHAHEED CAPTAIN SHUBHAM GUPTA
3,  FTBR,         FATEHABAD ROAD
34, TJML,         TAJ MAHAL
35, AFTM,         AGRA FORT
36, MKM,          MANKAMESHWAR MANDIR


## 🚀 Installation

 **Clone the repository**

   git clone https://github.com/pragatisingh-sketch/Assignment1_metro_project.git
   cd Assignment1_metro_project

## 🗂️ Project Structure and flow 
Assignment1_metro_project/
├── .venv/                # Python virtual environment folder
├── output/               # Results or demo outputs
├── Stations.csv          # Metro stations data
├── station.py            # Python code
└── README.md             # (This file)

+--------------------+
|   Start Script     |
+--------------------+
          |
          v
+--------------------+
| Read Stations.csv  |
+--------------------+
          |
          v
+------------------------------+
| Extract station codes & names|
+------------------------------+
          |
          v
+------------------------------+
| Initialize empty result list |
+------------------------------+
          |
          v
+------------------------------+
| Select Source Station        |
+------------------------------+
          |
          v
+------------------------------+
| Select Destination Station   |
+------------------------------+
          |
          v
+------------------------------+
| Source == Destination ?      |
+------------------------------+
      | Yes              | No
      v                  v
+-----------+    +----------------------+
| Skip Pair |    | Build API URL        |
+-----------+    +----------------------+
                           |
                           v
                  +----------------------+
                  | Send API Request     |
                  +----------------------+
                           |
                           v
                  +----------------------+
                  | Response OK ?        |
                  +----------------------+
                      | No        | Yes
                      v           v
                 +---------+  +----------------------+
                 | Skip    |  | Parse JSON Response  |
                 +---------+  +----------------------+
                                      |
                                      v
                        +-------------------------------+
                        | Extract fare, time & path     |
                        +-------------------------------+
                                      |
                                      v
                        +-------------------------------+
                        | Get intermediate stations     |
                        +-------------------------------+
                                      |
                                      v
                        +-------------------------------+
                        | Store data in result list     |
                        +-------------------------------+
                                      |
                                      v
                        +-------------------------------+
                        | Wait (REQUEST_DELAY)          |
                        +-------------------------------+
                                      |
                                      v
                        (Repeat for all station pairs)
                                      |
                                      v
+------------------------------+
| Create output folder         |
+------------------------------+
          |
          v
+------------------------------+
| Write data to Fares.csv      |
+------------------------------+
          |
          v
+--------------------+
|   End Script       |
+--------------------+


## 🧠 Usage 

python station.py


## Explanation of `station.py` (Important Logic)


`station.py` automatically fetches **metro route, fare, travel time, and intermediate station details** for **all possible station pairs** using the official **UPMRC API** and 
stores the processed data in a CSV file.

This demonstrates:

* API integration
* Automated data processing
* Real-world data engineering concepts

---

🔧 Imports Used (Why They Matter)

* **requests** – Calls the metro route API
* **pandas** – Reads input CSV and generates output CSV
* **time** – Adds delay between API calls (rate limiting)
* **os** – Handles output directory creation

---

 ⚙️ Configuration Section

* `Stations.csv` → Input station data
* `output/Fares.csv` → Output file
* Centralized API base URL for easy reuse

`REQUEST_DELAY = 0.5` ensures responsible API usage and avoids server blocking.

---

 🌐 API URL Builder Function

* Dynamically generates API URLs for **any source → destination**
* Uses **least-distance route logic**
* Keeps the code modular and readable

---

 📥 Reading Station Data

* Reads station codes and names from `Stations.csv`
* Creates a lookup dictionary for fast station code → name mapping

---

 🔁 Core Logic: Nested Loop

* Iterates through **all station combinations**
* Skips same source and destination
* Total API calls:

  ```
  N × (N − 1)
  ```
* Ensures complete metro network traversal

---

 📡 API Request Handling

* Sends GET requests with timeout and headers
* Skips failed or invalid responses safely
* Prevents crashes using error handling

---

 🧾 JSON Data Extraction

From the API response, the script extracts:

* Fare
* Total travel time
* Complete station path

---

 🚏 Intermediate Station Logic

* Removes source and destination stations
* Stores only intermediate stops
* Useful for route analysis and network optimization

 🗃️ Structured Result Storage

Each route is stored with:

* Source & destination codes and names
* Fare and total time
* Intermediate station count and names

The data is CSV-ready and well structured.

 ⏳ Rate Limiting

* Adds delay between API calls
* Prevents API abuse
* Follows production-grade best practices

 📁 Output Handling

* Automatically creates the `output/` directory
* Writes all results to `output/Fares.csv`
* Overwrites old data to keep output updated



### ✅ Final Outcome

The script generates a CSV containing:

* All source → destination routes
* Fare and travel time
* Intermediate station details

This output can be used for **analysis, dashboards, ERP systems, and metro planning tools**.
Database Drive link --
https://drive.google.com/file/d/199p42IpLONUWAauu7_sulHTaj7_P5rrD/view?usp=sharing


## 📦 Dependencies

This project uses basic Python libraries. If you used any external packages, list them here (e.g., pandas, numpy).

## ✉️ Contact

Created by Pragati Singh — feel free to reach out on GitHub.


