import React from 'react'


/*

Question 3
------------

Find actual distance from the given cars_travel table, find the actual distance travelled by
each car corresponding to each day.


SELECT * FROM car_travels;


SELECT *,
cummulative_distance - lag(cummulative_distance, 1, 0) OVER(PARTION BY car ODER BY days) AS distance_travell
FROM car_travels;




📋 Parent Table: car_travels

| car | day  | cummulative_distance |
| --- | ---- | -------------------- |
| A   | Day1 | 100                  |
| A   | Day2 | 180                  |
| A   | Day3 | 250                  |
| B   | Day1 | 50                   |
| B   | Day2 | 120                  |


🧠 Concept (Actual Distance Calculation)

The table stores cumulative distance, not daily distance
To get actual distance per day, we subtract:
today’s cumulative distance
minus previous day’s cumulative distance
LAG() is used to access the previous row value
PARTITION BY car ensures calculation is done separately for each ca
ORDER BY day ensures correct day-wise sequenc
Default value 0 in LAG() handles the first day

Formula:
actual_distance = current_cumulative - previous_cumulative

📤 Output Table

| car | day  | cummulative_distance | distance_travell |
| --- | ---- | -------------------- | ---------------- |
| A   | Day1 | 100                  | 100              |
| A   | Day2 | 180                  | 80               |
| A   | Day3 | 250                  | 70               |
| B   | Day1 | 50                   | 50               |
| B   | Day2 | 120                  | 70               |




*/








const Que_3 = () => {
  return (
    <div>3_Que</div>
  )
}

export default Que_3