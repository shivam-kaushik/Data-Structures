SELECT 
    Project.project_id, 
    ROUND(CAST(AVG(CAST(Employee.experience_years AS FLOAT)) AS FLOAT), 2) AS average_years
FROM 
    Project 
LEFT JOIN 
    Employee 
ON 
    Project.employee_id = Employee.employee_id
GROUP BY 
    Project.project_id;