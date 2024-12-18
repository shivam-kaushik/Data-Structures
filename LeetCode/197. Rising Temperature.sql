select W1.id from Weather W1 join Weather W2 
where W1.temperature > W2.temperature and 
datediff(W1.recordDate, W2.recordDate) = 1;