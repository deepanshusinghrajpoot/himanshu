import React from 'react'

/*


Qus 1 :- Delete duplicate data from the given CARS table, delete the records where car details are duplicated
================================================================================================================

SELECT * FROM cars;


📋 Parent Table: cars
.........................
Assume this is the data:


| model_id | model_name | brand   |
| -------- | ---------- | ------- |
| 1        | Swift      | Maruti  |
| 2        | Swift      | Maruti  |
| 3        | City       | Honda   |
| 4        | City       | Honda   |
| 5        | City       | Honda   |
| 6        | Creta      | Hyundai |



👉 Duplicates are defined by (model_name, brand)
👉 We want only ONE row per (model_name, brand)
👉 Usually we keep the smallest model_id


✅ Solution 1
................
Keep MIN(model_id), delete the rest


DELETE
FROM cars
WHERE model_id NOT IN (
      SELECT MIN(model_id)
      FROM cars
      GROUP BY model_name, brand
);



🔍 How it works
Step 1: Subquery result


SELECT MIN(model_id)
FROM cars
GROUP BY model_name, brand;


| model_name | brand   | MIN(model_id) |
| ---------- | ------- | ------------- |
| Swift      | Maruti  | 1             |
| City       | Honda   | 3             |
| Creta      | Hyundai | 6             |

➡️ These are the rows we want to KEEP

Step 2: DELETE logic
DELETE FROM cars
WHERE model_id NOT IN (1, 3, 6);








✅ Solution 2 (BEST & INTERVIEW-FAVORITE ⭐)
-----------------------------------------------

Using ROW_NUMBER()
DELETE
FROM cars
WHERE model_id IN(
   SELECT model_id
   FROM (
      SELECT *,
      ROW_NUMBER() OVER(PARTITION BY model_name, brand ORDER BY model_id) AS rn
      FROM cars
   ) AS x
   WHERE x.rn > 1
);



🔍 How it works
Step 1: Window function output


| model_id | model_name | brand   | rn |
| -------- | ---------- | ------- | -- |
| 1        | Swift      | Maruti  | 1  |
| 2        | Swift      | Maruti  | 2  |
| 3        | City       | Honda   | 1  |
| 4        | City       | Honda   | 2  |
| 5        | City       | Honda   | 3  |
| 6        | Creta      | Hyundai | 1  |



*/



const Top10 = () => {
  return (
    <div>Top10</div>
  )
}

export default Top10