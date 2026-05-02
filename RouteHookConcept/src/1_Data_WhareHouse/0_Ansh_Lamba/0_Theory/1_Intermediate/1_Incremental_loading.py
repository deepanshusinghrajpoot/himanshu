'''




## Incremental Loading ✅
=========================

---

## Concept ✅
--------------

"incremental loading is a technique where we load only new 
or changed data after the initial load."

- **Day 1:** Load all historical data  
  → Historical Data → Staging → Transform → Core Layer (Curated Data)

- **Day 2 onward:**  
  → Load only **new or updated data**  

- Avoids **full data reload every time**  
- Improves **performance and reduces storage usage**  

**Technique Used:**  
- CDC (**Change Data Capture**)  

**Interview Line:**  
lll "Incremental loading pushes only new or changed data after the initial full load."

---


## Flow in Data Warehouse Network ✅
-------------------------------------

### Day 1 (Full Load)
Database → Staging → Transform → Core Layer  

### Day 2+ (Incremental Load)
New/Changed Data → Staging → Transform → Core Layer  

---

## lll Staging Layer for Incremental Loading ✅
------------------------------------------------

There are two layer exist in staging layer.

### 🔹 Transient Layer (Most Common - 90%)

"In this approach, staging is cleared every time before loading new data."

- lll **Truncate staging table before each load**  
-     Load only **incremental data**  
-     it is Faster and widely used  

---

### 🔹 Persistence Layer (Less Common - 10%)

"In this approach, staging keeps historical data as well."

- lll **Don't truncate staging table**  
-     Load **new + historical data**  
-     it is Useful for **recovery scenarios**  


---
- lll CDC(**Change Data Capture**) technique helps identify **changed data**. 
---


## Key Interview Points ✅
--------------------------

"To summarize:"

- Incremental loading **improves efficiency and performance**  
- CDC(**Change Data Capture**) helps identify **changed data**  
- Staging layer handles **raw data before transformation**  
- Core layer always stores **clean, curated data**  

---

## 💡 Pro Tip (Interview)
--------------------------

"Think of Day 1 as moving the entire library, and Day 2 onward as adding only 
 new books to keep it updated efficiently."




'''