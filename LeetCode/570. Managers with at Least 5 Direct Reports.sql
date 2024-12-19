SELECT name 
FROM Employee 
WHERE id IN (
    SELECT managerId 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5)

-- SELECT e1.name as name FROM Employee e1 join Employee e2 on e1.id = e2.managerId
-- group by e1.id , e1.name
-- having count(e2.managerId)>=5;