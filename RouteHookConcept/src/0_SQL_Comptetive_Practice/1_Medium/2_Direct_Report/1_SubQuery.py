'''



Method 2 : Sub Query Concept
============================




SELECT e.name 
FROM Employee e
WHERE e.id IN (
    SELECT m.managerId
    FROM Employee m
    GROUP BY m.managerId
    HAVING COUNT(m.managerId) >= 5
);




'''