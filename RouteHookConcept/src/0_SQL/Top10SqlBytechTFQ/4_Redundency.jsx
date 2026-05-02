import React from 'react'

/*


Question
---------

Input to Output write a SQL query to convert the givent input into the expected output as shown below


📋 Parent Table (Input): city_distance

(Redundant distances between cities)

| from_city | to_city   | distance |
| --------- | --------- | -------- |
| Hyderabad | Bangalore | 570      |
| Bangalore | Hyderabad | 570      |
| Delhi     | Mumbai    | 1400     |
| Mumbai    | Delhi     | 1400     |
| Chennai   | Pune      | 1200     |


📤 Output Table (Expected Result)

| city_1    | city_2    | distance |
| --------- | --------- | -------- |
| Bangalore | Hyderabad | 570      |
| Delhi     | Mumbai    | 1400     |
| Chennai   | Pune      | 1200     |




Solution:-
----------

WITH cte AS
      ( 
        SELECT *,
        ROW_NUMBER() OVER() AS rn
        FROM  src_dest_distance
       )
SELECT t1.source, t1.destination, t1.distance
FROM cte t1
JOIN cte t2
        ON t1.rn < t2.rn
        AND t1.source = t2.destination
        AND t1.destination = t2.source;




🧠 Concept Explanation (Why This Works)
-----------------------------------------

1️⃣ Problem Nature
...................
The table contains bidirectional duplicates
(A → B) and (B → A) represent the same route
We must keep only one row per city pair

2️⃣ Role of ROW_NUMBER()
............................
ROW_NUMBER() assigns a unique number to each row
This helps in comparing two rows deterministically
Without row numbers, both (A → B) and (B → A) would match each other symmetrically

3️⃣ Why Self Join Is Used
............................
The table is joined with itself
Join conditions:
   t1.source = t2.destination
   t1.destination = t2.source

This matches:
Hyderabad → Bangalore with Bangalore → Hyderabad
Delhi → Mumbai with Mumbai → Delhi

4️⃣ Importance of t1.rn < t2.rn
................................
Ensures only one row is selected from each reverse pair

Prevents:
Duplicate output
A row matching with itself
Acts as a tie-breaker to keep a single direction

5️⃣ Why Chennai → Pune Is Excluded
...................................
There is no reverse row (Pune → Chennai)
Since the logic matches only reverse pairs, this row does not form a pair and is excluded


*/






const Redundency = () => {
  return (
    <div>4_Redundency</div>
  )
}

export default Redundency