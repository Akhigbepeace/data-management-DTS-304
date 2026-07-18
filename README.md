# DTS 304 — Data Management I: TMA Project

**Tutor-Marked Assessment**
**Course:** DTS 304 — Data Management I
**Institution:** MIVA Open University
**Title:** Design and Implementation of a Scalable Information Management System for a Retail Business

---

## Project Overview

This project simulates the design and partial implementation of an integrated information management system for a retail company similar to TIMA Corporation. It applies data management concepts from Weeks 1–4, covering data capture, representation, indexing, retrieval, and search simulation.

---

## Repository Structure

```
DTS304-TMA/
├── data/
│   └── purchases.csv          # Dataset captured via Google Forms (30 entries)
├── sql/
│   └── retail_db.sql          # Database creation, import, and index implementation
├── scripts/
│   └── search_simulation.py   # Binary search vs sequential search comparison
├── screenshots/               # Query result screenshots and script outputs
├── report/
│   └── TMA_Report.pdf         # Full project report
└── README.md
```

---

## Steps Completed

### Step 1 — Data Capture & Representation (Week 2)
- Designed a customer purchase form using **Google Forms**
- Captured fields: Customer Name, Purchase Date, Product ID, Product Category, Amount
- Collected **30 entries** representing retail transactions
- Data exported and stored in structured **CSV format** (`data/purchases.csv`)

### Step 2 — Data Indexing & Retrieval (Week 3)
- Created a relational database using **SQLite**
- Imported the captured dataset into the database
- Implemented the following indexes:
  - **Primary index** on `customer_id`
  - **Secondary index** on `product_category`
  - **Non-clustered index** on `purchase_date`
- Wrote SQL queries to:
  - Retrieve all purchases within a specific date range
  - Retrieve all purchases in a given product category
- SQL file: `sql/retail_db.sql`

### Step 3 — Search Simulation (Week 3–5)
- Implemented **binary search** in Python to locate a specific Product ID
- Simulated **sequential search** on the same dataset for performance comparison
- Demonstrated that binary search is significantly faster on sorted data
- Script: `scripts/search_simulation.py`

---

## Dataset Summary

| Field | Description |
|-------|-------------|
| Customer Name | Full name of the purchasing customer |
| Purchase Date | Date the transaction occurred |
| Product ID | Unique identifier for each product (PRD1001–PRD1030) |
| Product Category | Electronics, Food, Clothing and Textile, Health and Beauty |
| Amount (₦) | Transaction value in Nigerian Naira |

**Total records:** 30
**Date range:** June 1, 2026 – July 9, 2026
**Categories covered:** 4 (Electronics, Food, Clothing and Textile, Health and Beauty)

---

## Key Concepts Applied

- **Data Capture:** Manual and form-based capture using Google Forms
- **Data Representation:** Structured tabular format (CSV)
- **Indexing:** Primary, Secondary, and Non-clustered indexes
- **Search Techniques:** Sequential search vs Binary search
- **Database:** SQLite relational database with SQL queries

---

## How to Run

### SQL (requires SQLite)
```bash
sqlite3 retail.db < sql/retail_db.sql
```

### Python Search Script
```bash
python scripts/search_simulation.py
```

---

## Submission Format
Final submission zipped as: `DTS304_TMA_Submission.zip` containing all files above.
