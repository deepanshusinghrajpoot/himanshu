import React from 'react'



/*





🧠 What is the use of WITH in SQL?
=======================================
lll A CTE is a temporary named result set that exists only for the duration of the query.
    In SQL WITH keyword is used to create a Common Table Expression (CTE).




📌 Why do we use WITH?
--------------------------
1️⃣ Improves Readability & Structure

Breaks complex queries into logical, readable blocks
Makes SQL easier to understand and maintain




WITH dept_salary AS (
    SELECT dept, MAX(salary) AS max_salary
    FROM employees
    GROUP BY dept
)
   
SELECT *
FROM dept_salary;







*/




const Common_Table_Expression = () => {
  return (
    <div>Common_Table_Expression</div>
  )
}

export default Common_Table_Expression