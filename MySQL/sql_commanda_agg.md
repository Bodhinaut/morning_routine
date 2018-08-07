### Aggregate Functions
 

MIN	returns the smallest value in a given column
MAX	returns the largest value in a given column
SUM	returns the sum of the numeric values in a given column
AVG	returns the average value of a given column
COUNT	returns the total number of values in a given column
COUNT(*)	returns the number of rows in a table
Aggregate functions are used to compute against a "returned column of numeric data" from your SELECT statement. They basically summarize the results of a particular column of selected data. We are covering these here since they are required by the next topic, "GROUP BY". Although they are required for the "GROUP BY" clause, these functions can be used without the "GROUP BY" clause. For example:



SELECT AVG(salary)

FROM employee;

This statement will return a single result which contains the average value of everything returned in the salary column from the employee table.

Another example:


SELECT AVG(salary)


FROM employee

WHERE title = 'Programmer';
This statement will return the average salary for all employee whose title is equal to 'Programmer'

Example:


SELECT Count(*)

FROM employee;

This particular statement is slightly different from the other aggregate functions since there isn't a column supplied to the count function. This statement will return the number of rows in the employees table.

 

Use these tables for the exercises
items_ordered
customers
Review Exercises

Select the maximum price of any item ordered in the items_ordered table. Hint: Select the maximum price only.
Select the average price of all of the items ordered that were purchased in the month of Dec.
What are the total number of rows in the items_ordered table?
For all of the tents that were ordered in the items_ordered table, what is the price of the lowest tent? Hint: Your query should return the price only
