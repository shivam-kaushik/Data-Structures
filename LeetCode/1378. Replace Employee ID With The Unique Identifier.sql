select EmployeeUNI.unique_id, Employees.name from Employees 
left Join EmployeeUNI On Employees.id = EmployeeUNI.id;