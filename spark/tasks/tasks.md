## 1. Basic Spark operations

Given a DataFrame of employee data:

| id | name    | dept  | salary |
|----|---------|-------|--------|
| 1  | Alice   | HR    | 5000   |
| 2  | Bob     | IT    | 6000   |
| 3  | Charlie | HR    | 4500   |
| 4  | David   | IT    | 7000   |
| 5  | Eve     | Sales | 5500   |

### Tasks
1. Filter employees from the **HR** department.
2. Add a new column `bonus` = 10% of `salary`.
3. Get the **average salary** by department.

## 2. Window functions
| id | region  | sale |
|----|---------|------|
| 1  | East    | 100  |
| 2  | East    | 200  |
| 3  | West    | 150  |
| 4  | East    | 50   |
| 5  | West    | 300  |

### Tasks
1. Rank sales within each region. 
2. Get the top 2 sales per region.

## 3. UDF
You have a DataFrame with names and want to extract the length of each name.
### Tasks:
1. Write a UDF to get name length.
2. Replace the UDF with a built-in function for better performance.

## 4. Explode and Array functions
Given the existing df with employees
### Tasks:
1. Explode favorite_colors so each color is a new row.
2. Count how many users like each color.

## 5. Complex joins
Problem:
You have two DataFrames: orders and customers.

| id  | employee_id | order_date |
|-----|-------------|------------|
| 100 | 1           | 2024-01-01 |
| 101 | 2           | 2024-01-03 |
| 102 | 3           | 2024-01-05 |
| 103 | 1           | 2024-01-07 |

## Tasks:
1. Join orders with employees.
2. Identify orders with missing employees.
3. Find employees with no orders.

## 6. Customer purchase frequency
You are given 2 tables, customers and transactions:

| id  | name    |
|-----|---------|
| 1   | Alice   |
| 2   | Bob     |
| 3   | Charlie |

| id  | customer_id  | order_date | amount |
|-----|--------------|------------|--------|
| 100 | 1            | 2024-01-01 | 200    |
| 101 | 2            | 2024-01-03 | 400    |
| 102 | 1            | 2024-01-05 | 150    |
| 103 | 1            | 2024-01-07 | 100    |

### Tasks:

1. Count the number of transactions per customer.
2. Find customers who have spent more than $300 in total.
3. Join results to show: name, total_spent, and txn_count.

## 7. Sessionize Web Logs

| user_id | timestamp         |
|---------|-------------------|
| 1       | 2024-01-01 10:00  |
| 1       | 2024-01-01 10:05  |
| 1       | 2024-01-01 11:00  |
| 2       | 2024-01-01 09:00  |
| 2       | 2024-01-01 09:45  |

### Tasks:
1. Define a session as a sequence of actions no more than 30 minutes apart.
2. Assign session numbers per user.