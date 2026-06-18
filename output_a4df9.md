# Query Report

**Session:** `qr-9e6a4df9`
**Query:** go to this site - https://www.centuryrealestate.in/ and fill random fake details (but should look like a valid one) and give me the details of what you have filled and verify it
**Generated:** 2026-06-19 02:09:49

---

## 1. Original User Goal

> go to this site - https://www.centuryrealestate.in/ and fill random fake details (but should look like a valid one) and give me the details of what you have filled and verify it


## 2. Planner DAG

**Graph nodes:**

- `n:1` **planner** [complete]  inputs=['USER_QUERY']
- `n:2` **browser** [failed]  inputs=[]
- `n:3` **formatter** [pending]  inputs=['USER_QUERY', 'n:2']

**Edges (data flow):**

  n:1 → n:2
  n:2 → n:3


## 3. Browser Path Chosen

**Node n:2**

- **Status:** failed
- **Error:** exception: HTTPStatusError: Server error '502 Bad Gateway' for url 'http://localhost:8109/v1/vision'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502



## 4. Browser Actions Taken




## 5. Screenshots / Page-State Logs

**Node n:2**


**Run directory: `browser_1781815093`**
**Layer: `a11y`**
- `turn_01_legend.txt` (140 bytes)
- `turn_01_raw.png` (416.3 KB)
- `turn_02_legend.txt` (140 bytes)
- `turn_02_raw.png` (362.6 KB)
- `turn_03_legend.txt` (140 bytes)
- `turn_03_raw.png` (301.7 KB)
- `turn_04_legend.txt` (140 bytes)
- `turn_04_raw.png` (106.9 KB)
- `turn_05_legend.txt` (140 bytes)
- `turn_05_raw.png` (404.9 KB)
- `turn_06_legend.txt` (140 bytes)
- `turn_06_raw.png` (120.9 KB)
- `turn_07_legend.txt` (140 bytes)
- `turn_07_raw.png` (307.8 KB)
- `turn_08_legend.txt` (140 bytes)
- `turn_08_raw.png` (176.2 KB)
- `turn_09_legend.txt` (140 bytes)
- `turn_09_raw.png` (414.5 KB)
- `turn_10_legend.txt` (140 bytes)
- `turn_10_raw.png` (181.8 KB)
- `turn_11_legend.txt` (140 bytes)
- `turn_11_raw.png` (225.1 KB)
- `turn_12_legend.txt` (140 bytes)
- `turn_12_raw.png` (215.8 KB)
**Layer: `vision`**
- `turn_01_legend.txt` (140 bytes)
- `turn_01_marked.png` (148.3 KB)
- `turn_01_raw.png` (156.7 KB)
- `turn_02_legend.txt` (140 bytes)
- `turn_02_marked.png` (386.0 KB)
- `turn_02_raw.png` (406.9 KB)
- `turn_03_legend.txt` (492 bytes)
- `turn_03_marked.png` (118.1 KB)
- `turn_03_raw.png` (118.6 KB)
- `turn_04_legend.txt` (490 bytes)
- `turn_04_marked.png` (175.2 KB)
- `turn_04_raw.png` (182.9 KB)
- `turn_05_legend.txt` (500 bytes)
- `turn_05_marked.png` (164.8 KB)
- `turn_05_raw.png` (168.0 KB)
- `turn_06_legend.txt` (521 bytes)
- `turn_06_marked.png` (214.1 KB)
- `turn_06_raw.png` (219.7 KB)
- `turn_07_legend.txt` (521 bytes)
- `turn_07_marked.png` (160.0 KB)
- `turn_07_raw.png` (162.5 KB)
- `turn_08_legend.txt` (521 bytes)
- `turn_08_marked.png` (154.8 KB)
- `turn_08_raw.png` (158.2 KB)
- `turn_09_legend.txt` (521 bytes)
- `turn_09_marked.png` (205.5 KB)
- `turn_09_raw.png` (211.4 KB)
- `turn_10_legend.txt` (521 bytes)
- `turn_10_marked.png` (208.0 KB)
- `turn_10_raw.png` (212.9 KB)
- `turn_11_legend.txt` (521 bytes)
- `turn_11_marked.png` (182.7 KB)
- `turn_11_raw.png` (188.8 KB)



## 6. Extracted Data

_(No extractable data found.)_


## 7. Final Comparison Table

_(No formatter output available.)_


## 8. Turn Count & Cost Summary

| Node      | Skill              | Status   | Time    | Gateway Ledger (calls / tokens) | Provider      | Turns |
| :-------- | :----------------- | :------- | :------ | :------------------------------- | :------------ | :---- |
| n:1      | planner            | complete |    4.7s | 1 calls                          | gemini       |      |
| n:2      | browser            | failed   |    0.0s | 23 calls                         | —            |      |
| **Total** | **2 nodes** |          | **4.7s** | **$0.000000** |                |       |

